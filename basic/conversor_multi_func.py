cot_arg=65
cot_col=3875
cot_mex=24

def convertir(cot,monto):
    res = monto/cot
    res = str(res)
    return(res)

menu = """
Bienvenido al conversor de monedas.

1 - Pesos Mexicanos
2 - Pesos Colombianos
3 - Pesos Argentinos

Elige una opcion: 

"""

opcion= int(input(menu))

if opcion == 1:
    monto = float(input("Ingrese el monto en pesos mexicanos: "))
    res=convertir(cot_mex,monto)
    print("Tienes " + res + " dolares")
elif  opcion == 2:
    monto = float(input("Ingrese el monto en pesos colombianos: "))
    res=convertir(cot_col,monto)
    res = str(res)
    print("Tienes " + res + " dolares")
elif opcion == 3:
    monto = float(input("Ingrese el monto en pesos argentinos: "))
    res=convertir(cot_arg,monto)
    print("Tienes " + res + " dolares")
else: 
    print("\nOpcion equivocada") 



# EJEMPLO DE FUNCION
# def suma(a, b):
#     print("Se suman dos numero")
#     resultado= a+b
#     return(resultado)

# sumatoria= suma(1,4)
# print(sumatoria)