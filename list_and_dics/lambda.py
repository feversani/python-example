palindrome = lambda string: string == string[::-1]

def run():
    word = input("Ingrese una palabra: ")
    if palindrome(word):
        print("Es palindromo!")
    else:
        print("No es palindromo!")

if __name__ == "__main__":
    run()