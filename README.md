# firemail

`firemail` is a simple Python module for sending emails using the SMTP protocol. It allows you to send plain text or HTML emails and optionally attach files. The module is designed to work with Gmail by default but can be configured for other SMTP servers as well.

## Installation

To use `firemail`, you can install it via pip:

```bash
pip install firemail

```

## Usage
```python
import os
from firebmail import sendmail


# Example usage
sender = "yourmail@example.com"
password = "your_app_password"
payload = "Hello, this is a test email!"
recipient = "recipient_email@example.com"
subject = "Test Email"

sendmail(payload, recipient, sender,password, subject)
```

## Function Parameters
The sendmail function has the following parameters:

payload: The string containing the message, either in plain text or HTML format.
recipient: The email address of the recipient.
sender: Your email address 
password: Your app password 
subject: The email subject (default is "Message from firemail").
type_: The type of payload, either 'plain' or 'html' (default is 'plain').
filepath: The path of the email attachment, default is None.
client: The name of the client (default is 'smtp.gmail.com'). Attempts to use unrelated mail services may result in failure

## Example with attachment
```python
import os
from firebmail.firebmail import sendmail



# Example usage with attachment
sender = "yourmail@example.com"
password = "your_app_password"
payload = "Hello, this email includes an attachment."
recipient = "recipient_email@example.com"
subject = "Email with Attachment"
filepath = "path/to/your/file.pdf"

sendmail(payload, recipient,sender, password, subject, filepath=filepath)
```

## Sending Batch Mail

Using the `sendmail` function in a loop to send multiple emails can be inefficient, because it authenticates each time; instead use the BatchMail class to send multiple emails efficiently.

```python
from firebmail import BatchMail

sender = "mymail@example.com"
password = "my app password"

payload = "Hello, this is a test email!"
subject = "Test Email"

batch = BatchMail(sender = sender, password = password, subject=subject, payload=payload)
batch.send_batch(['test1@gmail.com', 'test2@gmail.com', 'test3@gmail.com'])
```


## Note
Make sure to use this module responsibly and adhere to the email sending policies of your email service provider. Additionally, consider using application-specific passwords for enhanced security.

For Gmail users, you can generate an app password by following the instructions <a href="https://support.google.com/accounts/answer/185833?hl=en">here</a>.

## License
This project is licensed under the MIT License - see the LICENSE.md file for details.

## Contributing
Pull requests are welcome. For major changes, please open an issdriveue first to discuss what you would like to change.

## Issues
If you encounter any issues, feel free to open an issue in the repository.
