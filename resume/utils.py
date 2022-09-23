import smtplib, ssl, dotenv, os
from email.message import EmailMessage

dotenv.load_dotenv()

SERVER = "smtp.gmail.com"
PORT = 465
SENDER = os.getenv('GMAIL_USER')
PASSWORD = os.getenv('GMAIL_PASS')
RECEIVER = os.getenv('GMAIL_END')

def send_email(name: str, email: str, message: str):

    msg = EmailMessage()
    msg.set_content(message)
    msg['Subject'] = f"{name} || {email}"
    msg['From'] = SENDER
    msg['To'] = RECEIVER

    context = ssl.create_default_context()


    try:
        with smtplib.SMTP_SSL(SERVER, PORT, context=context) as server:
            server.login(SENDER, PASSWORD)
            server.send_message(msg)
            return True
    except Exception as e:
        return False
