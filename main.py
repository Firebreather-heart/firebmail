import smtplib
import ssl,os,dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from dotenv import load_dotenv
from pathlib import Path 

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

BASE_DIR = Path(__file__).resolve().parent
dotenv_file = os.path.join(BASE_DIR,'.env')

if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)

SENDER = str(os.getenv('SENDER'))
PASSWORD = str(os.getenv('PASSWORD'))

ctx = ssl.create_default_context()
default_subject = "Message from firemail"


def sendmail(payload: str, recipient:str, subject:str = default_subject, sender:str =SENDER, password:str = PASSWORD, type='plain', filepath:str=None, client='smtp.gmail.com'):
    """
        >>> payload:    is the string containing the message, either in plain text or html format
        >>> recipient:  is the email address of the reciever
        >>> subject:    is the email subject
        >>> Sender:     is your email address, default is my email address(lordfirebcorps@gmail.com) 
        >>> Password:   is your app password, default is likewise my password
        >>> filepath:   is the path of the email attachment, defaults to None
        >>> client:     is the name of the client, defaults to 'smtp.gmail.com', any attempt to use unrelated mail services will result in failure.

    """
    message = MIMEMultipart("alternative")
    message['From'] = sender 
    message['To'] = recipient
    message['Subject'] = subject

    if type == 'plain':
        message.attach(MIMEText(payload, "plain"))
    else:
        message.attach(MIMEText(payload, "html"))

    if filepath is not None:
        filename = filepath
        with open(filename, "rb") as f:
            file = MIMEApplication(f.read())
            disposition = f"attachment; filename={filename}"
            file.add_header("Content-Disposition", disposition)
            message.attach(file)

    with smtplib.SMTP_SSL(client, port=465, context=ctx) as server:
        server.login(sender, password)
        server.sendmail(sender, recipient, message.as_string())
    print('Check mail for success!')