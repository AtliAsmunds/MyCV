import smtplib, ssl, dotenv, os
from email.message import EmailMessage

dotenv.load_dotenv()

SERVER = "smtp.gmail.com"
PORT = 465
SENDER = os.getenv('GMAIL_USER')
PASSWORD = os.getenv('GMAIL_PASS')
RECEIVER = os.getenv('GMAIL_END')

def send_email(name: str, reason: str, message: str, receiver=RECEIVER):

    msg = EmailMessage()
    msg.set_content(message)
    msg['Subject'] = f"{name} || {reason}"
    msg['From'] = SENDER
    msg['To'] = receiver

    context = ssl.create_default_context()


    try:
        with smtplib.SMTP_SSL(SERVER, PORT, context=context) as server:
            server.login(SENDER, PASSWORD)
            server.send_message(msg)
            return True
    except Exception as e:
        return False
