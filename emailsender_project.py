from email.message import EmailMessage
import ssl
import smtplib
import os

Email_sender= input("Enter your Email-ID :")
os.environ['PASSWORD'] = input("Enter your Email Password:")
email_receiver = input('enter email-ID of receiver :')
subject = "MY python project (sai kiran yadagini)"
body = """ This is my python project ----- thanks for checking"""

em = EmailMessage()
em['from'] = Email_sender
em['to'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(Email_sender, os.environ['PASSWORD'])
    smtp.sendmail(Email_sender, email_receiver, em.as_string())