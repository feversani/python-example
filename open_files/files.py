import os
FILE_PATH=os.path.dirname(__file__)

def write():
    names = ["Facundo", "Miguel", "Pepe", "Christian"]
    with open(f"{FILE_PATH}/folder/names.txt","w") as f:
        for name in names:
            f.write(name)
            f.write("\n")


def read():
    numbers = []
    with open(f"{FILE_PATH}/folder/numbers.txt","r", encoding="utf-8") as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)

def run():
    read()
    write()


if __name__ == "__main__":
    run()