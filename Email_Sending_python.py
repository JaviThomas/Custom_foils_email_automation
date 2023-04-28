import smtplib
import pandas as pd
import csv
import imghdr
from email.message import EmailMessage



# Your information here
EMAIL_ADDRESS = ('Youremail@yahoo.com')
EMAIL_PASSWORD = ('your3rdPartyPassword') # Note: This password is the 3rd party created password


f = open('Name_of_email_instruction_file.txt') #name of the email_list file

csv_f = csv.reader(f)

for row in csv_f :
    contacts = (row[:-1])
    file_location = (row[-1])

    msg = EmailMessage()
    msg['Subject'] = 'Invoice for your order from Custom Foils' # Subject Attached with Email
    msg['From'] = EMAIL_ADDRESS
    msg['To'] =  ', '.join(contacts)

    msg.set_content('Attached to this email is your invoice, thank you for your business!') # Message Attached with Email
    with open(file_location, 'rb') as f:
        file_data = f.read()
        file_name_list = f.name
        file_name = file_name_list.split("\\")
        file_name = file_name[-1]

    msg.add_attachment(file_data, maintype='application' , subtype='octet-stream', filename=file_name)

    with smtplib.SMTP_SSL('smtp.mail.yahoo.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)
    