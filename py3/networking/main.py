import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP('smtp.gmail.com', 25)

# start the process
server.ehlo()

# you should not do this
# server.login('mail@mail.com',  'password123')


# save the email and the password encrypted in a file
with open('password.txt', 'r') as f:
    password = f.read()

server.login('aridonk16@gmail.com', password)
msg = MIMEMultipart()
msg['From'] = 'Aridon'
msg['To'] = 'aridon.krasniqi1@student.uni-pr.edu'
msg['Subject'] = 'Just A Test'
with open('message.txt', 'r') as f:
    message = f.read()

msg.attach(MIMEText(message , 'plain'))