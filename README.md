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
from firebmail.firebmail import sendmail

# Set environment variables for your email credentials
os.environ['SENDER'] = 'your_email@gmail.com'
os.environ['PASSWORD'] = 'your_app_password'

# Example usage
payload = "Hello, this is a test email!"
recipient = "recipient_email@example.com"
subject = "Test Email"

sendmail(payload, recipient, subject)
```

## Function Parameters
The sendmail function has the following parameters:

payload: The string containing the message, either in plain text or HTML format.
recipient: The email address of the recipient.
subject: The email subject (default is "Message from firemail").
sender: Your email address (default is taken from the environment variable 'SENDER').
password: Your app password (default is taken from the environment variable 'PASSWORD').
type: The type of payload, either 'plain' or 'html' (default is 'plain').
filepath: The path of the email attachment, default is None.
client: The name of the client (default is 'smtp.gmail.com'). Attempts to use unrelated mail services may result in failure

## Example with attachment
```python
import os
from firemail import sendmail

# Set environment variables for your email credentials
os.environ['SENDER'] = 'your_email@gmail.com'
os.environ['PASSWORD'] = 'your_app_password'

# Example usage with attachment
payload = "Hello, this email includes an attachment."
recipient = "recipient_email@example.com"
subject = "Email with Attachment"
filepath = "path/to/your/file.pdf"

sendmail(payload, recipient, subject, filepath=filepath)
```

## Note
Make sure to use this module responsibly and adhere to the email sending policies of your email service provider. Additionally, consider using application-specific passwords for enhanced security.

For Gmail users, you can generate an app password by following the instructions <a href="https://support.google.com/accounts/answer/185833?hl=en">here</a>.

## License
This project is licensed under the MIT License - see the LICENSE.md file for details.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Issues
If you encounter any issues, feel free to open an issue in the repository.
