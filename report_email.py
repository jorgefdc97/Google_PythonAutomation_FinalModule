#!/usr/bin/env python3
import os
import datetime
import reports
import emails

path = "/home/student-02-7e2a3189f672/supplier-data/descriptions/"

paragraph ="<br/>"
attachment = "/tmp/processed.pdf"
title = "Processed Update on " + datetime.datetime.now().date().__str__()

for file in os.listdir(path):
  file_path = path + file
  with open(file_path, "r") as f:
    lines = f.readlines()
    paragraph = paragraph + "name: " + lines[0] + "<br/>weight: " + lines[1] + "<br/><br/>"

if __name__ == "__main__":
    reports.generate_report(attachment, title, paragraph)
    emails.send_email(attachment)
