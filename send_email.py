import smtplib 
import os 
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

load_dotenv()

remitente = os.getenv('user')

destinatario = 'margomez45sarai@gmail.com'
asunto = 'Bienvenido a DYGAV'

msg = MIMEMultipart()

msg['Subject'] = asunto
msg['from'] = remitente
msg['to'] = destinatario

with open('message.html', 'r') as archivo:
    html = archivo.read()

msg.attach(MIMEText(html, 'html'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(remitente, os.getenv('password'))

server.sendmail(remitente,destinatario,msg.as_string())

server.quit()