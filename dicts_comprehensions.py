#Crear un diccionario donde las llaves son los primeros 100 numeros natrurales y los valores elevados al cubo

def run():
    dict = {}
    dict2 = {}

    for n in range(101):
        dict[n] = n**3

    for key,value in dict.items():
        print(key,value)
    

    for n in range(101):
        if n % 3 != 0:
            dict2[n] = n**3

    for key,value in dict2.items():
        print(key,value)

    # [key: value for value in interable if condition]
    dict3 = {i: i**3 for i in range(1,101) if i % 3 != 0}
    print ("DICCIONARIO 3 COMIENZO")

    for key,value in dict3.items():
        print(key,value)
    
    dict4 = { i: i**0.5 for i in range(1000)}
    print("DICCIONARIO AL CUADRADO!")
    for key,value in dict4.items():
        print(key,value)
    

if __name__ == "__main__":
    run()