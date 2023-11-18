#!/usr/bin/env python3

from email.message import EmailMessage
import os
import smtplib

sender = "automation@example.com"
recipient = "student-02-7e2a3189f672@example.com"
subject = "Upload Completed - Online Fruit Store"
body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
body_error = "Please check your system and resolve the issue as soon as possible."
message = EmailMessage()
def generate_email(attachment):
  message["Subject"] = subject
  message["From"] = sender
  message["To"] = recipient
  message.set_content(body)
  with open(attachment, "rb") as ap:
    message.add_attachment(ap.read(),
                            maintype="application",
                            subtype="pdf",
                            filename=os.path.basename(attachment))


def send_email(attachment):
  mail_server = smtplib.SMTP('localhost')
  generate_email(attachment)
  mail_server.send_message(message)
  mail_server.quit()

def send_email_error(error):
  message["Subject"] = error
  message["From"] = sender
  message["To"] = recipient
  message.set_content(body_error)
  mail_server = smtplib.SMTP('localhost')
  mail_server.send_message(message)
  mail_server.quit()
