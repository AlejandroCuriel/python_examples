#Jorge Alejandro Curiel Galindo
#Escribir un programa que almacene las asignaturas de un curso (por ejemplo
#Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por
#pantalla.
asignaturas = []
def agregarAsignaturas(asignatura):
    asignaturas.append(asignatura)

agregar_Asignaturas("Matematicas")
agregar_Asignaturas("Fisica")
agregar_Asignaturas("Quimica")
agregar_Asignaturas("Historia")
agregar_Asignaturas("Ingles")
print(asignaturas)