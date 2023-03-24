import requests
import datetime
r= requests.get('https://www.frcon.utn.edu.ar/galileo/downld02.txt')

texto= r.text.split("\r\n")
largo=len(texto)
array = texto[(largo-2)]

print("El dia "+array[0:8])
print("A la hora "+array[10:16])
print("La temperatura fue de "+array[18:23])
