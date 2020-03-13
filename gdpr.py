import smtplib, ssl
import json

#OPEN JSON FILES
with open("languages.json", 'r', encoding='utf-8') as f:
    languages = json.load(f)
with open("config.json", 'r') as c:
    config = json.load(c)

#GET USER CREDENTIALS
semail = config['user_credentials']['sender_email']
spassword = config['user_credentials']['sender_password']

#GET USER INFORMATION
uname = config['user_information']['user_name']
uphone = config['user_information']['user_phone']
uemail = config['user_information']['user_email']
mail_language = config['misc']['language']

print("Welcome to gdprhelper, to start do you want to:\n1. Request access to your data\n2. Request data erasure")
template = input("Please choose either 1 or 2: ")

#FIND RECIPIENT
receiver = input("What site do you want to send a GDPR letter to?: ").lower()
if receiver in config['email_list']:
    recipient = config['email_list'][receiver]
    print("Success! " + receiver + " will be emailed.")
else:
    print("Did not find an email for that company in config.json")
    recipient = input("Email of company to mail: ")

#FIND SMTP SERVER
serverpicker = input("What is the email service you use?: ")
if serverpicker in config['provider_list']:
    smtp_server = config['provider_list'][serverpicker]
    print("Succes! " + serverpicker + "'s server has been found")
else:
    print("Did not find an SMTP server for that provider in config.json")
    smtp_server = input("SMTP Server of your email provider: ")

#GMAIL SEND FUNCTION
def send_mail():
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, 587) as server:
        server.starttls(context=context)
        server.login(semail, spassword)
        server.sendmail(semail, recipient, message)
        print("Email has been sent!")

#GETTING MAIL PRESET + MAIL SERVER
if mail_language == mail_language:
    message = languages[mail_language][template] + "\n" + uname + "\n" + uphone + "\n" + uemail

send_mail()