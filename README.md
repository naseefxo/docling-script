#  Docling PDF Multimodal Extractor

This Python script uses [Docling](https://docling-project.github.io/docling/) to convert a PDF document into:
- Markdown summary
- Extracted images (figures, logos, signatures, etc.)
- A rich, structured JSON output (`multimodal.json`)

##  Features
-Document Structure Extraction                                                                                          Two-Column Layout Detection                                                                                            Table Detection                                                                                                                    Multilingual OCR                                                                                                                   Signature Block Detection                                                                                                 Images Exported

## 🧰 Requirements

Install dependencies with:

```bash
pip install -r requirements.txt
You will also need Tesseract installed on your system. On Linux:
sudo apt install tesseract-ocr
usage:
Place your target PDF file in the same directory (e.g., OCR Scope of Work.pdf) and run: python script.py
This generates:

    extracted_data/summary.md — Markdown summary

    extracted_data/pictures/ — Extracted and saved images

    extracted_data/multimodal.json — Final JSON with full structure


