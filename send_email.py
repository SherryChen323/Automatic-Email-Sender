import ssl
import smtplib
from email.message import EmailMessage
import time
# from email.mime.base import MIMEBase
# from email import encoders

# Define email sender and receiver
email_sender = 'codingemail323@gmail.com'
email_password = 'uyol ztou qgjv hzsi'
email_receiver = 'sherrychen323@gmail.com'

# Set the subject and body of the email
subject = 'Test: Send Email with Python'
body = """
This email is a test email!
"""

em =EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

# Make the message multipart
em.add_alternative(body, subtype='html')

# # Attach the image file
# with open('whaleshark.png', 'rb') as attachment_file:
#     file_data = attachment_file.read()
#     file_name = attachment_file.name.split("/")[-1]

# attachment = MIMEBase('application', 'octet-stream')
# attachment.set_payload(file_data)
# encoders.encode_base64(attachment)
# attachment.add_header('Content-Disposition', f'attachment; filename="{file_name}"')
# em.attach(attachment)

# Add SSL (layer of security)
context = ssl.create_default_context()

# Log in and send the email
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
    time.sleep(15)  #15 seconds
    smtp.sendmail(email_sender, 'pohsuanchen323@gmail.com', em.as_string())

print("Email Sent!")