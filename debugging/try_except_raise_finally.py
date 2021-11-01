def divisors_comprehension(num):
    my_list2 = [i for i in range(1, num + 1) if num % i == 0]
    return(my_list2)

def dividors(num):
    my_list = []

    for i in range(1,num + 1):
        if num % i == 0:
            my_list.append(i)
    return(my_list)

def run():
    try:
        num = int(input("Ingrese un numero: "))
        if num < 0 or num == 0:
            raise ValueError
        else:
            print("hola")
            print(dividors(num))
            print(divisors_comprehension(num))
            print("Terminó mi programa")
    except ValueError:
        print("Debe ingresar un numero positivo!")


if __name__ == "__main__":
    run()