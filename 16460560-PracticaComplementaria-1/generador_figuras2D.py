#Jorge Alejandro Curiel Galindo
import math
figuras = []

#---- CIRCULO
def crear_circulo(radio):
    def area_circulo(radio):
        area = math.pi * (radio**2)
        return "{0:.4}".format(area)
    def perimetro_circulo(radio):
        perimetro = 2 * math.pi * radio
        return "{0:.4}".format(perimetro)
    circulos={
            "tipo":'Circulo',
            "area":area_circulo(radio),
            "perimetro":perimetro_circulo(radio)
    }
    figuras.append(circulos)
    print(figuras)
#----TRIANGULOS

def crear_triangulo(lado_a,lado_b,lado_c): #Triangulo Equilatero
    if(lado_a == lado_b and lado_b == lado_c):
        def area_triangulo(lado_a):
            area = (math.sqrt(3) * lado_a**2) / 4
            return "{0:.3f}".format(area)
        def perimetro_triangulo(lado_a):
            perimetro = lado_a*3
            return "{0:.3f}".format(perimetro)
        triangulos={
                "tipo":'Triangulo Equilatero',
                "area":area_triangulo(lado_a),
                "perimetro":perimetro_triangulo(lado_a)            
        }
        figuras.append(triangulos)
        print(figuras)
    elif(lado_a == lado_b or lado_b == lado_c or lado_a == lado_c): #Triangulo Isosceles
        if(lado_a == lado_b):
            def area_triangulo(lado_a,lado_c):
                altura = math.sqrt((math.pow(lado_a,2)-math.pow(lado_c,2)/4))
                area = (lado_c * altura) / 2
                return "{0:.3f}".format(area)
            def perimetro_triangulo(lado_a, lado_c):
                perimetro = lado_a + lado_b + lado_c
                return perimetro
            triangulos={
                        "tipo":'Triangulo Isosceles',
                        "area":area_triangulo(lado_a,lado_c),
                        "perimetro":perimetro_triangulo(lado_a,lado_c)           
            }
            figuras.append(triangulos)
        elif(lado_b==lado_c):
            def area_triangulo(lado_a,lado_b):
                print(lado_a)
                print(lado_b)
                altura = math.sqrt((math.pow(lado_b,2)-math.pow(lado_a,2)/4))
                area = (lado_a * altura) / 2
                return "{0:.3f}".format(area)
            def perimetro_triangulo(lado_a, lado_b):
                perimetro = lado_a + lado_b + lado_c
                return perimetro
            triangulos={
                        "tipo":'Triangulo Isosceles',
                        "area":area_triangulo(lado_a,lado_b),
                        "perimetro":perimetro_triangulo(lado_a,lado_b)           
            }
            figuras.append(triangulos)
        else:
            def area_triangulo(lado_c,lado_b):
                altura = math.sqrt((math.pow(lado_c,2)-math.pow(lado_b,2)/4))
                area = (lado_b * altura) / 2
                return "{0:.3f}".format(area)
            def perimetro_triangulo(lado_c, lado_b):
                perimetro = lado_a + lado_b + lado_c
                return perimetro
            triangulos={
                        "tipo":'Triangulo Isosceles',
                        "area":area_triangulo(lado_c,lado_b),
                        "perimetro":perimetro_triangulo(lado_c,lado_b)       
            }
            figuras.append(triangulos)
    else:                                                           #Triangulo Escaleno
        def area_triangulo(lado_a,lado_b,lado_c):
            s=(lado_a+lado_b+lado_c)/2
            area=math.sqrt(s*(s-lado_a)*(s-lado_b)*(s-lado_c))
            print(area)
            return "{0:.3}".format(area)
        def perimetro_triangulo(lado_a,lado_b,lado_c):
            perimetro=lado_a+lado_b+lado_c
            return perimetro

        triangulos={
                    "tipo":'Triangulo Escaleno',
                    "area":area_triangulo(lado_a,lado_b,lado_c),
                    "perimetro":perimetro_triangulo(lado_a,lado_b,lado_c)       
        }
        figuras.append(triangulos)
    print(figuras)

#----FIN TRIANGULOS

#----CUADRADO
def crear_cuadrado(lado):
    def area_cuadrado(lado):
        area = float(lado*lado)
        return area
    def perimetro_cuadrado(lado):
        perimetro = float(lado*4)
        return perimetro
    cuadrados={
                "tipo":'Cuadrado',
                "area":area_cuadrado(lado),
                "perimetro":perimetro_cuadrado(lado)
    }
    figuras.append(cuadrados)
    print(figuras)
#----FIN CUADRADO


#----Funciones del menu principal
def borrar_figuras():
    figuras.clear()
    return print("-----> Se a borrado los datos con exito! <------")

def sumador_areas():
    total_area = 0.0
    fig=["Cuadrado","Triangulo","Circulo"]
    for figura in fig:
        for i in figuras:
            if(figura==i["tipo"].split(" ").pop(0)):
                total_area+=float(i['area'])
        print(f"El total de las areas del tipo de figura {figura} es de {total_area}")
        total_area = 0.0

def sumador_perimetro():
    total_perimetro = 0.0
    fig=["Cuadrado","Triangulo","Circulo"]
    for figura in fig:
        for i in figuras:
            if(figura==i["tipo"].split(" ").pop(0)):
                total_perimetro+=float(i['perimetro'])
        print(f"El total de los perimetros del tipo de figura {figura} es de {total_perimetro}")
        total_perimetro = 0.0

def listar_clasificacion(clasificacion): #Busqueda especifica
    if(clasificacion==1):
        clasificacion="Cuadrado"
    elif(clasificacion==2):
        clasificacion="Triangulo"
    else:
        clasificacion="Circulo"
    for i in figuras:
        if clasificacion == i['tipo'].split(" ").pop(0):
            print(i)

def imprimir(): #Imprimir todos
    print("----Todas las figuras guardadas----")
    fig=["Cuadrado","Triangulo","Circulo"]
    for figura in fig:
        print(f"***** -> Los registros de la figura: {figura} son los siguientes:")
        for i in figuras:
            if(figura == i["tipo"].split(" ").pop(0)):
                print(i)

def menu_figuras():
    bandera = True
    while(bandera == True):
        print("1.- Cuadrado \n2.- Triangulo \n3.- Circulo \n0.- Salir")
        opc = int(input("Ingrese una opcion: "))
        if(opc==1):
            print("*****-----Creando una figura Cuadrado-----*****")
            lado = int(input("Ingrese un lado del cuadrado: "))
            crear_cuadrado(lado)
        elif(opc==2):
            print("opcion triangulo")
            lado_a = int(input("Ingrese el lado A del triangulo: "))
            lado_b = int(input("Ingrese el lado B del triangulo: "))
            lado_c = int(input("Ingrese el lado C del triangulo: "))
            crear_triangulo(lado_a, lado_b, lado_c)
        elif(opc==3):
            radio=float(input("Ingrese el radio del circulo: "))
            crear_circulo(radio)
            print("opcion circulo")
        elif(opc==0):
            print("salir")
            bandera=False
        else:
            print("Opcion no valida")
            bandera=True
def main():
    bandera = True
    while(bandera==True):
        print("1.- Crear Figura \n2.- Listar una clasificacion de figuras" 
                    "\n3.- Listar todas las figuras \n4.- Mostrar suma de todas las àreas"
                    "\n5.- Mostrar la suma de todos los perimetros \n6.- Limpiar lista \n0.- Salir")
        opc = int(input("Ingrese una opcion: "))
        if(opc==1):
            menu_figuras()
        elif(opc==2):
            bandera = True
            while(bandera == True):
                print("---¿De que figuras desea buscar en la lista?---\n1.- Cuadrado \n2.- Triangulo \n3.- Circulo \n0.- Salir")
                clasificacion = int(input("Ingresar opcion ---> : "))
                if(clasificacion == 0):
                    break
                elif(clasificacion>=4):
                    print("-----> ERROR:Opcion no validad, intente de nuevo <-----")
                    bandera = True
                else:
                    listar_clasificacion(clasificacion)
        elif(opc==3):
            if(len(figuras)==0):
                print("----> NO EXISTEN DATOS <----")
            else:
                imprimir()
        elif(opc==4):
            sumador_areas()

        elif(opc==5):
            sumador_perimetro()

        elif(opc==6):
            print("\t \t ********* ADVERTENCIA *********")
            sure = input("Esta seguro que desea eliminar TODOS los datos de la lista?\n"
                        "Y -> Si estoy seguro \nN -> No, cancelar\n : ----> ")
            if (sure == 'Y' or sure == "y"):
                borrar_figuras()
            else:
                bandera == True

        elif(opc==0):
            print("0")
            bandera =False
        else:
            print("ERROR -> Opcion no valida!!")
            bandera =True
main()