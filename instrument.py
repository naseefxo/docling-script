from pathlib import Path
import os
import json
from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import (
    PdfPipelineOptions,
    TesseractCliOcrOptions
)
from docling.document_converter import DocumentConverter, PdfFormatOption

# === Prepare output directories ===
os.makedirs("extracted_data", exist_ok=True)
os.makedirs("extracted_data/pictures", exist_ok=True)

# === Setup pipeline options ===
ocr_options = TesseractCliOcrOptions(force_full_page_ocr=True)

pipeline_options = PdfPipelineOptions(
    do_ocr=True,
    do_table_structure=True,
    do_detect_figures=True,
    generate_images=True,
    generate_picture_images=True,
    ocr_languages=["eng", "hin"],
    ocr_options=ocr_options,
    chunking_mode="advanced"  #  This enables hierarchical chunking
)

# === Create the document converter ===
doc_converter = DocumentConverter(
    format_options={InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options)}
)

# === Convert the PDF ===
input_pdf_path = Path("OCR Scope of Work.pdf")  # Replace with your file
result = doc_converter.convert(input_pdf_path)
doc = result.document

# === Export Markdown Summary ===
try:
    markdown_text = doc.export_to_markdown()
    with open("extracted_data/summary.md", "w", encoding="utf-8") as f:
        f.write(markdown_text)
    print(" Markdown summary saved to extracted_data/summary.md")
except Exception as e:
    print(" Markdown export failed:", e)

# === Export extracted images ===
for idx, picture in enumerate(doc.pictures):
    image = picture.get_image(doc)
    if image:
        img_path = f"extracted_data/pictures/picture_{idx}.png"
        image.save(img_path)
    else:
        print(f" Picture {idx} has no image data.")



# ===  Multimodal JSON Export (Docling's built-in) ===
try:
    multimodal_dict = doc.export_to_dict()
    with open("extracted_data/multimodal.json", "w", encoding="utf-8") as f:
        json.dump(multimodal_dict, f, indent=2, ensure_ascii=False)
    print(" Multimodal JSON saved to extracted_data/multimodal.json")
except Exception as e:
    print(" Multimodal export failed:", e)
