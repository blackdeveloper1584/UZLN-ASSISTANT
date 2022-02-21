from email.mime.base import MIMEBase
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from email import encoders
import time
import sys
sys.path.append('.')

try:
    from src.All_Functions.Send_Message.GUI import Design
    from src.System.main import Voice

except Exception:
    print('Помилка!')


class Email:

    def __init__(self):
        self.voice=Voice()
        self.design=Design()
    

    def send_text_message(self):

        self.design.text_message()

        try:
            msg=MIMEMultipart()
            msg['From']=self.design.email_from
            msg['To']=self.design.email_to
            msg['Subject']=self.design.subject
            message=self.design.message_1
            msg.attach(MIMEText(message,"plain"))
            server=smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            time.sleep(0.2)
            server.login(self.design.email_from,self.design.password)
            text=msg.as_string()
            server.sendmail(self.design.email_from,self.design.email_to,text)
            server.quit()
            time.sleep(0.2)
        
        except Exception:
            self.voice.say_message('Error!')
    

    def send_file(self):

        self.design.file_message()

        try:
            filepath =self.design.path_to_file
            basename = os.path.basename(filepath)
            # filesize = os.path.getsize(filepath)
            msg = MIMEMultipart()
            msg['Subject'] =self.design.subject
            msg['From'] =self.design.email_from
            msg['To'] =self.design.email_to
            part_file = MIMEBase("application", f"octet-stream; name={basename}")
            part_file.set_payload(open(filepath, "rb").read())
            encoders.encode_base64(part_file)
            msg.attach(part_file)
            mail = smtplib.SMTP_SSL('smtp.gmail.com')
            time.sleep(0.2)
            mail.login(self.design.email_from,self.design.password)
            mail.sendmail(self.design.email_from,self.design.email_to,msg.as_string())
            mail.quit()
            time.sleep(0.2)
        
        except Exception:
            self.voice.say_message('Error!')