# 📘 Purchase Order PDF Generator using FastAPI & Playwright

## 📌 Project Overview

This project is a **dynamic Purchase Order (PO) PDF generation system** that allows users to enter purchase details via a web form and instantly download a **professionally formatted A4 PDF**.

The system automatically:
- Calculates totals and taxes
- Converts amounts into words (Indian format)
- Adjusts layout for variable data (items, addresses, terms)
- Embeds company logo and authorized signature

The goal of this project is to demonstrate how **HTML templates + backend rendering + headless browsers** can be combined to generate **print-ready business PDFs**.

---

## 🎯 Objectives

- Generate purchase order PDFs dynamically
- Maintain a fixed professional layout
- Auto-adjust PDF height for variable content
- Prevent page cut issues
- Keep frontend simple and lightweight
- Produce print-ready A4 PDFs
- Separate business logic from presentation

---

## 🧠 High-Level Workflow

1. User fills Purchase Order form (HTML)
2. Frontend sends JSON payload to FastAPI
3. Backend validates data using Pydantic
4. Totals and GST are calculated
5. Data is injected into Jinja2 HTML template
6. Playwright renders HTML using Chromium
7. PDF is generated in A4 format
8. PDF is streamed back to the browser for download

---

## 🛠️ Technologies Used and Why

### Python
- Core backend language
- Clean ecosystem for APIs and PDF generation

---

### FastAPI
Used for:
- API creation
- Request validation
- Streaming PDF responses

Chosen for:
- High performance
- Automatic data validation
- Clean architecture

---

### Jinja2
- HTML templating engine
- Injects dynamic data into PDF layout
- Keeps design and logic separate

---

### Playwright (Chromium)
- Renders HTML to PDF
- Ensures pixel-perfect output
- Handles page breaks and print styles

Why Playwright?
- Accurate CSS support
- Better PDF rendering than traditional libraries

---

### Pydantic
- Validates incoming request data
- Ensures correct data types
- Prevents malformed payloads

---

### num2words
- Converts numeric amounts into words
- Uses Indian numbering system (`en_IN`)

---

### Plain HTML + JavaScript
- Lightweight frontend
- No framework dependency
- Easy to deploy and maintain

---

## 📂 Project Structure


purchase-order-pdf/
│
├── backend/
│   ├── main.py
│   ├── pdf_generator.py
│   ├── schemas.py
│   ├── utils.py
│   └── templates/
│       └── purchase_order.html
│
├── frontend/
│   └── index.html
│
├── static/
│   ├── logo.png
│   └── signature.png
│
├── requirements.txt
└── README.md


---

## 📄 Purchase Order Template Features

- Fixed header with company details
- Bill From / Bill To / Ship To layout
- Dynamic item table
- Automatic totals & GST calculation
- Amount in words
- Terms & Conditions section
- Signature fixed to bottom-right
- Fully print-compatible layout

---

---

## ▶️ How to Run the Project


Follow the steps below to execute the project successfully.


---


### Step 1: Create a Virtual Environment

Create a Python virtual environment named `lib`:

```bash
python -m venv lib
```

---

### Step 2: Activate the Virtual Environment

For **Windows**:

```bash
lib\Scripts\activate
```

For **Linux / macOS**:

```bash
source lib/bin/activate
```

---

### Step 3: Install Required Dependencies

Install all project dependencies listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

---

### Step 4: Install Playwright Browser

Install Chromium required for PDF generation:

```bash
playwright install chromium
```

---


### Step 5: Run the Application

Start the Purchase Order PDF Generator by running:

```bash
uvicorn backend.main:app --reload
```


