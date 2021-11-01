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
    num = int(input("Ingrese un numero: "))

    print(dividors(num))
    print(divisors_comprehension(num))
    print("Terminó mi programa")

if __name__ == "__main__":
    run()