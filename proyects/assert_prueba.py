def divisors_comprehension(num):
    my_list2 = [i for i in range(1, num + 1) if num % i == 0]
    return(my_list2)

def run():
        num = int(input("Ingrese un numero: "))
        assert num > 0 or num == 0, "Ingresa un numero positivo!"
        
        print(divisors_comprehension(num))
        print("Terminó mi programa")



if __name__ == "__main__":
    run()