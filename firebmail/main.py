import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


ctx = ssl.create_default_context()
default_subject = "Message from firemail"


def sendmail(payload: str, 
             recipient:str,  
             sender:str, 
             password:str, 
             subject:str = default_subject,
             type='plain', 
             filepath = None, 
             client='smtp.gmail.com'):
    """
        >>> payload:    is the string containing the message, either in plain text or html format
        >>> recipient:  is the email address of the reciever
        >>> Sender:     is your email address
        >>> Password:   is your app password
        >>> subject:    is the email subject
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