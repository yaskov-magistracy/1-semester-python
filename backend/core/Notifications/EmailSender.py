import smtplib
from fastapi import HTTPException
from config import settings
from smtplib import SMTP
import datetime
from tasks import SendMailTask



class EmailSender():
    async def SendEmail(self, targetMail: str, text: str, targetDateTime: datetime):
        currentTime = datetime.datetime.now(datetime.timezone.utc)
        delay = int((targetDateTime - currentTime).total_seconds() * 1000)
        print (delay)
        if (delay < 0):
            raise HTTPException(400, "Время только в будущем")
        
        try:
            self.SendWithoutDramatiq(targetMail, text)
        except Exception as e:
            raise HTTPException(e)
        #SendMailTask.send_with_options(args=(targetMail, text), delay=delay)
        #send_with_options(args=(targetMail, text), delay=delay)

    def SendWithoutDramatiq(self, targetMail: str, text: str):
        smtpClient = smtplib.SMTP('smtp.mail.ru', 587)
        email = settings.EMAIL_LOGIN()
        smtpClient.starttls()
        smtpClient.login(email, settings.EMAIL_PASSWORD())
        smtpClient.sendmail(email, targetMail, text)
        smtpClient.close()


