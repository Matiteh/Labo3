import socket
import requests
import json
import time

# Cliente 
host = '192.168.201.54'
port = 8080

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
client_socket.connect((host, port))

diccionario= {"temperatura":"", "humedad":""}
client_socket.sendall(json.dumps(diccionario).encode('utf-8'))
 
data = client_socket.recv(1024)

print(f"Datos recibidos del servidor: {data.decode('utf-8')}")

client_socket.close()