import smtplib
from email.mime.text import MIMEText

class SendEmail():
    def __init__(self ):
        pass

    def send_email(self, subject,text,recipient):
        MESSAGE = MIMEText(text, 'plain')
        MESSAGE['subject'] = subject
        MESSAGE['To'] = recipient
        MESSAGE['From'] = str(input("Enter gmail account id ? "))  #enter gmail account id
        server = smtplib.SMTP('smtp.gmail.com', 587)
        password = str(input("Password? "))  #enter user account password
        server.starttls()
        server.login(MESSAGE["FROM"], password)
        server.sendmail(MESSAGE["FROM"], recipient, MESSAGE.as_string())
        server.quit()
        print('Email sent!')

s1 = SendEmail()
subject = str(input("Subject? "))
body = str(input("Body? "))
recipient = str(input("Recipient? "))
s1.send_email(subject,body,recipient)
