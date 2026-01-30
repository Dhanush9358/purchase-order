from num2words import num2words
from datetime import datetime

def generate_order_no():
    today = datetime.now()
    return f"OMC-PO-{today.strftime('%d%m%y%H%M%S')}"

def calculate_totals(items):
    sub_total = 0
    gst_total = 0
    total_qty = 0

    for item in items:
        item.amount = item.qty * item.rate
        sub_total += item.amount
        gst_total += item.amount * (item.gst / 100)
        total_qty += item.qty

    grand_total = round(sub_total + gst_total, 2)

    return {
        "order_no": generate_order_no(),
        "total_qty": total_qty,
        "sub_total": round(sub_total, 2),
        "taxable": round(sub_total, 2),
        "gst_total": round(gst_total, 2),
        "grand_total": grand_total,
        "total_gst_words": num2words(gst_total, lang="en_IN").title() + " Only",
        "bill_amount_words": num2words(grand_total, lang="en_IN").title() + " Only"
    }
