def run():

    #con list
    my_list = [1,2,3,4,5]

    squares = [i**2 for i in my_list]

    print(squares)

    #con maps

    squares2 = list(map(lambda x: x**2,my_list))

    print(squares2)
    


if __name__ == "__main__":
    run()