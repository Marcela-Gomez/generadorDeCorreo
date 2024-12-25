import smtplib 
import os 
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import logging
import logging.config

load_dotenv()

try:
    remitente = os.getenv('user')
    contraseña = os.getenv('password')
    destinatario = 'feraguilar6985@gmail.com'
    asunto = 'Feliz navidad te desea DYGAV'

    msg = MIMEMultipart()

    msg['Subject'] = asunto
    msg['from'] = remitente
    msg['to'] = destinatario

    with open('chirstmas_email.html', 'r') as archivo:
        html = archivo.read()

    msg.attach(MIMEText(html, 'html',"utf-8"))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(remitente, contraseña)

    server.sendmail(remitente,destinatario,msg.as_string())

    server.quit()
except Exception as e:
    logger = logging.getLogger('simpleExample')
    logger.error("Error: El correo no se envio")
