import smtplib
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from getSNMP import consultaSNMP
from getSNMP import consultaSNMP2

COMMASPACE = ', '
# Define params
rrdpath = '/home/esme/Escritorio/Admonredes/Practica3/RRD/'
imgpath = '/home/esme/Escritorio/Admonredes/Practica3/IMG/'
#fname = 'trend.rrd'

mailsender = "paralosmama3@gmail.com"
mailreceip = "dummycuenta3@gmail.com"
mailserver = 'smtp.gmail.com: 587'
password = 'cahfprbgkoyvwaev'
aux = consultaSNMP2('EsmeraldaZP', '192.168.100.245', '1.3.6.1.2.1.1.1.0')
SO = aux.split()[14]
VersionSO = aux.split()[16]
aux = consultaSNMP2('EsmeraldaZP', '192.168.100.245','1.3.6.1.2.1.1.5.0')
nombreDis = aux.split()[2]
aux =  consultaSNMP2('EsmeraldaZP', '192.168.100.245', '1.3.6.1.2.1.1.3.0')
Timepo = aux.split()[2]
 

def send_alert_attached(subject: str, mensaje: str, imagen: str):
    """ Envía un correo electrónico adjuntando la imagen en IMG
    """
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = mailsender
    msg['To'] = mailreceip
    m = mensaje 
    m2 = "Dispositivo: " + nombreDis + " Sistema Operativo: " + SO + " Version: " + VersionSO + " Tiempo sistema: " + Timepo + " Comunidad: EsmeraldaZP"
    msg.attach(MIMEText(m, _charset='utf-8'))
    msg.attach(MIMEText(m2, _charset='utf-8'))
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