#!/usr/bin/env python3

import requests
import os 
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(attachment, title, paragraph):
  report = SimpleDocTemplate("/tmp/processed.pdf")
  styles = getSampleStyleSheet()
  report_title = Paragraph(title, styles["h1"])
  report_body = Paragraph(paragraph)
  report.build([report_title, report_body])
  print("GERADO")
