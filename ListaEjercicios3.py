##Pregunta 2
texto=str("""Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto.
Lorem Ipsum ha sido el texto de relleno estándar de las industrias desde el año 1500, cuando un
impresor (N. del T. persona que se dedica a la imprenta) desconocido usó una galería de textos
y los mezcló de tal manera que logró hacer un libro de textos especimen.""")
print("elije una de las opciones: ")
opciones="""
A Separar texto
B Unir texto
C Contar texto
D Encontrar texto
E Convertir a mayúsculas
F Convertir a minúsculas
"""
print(opciones)
opcion=input("Ingresa la opción: ")
if opcion=="A":
   print(texto.split(sep=" "))
else:
   if opcion=="B":
     print(" ".join(texto.split(sep=" ")))
   else: 
     if opcion=="C":
       print(texto.count("Lorem"))
     else:
        if opcion=="D":
            print(texto.find("Lorem"))
        else:
            if opcion=="E":
                print(texto.upper())
            else: 
                if opcion=="F":
                    print(texto.lower())
                else:
                    print("Elija una opción válida")
##Pregunta 3
def bar(x):
    x=x*2
    return x
x=int(input("Ingrese un valor entero: "))
bar(x)
x=bar(x)
print(x)
def bar2(x):
    x=x/5
    return x
bar2(x)
x=bar2(x)
print(x)   
##Pregunta 4

class producto:
    def __init__(self, nombre, marca, precio, cantidad, productid):
        self.nombre=nombre
        self.marca=marca
        self.precio=precio
        self.cantidad=cantidad
        self.productid=productid
    def __str__(self):
        return f'El producto tiene los siguientes atributos {self.nombre}, {self.marca}, {self.precio}, {self.cantidad}, {self.productid}'


class Catalogo:
    listproducto = []
    def __init__(self, listproducto:list=[]):
        self.listproducto=listproducto
    def agregar(self, c): 
        self.listproducto.append(c)
    def mostrarCatalogo(self):
        for i,c in enumerate(self.producto):
            i+=1
            print(i,c)
try:
    c1=producto('parachoque', 'toyota', '200', '4','1334')
    c2=producto('espejo', 'toyota', '200', '4','1334')
    print(c1)
    a=c1.nombre
    print(a)
    b=c2.nombre
    print(b)
    catalogo=[c1, c2]
    for i in catalogo:
        print(i)
    catalogo.agregar(c1)
    catalogo.agregar(c2)
    catalogo.mostrarCatalogo()
except Exception as e:
    print("Error al crear los objetos productos")
    print(e)


##pregunta 6

import os
ruta = r'c:/Users/Usuario/Desktop/pythonWorkspace/ListaEjercicios3.py'
nombre_archivo = os.path.basename(ruta)
print(nombre_archivo)

##pregunta 7
class Producto:
    def __init__(self, codigo):
        self.codigo = codigo
        print('Se ha creado el producto:', self.codigo)
    def __str__(self):
        return f'El codigo del producto es {self.codigo}'
pais= input("ingresar el país de origen: ")
lote= input("ingrese el número del lote: ")
año= input("ingresar el año: ")
p=Producto(pais.upper()+ "-"+lote+ "-"+año)
print(str(p))





