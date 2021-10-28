def es_primo(num):
    sum=0
    for cont in range (2,num + 1):
        if (num % cont == 0):
            print("El numero "+ str(cont) + " es divisor")
            sum=sum+1
            if sum == 2:
                return(False)
    
    return(True)

def run():
    num=int(input("Ingrese numero: "))
    valor=es_primo(num)
    if (valor):
        print("Es primo!")
    else:
        print("No es primo!")
    

if __name__ == "__main__":
    run()