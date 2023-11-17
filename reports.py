#!/usr/bin/env python3

import requests
import os 
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(attachment, title, paragraph):
  styles = getSampleStyleSheet() 
  report = SimpleDocTemplate(attachment)
  report_title = Paragraph(title, styles["h1"])
  report.build([report_title])
  print("GERADO")
