#!/usr/bin/env python
# coding: utf-8

# In[1]:

import json
import pandas as pd
import os
import smtplib
import mimetypes
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.message import Message
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.text import MIMEText

def sendMail(email_data):
    email_data = pd.read_json(r'C:/emailreport/'+email_data)
    emailfrom = email_data['emails']['senderEmail']
    emailto = email_data['emails']['receiverEmails']
    fileToSend = email_data['emails']['reports']['reportList']
    username = email_data['emails']['senderEmail']
    password = email_data['emails']['senderPW']
    for elem in fileToSend:
        msg = MIMEMultipart()
        msg["From"] = emailfrom
        msg["To"] = ", ".join(emailto)
        msg["Subject"] = elem
        elem = os.path.join("C:/emailreport/data/", elem)
        ctype, encoding = mimetypes.guess_type(elem)
        if ctype is None or encoding is not None:
            ctype = "application/octet-stream"

        maintype, subtype = ctype.split("/", 1)

        if maintype == "text":
            fp = open(elem)
            # Note: we should handle calculating the charset
            attachment = MIMEText(fp.read(), _subtype=subtype)
            fp.close()
        elif maintype == "image":
            fp = open(elem, "rb")
            attachment = MIMEImage(fp.read(), _subtype=subtype)
            fp.close()
        elif maintype == "audio":
            fp = open(elem, "rb")
            attachment = MIMEAudio(fp.read(), _subtype=subtype)
            fp.close()
        else:
            fp = open(elem, "rb")
            attachment = MIMEBase(maintype, subtype)
            attachment.set_payload(fp.read())
            fp.close()
            encoders.encode_base64(attachment)
        attachment.add_header("Content-Disposition", "attachment", filename=msg["Subject"])
        msg.attach(attachment)

        server = smtplib.SMTP("smtp.office365.com:587")
        server.starttls()
        server.login(username,password)
        server.sendmail(emailfrom, emailto, msg.as_string())
        server.quit()

