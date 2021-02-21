#Jorge Alejandro Curiel Galindo
#Realiza una función llamada area_circulo(radio) que devuelva el área de un
#círculo a partir de un radio. Calcula el área de un círculo de 5 de radio.

def area_circulo(radio):
    pi=3.14159
    area = pi*(radio**2)
    return (f"El area del circulo es de: {round(area,2)}")

print(area_circulo(5))