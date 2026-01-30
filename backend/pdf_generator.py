from playwright.sync_api import sync_playwright
from jinja2 import Environment, FileSystemLoader
import os
import tempfile

BASE_DIR = os.path.dirname(__file__)

def generate_pdf(data):
    env = Environment(loader=FileSystemLoader(os.path.join(BASE_DIR, "templates")))
    template = env.get_template("purchase_order.html")
    html_content = template.render(**data)

    with tempfile.NamedTemporaryFile(delete=False, suffix=".html", mode="w", encoding="utf-8") as f:
        f.write(html_content)
        html_path = f.name

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(f"file:///{html_path}")
        pdf_bytes = page.pdf(
            format="A4",
            print_background=True,
            margin={
                "top": "15mm",
                "bottom": "15mm",
                "left": "15mm",
                "right": "15mm"
            }
        )
        browser.close()

    os.remove(html_path)
    return pdf_bytes
