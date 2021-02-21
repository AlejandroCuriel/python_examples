#Jorge Alejandro Curiel Galindo
#Escribir una función dia_siguiente_t que dada una fecha expresada como la terna
#(Día, Mes, Año) (donde Día y Año son números enteros, y Mes es el texto Ene, Feb, ...,
#Dic, según corresponda) calcule el día siguiente al dado, en el mismo formato.
import datetime
def dia_siguiente_t(dia,mes,anio):
    print(f"El dia de hoy es: {dia}/{mes}/{anio}")
    print(f"El dia de mañana sera: {dia+1}/{mes}/{anio}")
hoy=datetime.datetime.now()
dia=hoy.day
mes=hoy.strftime("%b")
anio=hoy.year
dia_siguiente_t(dia,mes,anio)

