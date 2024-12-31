import smtplib 
import os 
import pandas as pd
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import logging
import logging.config
load_dotenv()

logging.basicConfig(
    level=logging.ERROR,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)
logger = logging.getLogger('emailLogger')

try:
    remitente = os.getenv('user')
    contraseña = os.getenv('password')
    asunto = 'Feliz año nuevo te desea DYGAV'

    data = pd.read_excel("data.xlsx")
    destinatarios = data["email"].tolist()

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(remitente, contraseña)

    for destinatario in destinatarios:
        msg = MIMEMultipart()

        msg['Subject'] = asunto
        msg['from'] = remitente
        msg['to'] = destinatario

        with open('new_year_email.html', 'r') as archivo:
            html = archivo.read()

        msg.attach(MIMEText(html, 'html', 'utf-8'))

        server.sendmail(remitente,destinatario,msg.as_string())

    server.quit()
    logger.info('Emails enviados con éxito')
except Exception as e:
    logger.error("Error: El correo no se envio" + str(e))
