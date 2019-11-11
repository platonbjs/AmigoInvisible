import random
import csv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# Funcion para enviar correos
def send_mail(recipient, amigo_invisible):
    fromaddr = 'your_email@domain.com'
    toaddrs  = recipient
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Your subject"
    msg['From'] = fromaddr
    msg['To'] = recipient
    text = "Hola!\nTu amigo invisible es \n"+amigo_invisible
    html = """\
    <html>
        <head></head>
            <body>
                <p>Hola!<br>
                Tu amigo invisible es<br>
                <b>"""+amigo_invisible+"""</b>
                </p>
            </body>
        </html>
    """
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')
    msg.attach(part1)
    msg.attach(part2)
    username = 'username'
    password = 'password'

    # Enviando el correo desde gmail
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username,password)
    server.sendmail(fromaddr, toaddrs, msg.as_string())
    server.quit()
    #print("Enviado correo a",recipient,"para que regale a", amigo_invisible)
def leer_participantes():
    # csv con email,nombre
    with open('participantes.csv', mode='r') as f:
        reader = csv.reader(f)
        participantes = list(reader)
        return participantes


# Creamos una nueva lista con orden aleatorio
def create_random_list(participantes):
    lista_random=[]
    temp = participantes.copy()
    num_part = len(participantes)

    for i in range(0,num_part):
        num = random.randint(1,len(temp))
        lista_random.append(temp[num-1])
        temp.pop(num-1)
    return lista_random
# Hacemos el sorteo asignandole a cada participante el siguiente en la lista de forma circular
def hacer_sorteo(lista_random):
    num_part = len(lista_random)
    for i in range(0,num_part):
        send_mail(lista_random[i][0], lista_random[(i+1)%(num_part)][1])
# Main function
def main():
    participantes = leer_participantes()
    lista_random = create_random_list(participantes)
    hacer_sorteo(lista_random)

if __name__ == "__main__":
    main()
