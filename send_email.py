import ssl
import smtplib
from email.message import EmailMessage
from openpyxl import load_workbook
import time

# Get Receiver data from the excel file
workbook = load_workbook("Email_Data.xlsx")
receiver_sheet = workbook["Receiver Info"]
receiver_rows = receiver_sheet.rows
receiver_headers = [cell.value for cell in next(receiver_rows)]
receiver_data = []

for row in receiver_rows:
    data = {}
    for title, cell in zip(receiver_headers, row):
        data[title] = cell.value
    receiver_data.append(data)

# Get Sender data from the excel file
sender_sheet = workbook["Sender Info"]
sender_rows = sender_sheet.rows
sender_headers = [cell.value for cell in next(sender_rows)]
sender_data = []

for row in sender_rows:
    data = {}
    for title, cell in zip(sender_headers, row):
        data[title] = cell.value
    sender_data.append(data)

# Send emails
for data in receiver_data:
    # Define email data
    email_sender = sender_data[0]["Sender Email"]
    email_password = sender_data[0]["Email Password"]
    email_receiver = data["Receiver Email"]
    subject = data["Email Subject"]
    body = data["Email body"]

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    em.add_alternative(body, subtype='html') # Make the message multipart
    context = ssl.create_default_context()  # Add SSL (layer of security)

    # Log in and send the email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        print("Login Success!")
        smtp.sendmail(email_sender, email_receiver, em.as_string())
        print("Email Sent!")
        smtp.quit()
        time.sleep(900)  #5=5 seconds / 900=15 mins

print("All Emails Sent!")





# ------------------------------------
# # Attach the image file

# from email.mime.base import MIMEBase
# from email import encoders

# with open('whaleshark.png', 'rb') as attachment_file:
#     file_data = attachment_file.read()
#     file_name = attachment_file.name.split("/")[-1]

# attachment = MIMEBase('application', 'octet-stream')
# attachment.set_payload(file_data)
# encoders.encode_base64(attachment)
# attachment.add_header('Content-Disposition', f'attachment; filename="{file_name}"')
# em.attach(attachment)