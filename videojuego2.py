import random 

def comprobacion(num_ale,num):
    if num_ale > num:
        print("Elige un numero más grande!")
        return(True)
    elif num > num_ale:
        print("Elige un numero más pequeño!")
        return(True)
    else:
        print("El numero es el correcto!")
        return(False)


def genera():
    num_ale = random.randint(0,100)
    print(num_ale)
    return(num_ale)

def ingreso_num():
    num=int(input("Elige un numero del 1 al 100: "))
    while (num < 0 or num >100): 
        print("Numero fuera de rango, vuelva a ingresar el numero!")
        num=int(input("Elige un numero del 1 al 100: "))

    return(num)
         

def run():
    num_ale=genera()
    ciclo=True
    while(ciclo):
        num=ingreso_num()
        ciclo=comprobacion(num_ale,num)

    

if __name__ =="__main__":
    run()