# -*- coding: utf-8 -*-
import io
from wand.image import Image
from wand.color import Color
from PyPDF2 import PdfFileReader, PdfFileWriter


def convert(filename, page=0, res=120):
    reader = PdfFileReader(filename, strict=False)
    page_obj = reader.getPage(page)
    dst_pdf = PdfFileWriter()
    dst_pdf.addPage(page_obj)

    pdf_bytes = io.BytesIO()
    dst_pdf.write(pdf_bytes)
    pdf_bytes.seek(0)

    img = Image(file=pdf_bytes, resolution=res)
    img.format = 'png'
    img.compression_quality = 90
    img.background_color = Color('white')
    img_path = filename.replace('pdf', 'png')
    img.save(filename=img_path)
    img.destroy()
