def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname": "Diego","lastname": "Feversani"}

    super_list =[
        {"Firstname:": "Diego","Lastname:": "Feversani"},
        {"Firstname:": "Micaela","Lastname:": "Feversani"},
        {"Firstname:": "Fabrizio","Lastname:": "Feversani"},
        {"Firstname:": "Mariana","Lastname:": "Feversani"},
        {"Firstname:": "Rafael","Lastname:": "Feversani"},
    ]

    super_dict = {
        "natural_num":[1,2,3,4,5],
        "integer_nums":[-1, -2, 0, 1, 2],
        "floating_nums": [1.1, 4.5, 6.45]
    }

    for key, value in super_dict.items():
        print (key,"",value)

    for caracter in super_list:
        for key, value in caracter.items():
            print(key,"",value)

if __name__=="__main__":
    run()