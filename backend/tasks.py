import dramatiq
import smtplib
from fastapi import HTTPException
from config import settings
from smtplib import SMTP

@dramatiq.actor()
def SendMailTask(targetMail: str, text: str):
    print(f"task {targetMail}")
    try:
        smtpClient = smtplib.SMTP('smtp.mail.ru', 587)
        email = settings.EMAIL_LOGIN()
        smtpClient.starttls()
        smtpClient.login(email, settings.EMAIL_PASSWORD())
        smtpClient.sendmail(email, targetMail, text)
        smtpClient.close()
    except Exception as e:
        raise HTTPException(400, e)