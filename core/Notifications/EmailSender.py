import smtplib
from fastapi import HTTPException
from config import settings


class EmailSender():
    def __init__(self):
        self.smtpClient = smtplib.SMTP('smtp.mail.ru', 587)
        self.email = settings.EMAIL_LOGIN()
        smtpObj.starttls()
        smtpObj.login(self.email, settings.EMAIL_PASSWORD)

    def SendEmail(self, targetMail: str, text: str):
        try:
            self.smtpClient.sendmail(self.email, targetMail, text)
        except e:
            raise HTTPException(400, e)