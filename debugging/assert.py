def divisors_comprehension(num):
    my_list= [i for i in range(1, num + 1) if num % i == 0]
    return(my_list)


def run():
    num = input("Ingrese un numero: ")
    
    assert num.isnumeric(),"Debes ingresar un numero"

    print(divisors_comprehension(int(num)))
    print("Terminó mi programa")


if __name__ == "__main__":
    run()