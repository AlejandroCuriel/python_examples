#Jorge Alejandro Curiel Galindo
#El tiempo como tuplas.
#1. Proponer una representación con tuplas para representar el tiempo.
#2. Escribir una función sumaTiempo que reciba dos tiempos dados y devuelva
#su suma.
import datetime
def sumaTiempo(hoy,navidad):
    suma=hoy.today() + datetime.timedelta(days=navidad.day)
    print(suma)

hoy=datetime.datetime.now()
navidad = datetime.datetime(2021,12,24,23,59,59,59)
sumaTiempo(hoy,navidad)