import random

def generar_pass():
    mayusculas = ["A","B","C","D","E","F","G"]
    minusculas = ["a","b","c","d","e","f","g"]
    numeros = ["1","2","3","4","5","6","7"]

    caracteres = mayusculas + minusculas + numeros

    password = []

    for i in range(15):
        caracter_random = random.choice(caracteres)
        password.append(caracter_random)

    password = "".join(password)

    return(password)



def run():
    password= generar_pass()
    print("Tu nueva contraseña es: " + password)




if __name__=="__main__":
    run()