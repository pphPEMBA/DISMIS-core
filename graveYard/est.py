#!/usr/bin/python
import smtplib
def apple():
    message = """From: From Person <from@fromdomain.com>
    To: To Person <to@todomain.com>
    MIME-Version: 1.0
    Content-type: text/html
    Subject: SMTP HTML e-mail test
    This is an e-mail message to be sent in HTML format
    <b>This is HTML message.</b>
    <h1>This is headline.</h1>
    """
    try:
        smtpObj = smtplib.SMTP('localhost')
        smtpObj.sendmail(sender, receivers, message)
    except:
        print( "Error: unable to send email")


# import all necessary components
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

port = 587
smtp_server = "smtp.gmail.com"
login = "pembamoktan.t@gmail.com"
password = "D1i1s1m1i1s@" # paste your password generated by Mailtrap

sender_email = "pembamoktan.t@gmail.com"
receiver_email = "pembatamang.m@gmail.com"
message = MIMEMultipart("alternative")
message["Subject"] = "CID image test"
message["From"] = sender_email
message["To"] = receiver_email

# write the HTML part
html = """\
<html>
 <body>
   <img src="cid:Mailtrapimage">
 </body>
</html>
"""

part = MIMEText(html, "html")
message.attach(part)

# We assume that the image file is in the same directory that you run your Python script from
fp = open('/home/pemba/d1_SuperDismis/Dismis-HA_GUI/test.jpg', 'rb')
image = MIMEImage(fp.read())
fp.close()

# Specify the  ID according to the img src in the HTML part
image.add_header('Content-ID', '<Mailtrapimage>')
message.attach(image)

# send your email
with smtplib.SMTP('smtp.gmail.com', 587) as server:
   server.login(login, password)
   server.sendmail(
       sender_email, receiver_email, message.as_string())
print('Sent')

