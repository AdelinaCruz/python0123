## pregunta 1
def main():
    print("Solución")
if __name__=='__main__':
    main()

##pregunta 5

while(True):
    try:
        from módulo.modulo1 import sumarNumeros
        n=int(input("Ingrese un número entero: "))
        print(sumarNumeros(n))
    except:
        print("Ha ocurrido un error, introduce bien el número")
    else:
        import os
        ruta2=os.getcwd()
        print(ruta2)
        break  # Importante romper la iteración si todo ha salido bien
    finally:
        print("Proceso terminado") # Siempre se ejecuta

while(True):
    try:
        from módulo.modulo2 import dividirNumeros
        a=int(input("Ingrese el primer número: "))
        b=int(input("Ingrese el segundo número: "))
        print(dividirNumeros(a,b))
    except:
        print("Ha ocurrido un error, introduce bien el número")
    else:
        import os
        ruta2=os.getcwd()
        print(ruta2)
        break  # Importante romper la iteración si todo ha salido bien
    finally:
        print("Proceso terminado") # Siempre se ejecuta


