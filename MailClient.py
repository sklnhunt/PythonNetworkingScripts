import smtplib
from email import encoders, message
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP('smtp.gmail.com',465)
# SMTP server of provider

server.ehlo()

server.login('sender@email.com','Password')
#add your email and password here or use file and load the password from that file

msg = MIMEMultipart()
msg['From'] = 'Whoami'
msg['To'] = 'receiver@email.com'
msg['Subject'] = 'Just a script test'

with open('message.txt','r') as f:
    message = f.read()

msg.attach(MIMEText(message, 'plain'))

filename = 'Notapic.jpg'
attachment = open(filename,'rb')


# Because it is an image we have to make a payload which can carry an image.
p = MIMEBase('application','octet-stream') 
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header('Content-Disposition',f'attachment; filename={filename}')

msg.attach(p)

text = msg.as_string()
server.sendmail('sender@email.com','receiver@email.com',text)