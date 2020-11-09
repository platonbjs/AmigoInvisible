import random
import csv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Configuracion
# csv con email,nombre
FICHERO_PARTICIPANTES = 'participantes.csv'
SENDER = 'your_email@domain.com'
USERNAME = "username"
PASSWORD = "password"
MAIL_SERVER = 'smtp.gmail.com:587'
SUBJECT = 'Tu amigo invisible'
##########

# Funcion para enviar correos
def send_mail(recipient, amigo_invisible):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = SUBJECT
    msg['From'] = SENDER
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
    username = USERNAME
    password = PASSWORD

    # Enviando el correo
    server = smtplib.SMTP(MAIL_SERVER)
    server.starttls()
    server.login(username,password)
    server.sendmail(SENDER, recipient, msg.as_string())
    server.quit()
    print("Enviado correo a",recipient)

def leer_participantes():
    with open(FICHERO_PARTICIPANTES, mode='r') as f:
        reader = csv.reader(f)
        participantes = list(reader)
    return participantes

# Creamos la combinacion de los elementos sin repeticiones
def crear_combinatoria(size):
    lista_combinada=[]
    for i in range(size):
        for j in range(size):
            if i != j:
                lista_combinada.append((i,j))
    return(lista_combinada)

def hacer_sorteo(lista_combinada):
    # Creamos contador para la lista resultante
    # Creamos la lista de salida
    lista_definitiva=[]
    # Ejecutamos el bucle hasta que vaciemos la lista
    while (len(lista_combinada)>0):
        #Mezclamos la lista_aux
        lista_combinada = random.sample(lista_combinada,len(lista_combinada))
        #Guardamos el primer elemento
        muestra = lista_combinada[0]
        lista_definitiva.append(muestra)
        # Recorremos toda la lista
        i=0
        while i < len(lista_combinada):
            # Buscamos elementos que coincidan primer o segundo elemento del
            # emparejamiento con la muestra
            if(lista_combinada[i][0]==muestra[0] or lista_combinada[i][1]==muestra[1]):
                # Eliminamos el emparejamiento
                lista_combinada.remove(lista_combinada[i])
                i -= 1
            i += 1
    return lista_definitiva

def create_random_list(participantes):
    lista_random=[]
    temp = participantes.copy()
    num_part = len(participantes)
    for i in range(num_part):
        num = random.randint(1,len(temp))
        lista_random.append(temp[num-1])
        temp.pop(num-1)
    return lista_random

# Main function
def main():
    # Guardo los participantes del
    participantes = leer_participantes()
    lista_combinada = crear_combinatoria(len(participantes))
    resultado=hacer_sorteo(lista_combinada)
    while len(resultado)<len(participantes):
        resultado=hacer_sorteo(lista_combinada)
    for i in range(len(resultado)):
        regalador=participantes[resultado[i][0]][0]
        regalado=participantes[resultado[i][1]][1]
        #sendmail(regalador,regalado)
        # Linea para hacer pruebas sin enviar
        print("Regalador: "+regalador+" Regalado: "+regalado)
if __name__ == "__main__":
    main()
