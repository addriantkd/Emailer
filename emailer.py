import smtplib
import imaplib
import email
from config import INBOX_FILE, username, password, my_name
from templates import Template
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

SMTP_host = 'smtp.mail.yahoo.com'
IMAP_host = 'imap.mail.yahoo.com'

class Emailer:
    subject= "Weeding invitation"
    from_email = f"{my_name} <{username}>"
    
    def init(self, subject):
        self.subject = subject
        
    def read_email(self, subject):
        with imaplib.IMAP4_SSL(IMAP_host) as mail:
            mail.login(username, password)
            mail.select('INBOX')
            _, search_data = mail.search(None, f'(SUBJECT "{subject}")')
            my_messages = []
            for num in search_data[0].split():
                _, data = mail.fetch(num, '(RFC822)')
                _, data_bytes = data[0]
                email_message = email.message_from_bytes(data_bytes)
                for part in email_message.walk():
                    if part.get_content_type() == "text/plain":
                        body = part.get_payload(decode=True)
                        my_messages.append(body.decode())
        with open(INBOX_FILE, 'w') as file:
            file.write(my_messages[0])
        print(f"Email seen and stored in {INBOX_FILE}")
                 
    def format_email(self, template_path, subject, to_email, name):
        invitation = Template(template_path=template_path, subject=subject )
        msg = MIMEMultipart('alternative')
        msg['From'] = self.from_email
        msg['To'] = to_email
        msg['Subject'] = invitation.subject

        txt_part = MIMEText(invitation.get_template(name=name), 'plain')
        msg.attach(txt_part)
        return msg.as_string()
        
    def send_email(self, file_path, to_emails={}):
        with smtplib.SMTP(host=SMTP_host, port= 587) as mail:
            mail.ehlo()
            mail.starttls()
            try:
                mail.login(username, password)
            except smtplib.SMTPAuthenticationError:
                print("Login failed")
            for name, to_email in to_emails.items():
                email_msj = self.format_email(template_path=file_path, subject=self.subject, to_email=to_email, name=name)
                try:
                    mail.sendmail(from_addr=self.from_email, to_addrs=to_email, msg=email_msj)
                    print(f"Invitation sent to {name}")
                except:
                    print("Mail sending failed")   
        
    

