#Jorge Alejandro Curiel Galindo
#Escribir una función dia_siguiente_e que dada una fecha expresada como la terna
#(Día, Mes, Año) (donde Día, Mes y Año son números enteros) calcule el día siguiente
#al dado, en el mismo formato.

##### 1.- FORMA ####
# import datetime
# def dia_siguiente_e(fecha):
#     fecha2= fecha.today() + datetime.timedelta(days=1)
#     print(f"Fecha de hoy: {fecha.strftime('%d')}/{fecha.strftime('%m')}/{fecha.strftime('%y')}")
#     print(f"Fecha de mañana: {fecha2.strftime('%d')}/{fecha2.strftime('%m')}/{fecha2.strftime('%y')}")

# hoy=datetime.datetime.now()
# dia_siguiente_e(hoy)

##### 2.- FORMA #####
import datetime
def dia_siguiente_e(dia,mes,anio):
    print(f"El dia de hoy es: {dia}/{mes}/{anio}")
    print(f"El dia de mañana sera: {int(dia)+1}/{mes}/{anio}")
hoy = datetime.datetime.now()
dia=int(hoy.strftime("%d"))
mes=int(hoy.strftime("%m"))
anio=int(hoy.strftime("%y"))
dia_siguiente_e(dia,mes,anio)