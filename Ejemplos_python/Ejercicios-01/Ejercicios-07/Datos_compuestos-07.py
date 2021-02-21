#Jorge Alejandro Curiel Galindo
#Escribir un programa que pregunte al usuario los números ganadores de la lotería
#primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a
#mayor.
#Escribir un programa que almacene en una lista los números del 1 al 10 y los
#muestre por pantalla en orden inverso separados por comas.
num_ganadores=[]
for i in range(5):
    num = int(input("Ingrese los numeros ganadores de la loteria: "))
    num_ganadores.append(num)
num_ganadores.sort()
print(f"Los numeros ordenadors de menor a mayor son: {num_ganadores}")

#Escribir un programa que almacene en una lista los números del 1 al 10 y los
#muestre por pantalla en orden inverso separados por comas.
num = []
for i in range(1,11,1):
    num.append(i)
num.sort(reverse=True)
print(num)