import pandas as pd
from datetime import datetime, timedelta
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

def sendMail():
    mail_content = pd.read_csv('mail_content.csv')
    today_mail_text = mail_content.loc[mail_content['date'] == datetime.today().strftime('%Y-%m-%d')]
    today_mail_text.reset_index(drop=True, inplace=True)

    sender_address = 'SENDER@gmail.com'
    sender_pass = 'SENDER_PASS'
    receiver_address = 'RECIVER@yahoo.com'

    message =  MIMEMultipart('alternative')
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'Otodom - ' + datetime.today().strftime('%Y-%m-%d')

    text = MIMEText(str(today_mail_text['text'][0]), 'html')
    message.attach(text)

    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print('Mail Sent - ' + current_time)
