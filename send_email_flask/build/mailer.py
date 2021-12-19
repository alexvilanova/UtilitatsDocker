import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def envia_email(email_destinatari:str, titol:str, cos:str, confirmacio:bool = True):

    email_origen = "test@gmail.com"

    mostra_email(
        email_origen = email_origen,
        email_destinatari = email_destinatari,
        titol = titol,
        cos = cos,
        confirmacio = confirmacio
    )

    port = 587  # For starttls
    servidor_smtp = "smtp.gmail.com"
    password = "password-de-test"

    missatge = MIMEMultipart("alternative")
    missatge["Subject"] = titol
    missatge["From"] = email_origen
    missatge["To"] = email_destinatari
    missatge.attach(MIMEText(cos, "html"))

    context = ssl.create_default_context()
    with smtplib.SMTP(servidor_smtp, port) as server:
        server.starttls(context=context)
        server.login(email_origen, password)
        server.sendmail(email_origen, email_destinatari, missatge.as_string())

def mostra_email(email_origen:str, email_destinatari:str, titol:str, cos:str, confirmacio:bool):
    print("------------------------------------------------------")
    print(f"From: {email_origen}")
    print(f"To: {email_destinatari}")
    print(f"Subject: {titol}")
    print(cos)
    print("------------------------------------------------------")
    if confirmacio:
        input("Pulsa qualsevol tecla per enviar o CTRL + C per cancel·lar")


################################################################################################
#
# Prova d'enviament d'emails
#

envia_email(
    email_destinatari = "boriyox968@swsguide.com",
    titol = "Hola!",
    cos = "Això és una prova!\nEm reps?\nTot bé?"
)
