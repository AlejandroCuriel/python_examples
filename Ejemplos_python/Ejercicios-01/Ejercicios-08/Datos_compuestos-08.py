#Jorge Alejandro Curiel Galindo
#Proponer una representación con tuplas para las cartas de la baraja francesa.
#Escribir una función poker que recibe cinco cartas de la baraja francesa e informe
#(devuelva el valor lógico correspondiente) si esas cartas forman o no un poker (es
#decir que hay 4 cartas con el mismo número).
def func_poker(mazo):
    for cartas in mazo:
        cont=0
        for i in range(len(mazo)):
            if(cartas == mazo[i]):
                cont+= 1
                if(cont>=4):
                    return print("POKER!!") 
    return print("No hay poker :(")

poker = (2,4,4,4,4)
func_poker(poker)