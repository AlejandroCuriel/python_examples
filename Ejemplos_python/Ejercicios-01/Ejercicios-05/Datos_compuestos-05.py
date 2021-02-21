#Jorge Alejandro Curiel Galindo
#Realiza una función separar(lista) que tome una lista de números enteros
#desordenados y devuelva dos listas ordenadas. La primera con los números pares y la
#segunda con los números impares.
pares=[]
impar=[]
def seperar(lista):

    for num in lista:
        if(num % 2 ==0):
            pares.append(num)
        else:
            impar.append(num)
seperar({1,2,3,4,5,6,7,8,9,10})
print(f"Lista de numeros pares: {pares}")
print(f"Lista de numeros impares: {impar}")