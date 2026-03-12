import smtplib
from email.message import EmailMessage

msg = EmailMessage()
msg['Subject'] = 'Pi Digit Calculation - Position 1'
msg['To'] = 'brandonmwebb@gmail.com'
msg.set_content('The next digit of pi at position 1 is: 3\n\nCalculated on: 2026-03-12')

print("Email prepared. Configure SMTP settings to send.")
print(f"To: {msg['To']}")
print(f"Subject: {msg['Subject']}")
print(f"Body:\n{msg.get_content()}")
