import smtplib
from fastapi import HTTPException
from config import settings
from smtplib import SMTP
import datetime
import dramatiq


class EmailSender():
    smptClient: SMTP
    email: str

    def __init__(self):
        self.smtpClient = smtplib.SMTP('smtp.mail.ru', 587)
        self.email = settings.EMAIL_LOGIN()
        self.smtpClient.starttls()
        self.smtpClient.login(self.email, settings.EMAIL_PASSWORD())

    def SendEmail(self, targetMail: str, text: str, targetDateTime: datetime):
        currentTime = datetime.now()
        delay = int((targetDateTime - currentTime).total_seconds() * 1000)
        self.SendMailTask.send_with_options(args=(targetMail, text), delay=delay)

    @dramatiq.actor
    def SendMailTask(self, targetMail: str, text: str):
        try:
            self.smtpClient.sendmail(self.email, targetMail, text)
        except Exception as e:
            raise HTTPException(400, e)