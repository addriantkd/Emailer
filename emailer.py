import os
import smtplib
import imaplib
import email
from templates import Template
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

SMTP_host = 'smtp.mail.yahoo.com'
# IMAP_host = 'imap.mail.yahoo.com'

username = os.environ.get('EMAIL')
password = os.environ.get('PASSWORD')

class Emailer:
    from_email = username
    to_emails = []
    email_msg = ""
    
    def init(self, to_emails):
        self.to_emails = to_emails
        
          
    def format_email(self):
        mail = Template()
        msg = MIMEMultipart('alternative')
        msg['From'] = self.from_email
        msg['To'] = to_email
        msg['Subject'] = mail.subject

        txt_part = MIMEText(mail.context, 'plain')
        msg.attach(txt_part)

        self.email_msg = msg.as_string()
        
    def send_email(self):
        with smtplib.SMTP(host=SMTP_host, port= 587) as mail:
            mail.ehlo()
            mail.starttls()
            try:
                mail.login(username, password)
            except smtplib.SMTPAuthenticationError:
                print("Login failed")
            try:
                mail.sendmail(from_addr=None, to_addrs=None, msg= None)
                print("Mail sent")
            except:
                print("Mail sending failed")   
        
    # def read_mail(self):
    #     with imaplib.IMAP4_SSL(IMAP_host) as mail:
    #         mail.login(username, password)
    #         mail.select('inbox')
            
    #         _, search_data = mail.search(None, 'UNSEEN')
    #         my_messages = []
    #         for num in search_data[0].split():
    #             email_data ={}
    #             # print(num)
    #             _, data = mail.fetch(num, '(RFC882)')
    #             # print(data[0])
    #             _, b = data[0]
    #             email_message = email.message_from_bytes(b)
    #             # print(email_message)
    #             for header in ['subject', 'to', 'from', 'date']:
    #                 print("{}: {}".format(header, email_message[header]))
    #                 email_data[header] = email_message[header]
    #             for part in email_message.walk():
    #                 if part.get_content_type == "text/plain":
    #                     body = part.get_payload(decode=True)
    #                     print(body.decode())
    #                     email_data[body] = body.decode()
    #                 elif part.get_content_type == "text/html":
    #                     html_body = part.get_payload(decode=True)
    #                     print(html_body.decode())
    #                     email_data[html_body] = html_body.decode()
    #                 my_messages.append(email_data)
    #     return my_messages    
                
    

