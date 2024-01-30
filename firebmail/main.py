import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


ctx = ssl.create_default_context()
default_subject = "Message from firemail"

class BatchMail:
    def __init__(self, 
                sender:str, 
                password:str,
                payload: str, 
                subject:str = default_subject,
                type_:str='plain', 
                filepath = None, 
                client:str='smtp.gmail.com',
                port:int = 465
                 ):
        """
        Initializes a BatchMail object.

        Args:
            sender (str): The email address of the sender.
            password (str): The password of the sender's email account.
            payload (str): The content of the email.
            subject (str, optional): The subject of the email. Defaults to default_subject.
            type_ (str, optional): The type of the email content. Defaults to 'plain'.
            filepath (str, optional): The path to the file to be attached to the email. Defaults to None.
            client (str, optional): The SMTP server address. Defaults to 'smtp.gmail.com'.
            port (int, optional): The port number for the SMTP server. Defaults to 465.
        """
        self.sender = sender
        self.password = password
        self.payload = payload 
        self.subject = subject 
        self.type_ = type_
        self.filepath = filepath
        self.client = client 
        self.port = port
     
    
    def send_batch(self, batch:list):
        """
        Sends batch emails to a list of recipients.

        Args:
            batch (list): A list of email addresses of the recipients.
        """
        message = MIMEMultipart("alternative")
        message['From'] = self.sender 
        message['Subject'] = self.subject

        if self.type_ == 'plain':
            message.attach(MIMEText(self.payload, "plain"))
        else:
            message.attach(MIMEText(self.payload, "html"))

        if self.filepath is not None:
            filename = self.filepath
            with open(filename, "rb") as f:
                file = MIMEApplication(f.read())
                disposition = f"attachment; filename={filename}"
                file.add_header("Content-Disposition", disposition)
                message.attach(file)
        with smtplib.SMTP_SSL(self.client, self.port, context=ctx) as server:
            server.login(self.sender, self.password)
            for i in batch:
                del message['To']
                message['To'] = str(i)
                server.sendmail(self.sender, str(i), message.as_string())



def sendmail(payload: str, 
             recipient:str,  
             sender:str, 
             password:str, 
             subject:str = default_subject,
             type_:str='plain', 
             filepath = None, 
             client:str='smtp.gmail.com',
             port:int = 465):
    """
        >>> payload:    is the string containing the message, either in plain text or html format
        >>> recipient:  is the email address of the reciever
        >>> Sender:     is your email address
        >>> Password:   is your app password
        >>> subject:    is the email subject
        >>> type_:      tells if the content is html or plain text, defaults to plain
        >>> filepath:   is the path of the email attachment, defaults to None
        >>> client:     is the name of the client, defaults to 'smtp.gmail.com', any attempt to use unrelated mail services will result in failure.
        >>> port:       is the port number, defaults to 465

    """
    message = MIMEMultipart("alternative")
    message['From'] = sender 
    message['To'] = recipient
    message['Subject'] = subject

    if type_ == 'plain':
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

    with smtplib.SMTP_SSL(client, port, context=ctx) as server:
        server.login(sender, password)
        server.sendmail(sender, recipient, message.as_string())
    print('Check mail for success!')

