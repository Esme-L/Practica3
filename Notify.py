import smtplib
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

COMMASPACE = ', '
# Define params
rrdpath = '/home/esme/Escritorio/Admonredes/Practica3/RRD/'
imgpath = '/home/esme/Escritorio/Admonredes/Practica3/IMG/'
#fname = 'trend.rrd'

mailsender = "paralosmama3@gmail.com"
mailreceip = "paralosmama3@gmail.com"
mailserver = 'smtp.gmail.com: 587'
password = 'cahfprbgkoyvwaev'

def send_alert_attached(subject: str, mensaje: str, imagen: str):
    """ Envía un correo electrónico adjuntando la imagen en IMG
    """
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = mailsender
    msg['To'] = mailreceip
    m = mensaje
    msg.attach(MIMEText(m, _charset='utf-8'))
    fp = open(imgpath+imagen+'.png', 'rb')
    img = MIMEImage(fp.read())
    fp.close()
    msg.attach(img)
    s = smtplib.SMTP(mailserver)

    s.starttls()
    # Login Credentials for sending the mail
    s.login(mailsender, password)

    s.sendmail(mailsender, mailreceip, msg.as_string())
    s.quit()