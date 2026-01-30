from fastapi import FastAPI
from fastapi.responses import StreamingResponse, HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from schemas import PurchaseOrder
from utils import calculate_totals
from pdf_generator import generate_pdf
from io import BytesIO
import os

app = FastAPI()

# CORS (dev safe)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# ✅ Serve frontend folder
app.mount("/frontend", StaticFiles(directory=os.path.join(BASE_DIR, "frontend")), name="frontend")

# ✅ Serve static files (logo, signature)
app.mount(
    "/static",
    StaticFiles(directory=os.path.join(BASE_DIR, "static")),
    name="static"
)

# ✅ Open index.html when root URL is hit
@app.get("/", response_class=HTMLResponse)
def open_index():
    index_path = os.path.join(BASE_DIR, "frontend", "index.html")
    with open(index_path, "r", encoding="utf-8") as f:
        return f.read()

# ✅ Generate PDF API
@app.post("/generate-pdf")
def generate_po(po: PurchaseOrder):

    totals = calculate_totals(po.items)

    data = {
        **po.dict(),
        **totals,
        "logo_path": "http://127.0.0.1:8000/static/logo.png",
        "signature_path": "http://127.0.0.1:8000/static/signature.png"
    }


    pdf_bytes = generate_pdf(data)

    return StreamingResponse(
        BytesIO(pdf_bytes),
        media_type="application/pdf",
        headers={"Content-Disposition": "attachment; filename=purchase_order.pdf"}
    )

