def run():

    my_list = []
    my_list2 = []

    for n in range(101):
        print("El numero " + str(n) + " elevado al cuadrado es: " + str(n**2))
        my_list.append(n**2)

    for n in range(101):
        if (n % 3 != 0):
            my_list2.append(n**2)
    
    print(my_list2)
    
    # [element for element in interable if condition]

    my_list3= [i**2 for i in range (101) if (i**2 % 3 != 0)]
    print("Lista comprehension")
    print(my_list3)

    my_list4 = [i for i in range(1,100001) if (i % 4 == 0 and i % 6 == 0 and i % 9 == 0 )]
    print("Lista Reto:")
    print(my_list4)

if __name__ == "__main__":
    run()
