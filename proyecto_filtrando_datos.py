DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]
def show_dev_python():
    print("Programadores de Python: ")
    all_python_devs = [dev["name"] for dev in DATA if dev["language"] == "python"]

    for i in all_python_devs:
        print(i)

def show_platzi():
    print("Empleados de Platzi: ")
    all_platzi_workers = [worker["name"] for worker in DATA if worker["organization"] == "Platzi"]

    for i in all_platzi_workers:
        print (i)

def show_adults():
    adults = list (filter(lambda adult: adult["age"] > 18, DATA))
    adults = list(map(lambda adult: adult["name"], adults))


    for i in adults:
        print (i)

def old_people():
    old = list(map(lambda worker: worker | {"old": worker ["age"] > 70}, DATA))
    
    for key in old:
        print (key)

def run():
    #show_dev_python()
    #show_platzi()
    #show_adults()
    old_people()


    


if __name__ == "__main__":
    run()