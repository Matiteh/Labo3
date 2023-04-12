import socket
import requests
import json
import time

# Server

server = socket.socket(family = socket.AF_INET, type=socket.SOCK_STREAM)
server.bind(("0.0.0.0",8080))
flag=True
server.listen(2)
while True:
    connection, address = server.accept()
    if (flag==False):
        finTemp=time.time()
        if(finTemp>=(inicioTemp+300)):
            flag=True
    while True:
        data = connection.recv(1024)
        if data:
            print('\nSolicitud Recibida\n')
            if(flag ==False):
                print('Todavia no pasaron 5 minutos para actualizar')
            else:
                print('Informacion actualizada')
            print('Enviando de regreso los dato al cliente ')
            Diccionario = json.loads(data.decode('utf-8'))
            if(flag ==True):
                r = requests.get('https://www.frcon.utn.edu.ar/galileo/downld02.txt')
                texto = r.text.split("\r\n")
                tamaño = len(texto)
                array = texto[(tamaño-2)]
                temp= array[18:23]
                hume= array[40:43]
                inicioTemp=time.time()


            if(Diccionario == {"temperatura":""} ):
                Diccionario['temperatura'] = temp
                data = json.dumps(Diccionario).encode('utf-8')
                connection.sendall(data)
            elif(Diccionario == {"humedad":""} ):
                Diccionario['humedad'] = hume
                data = json.dumps(Diccionario).encode('utf-8')
                connection.sendall(data)
            elif(Diccionario == {"temperatura":"","humedad":""} ):
                Diccionario['temperatura'] = temp
                Diccionario['humedad'] = hume
                data = json.dumps(Diccionario).encode('utf-8')
                connection.sendall(data)
        else:
            print('No hay mas datos de:', address)
            flag=False
            break