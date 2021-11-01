# menu = """
# Bienvenido al conversor de monedas.

# 1 - Pesos Mexicanos
# 2 - Pesos Colombianos
# 3 - Pesos Argentinos

# Elige una opcion: 

# """

# opcion= int(input(menu))

# if opcion == 1:
#     cot_mex = float(input("Ingrese la cotizacion de pesos mexicanos a dolar: "))
#     monto = float(input("Ingrese el monto en pesos mexicanos: "))
#     res = monto/cot_mex
#     res = str(res)
#     print("Tienes " + res + " dolares")
# elif  opcion == 2:
#     cot_col = float(input("Ingrese la cotizacion de pesos colombianos a dolar: "))
#     monto = float(input("Ingrese el monto en pesos colombianos: "))
#     res = monto/cot_col
#     res = str(res)
#     print("Tienes " + res + " dolares")
# elif opcion == 3:
#     cot_arg = float(input("Ingrese la cotizacion de pesos argentinos a dolar: "))
#     monto = float(input("Ingrese el monto en pesos argentinos: "))
#     res = monto/cot_arg
#     res = str(res)
#     print("Tienes " + res + " dolares")
# else: 
#     print("\nOpcion equivocada")

def suma(a, b):
    print("Se suman dos numero")
    resultado= a+b
    return(resultado)

sumatoria= suma(1,4)
print(sumatoria)