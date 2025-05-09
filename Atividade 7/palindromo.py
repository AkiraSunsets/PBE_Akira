print("Palindromos")

def verify_palindromo(word):
    invert_word = word[::-1]
    if word == invert_word:
        print(f"A palavra {word} é um palindromo")
    else:
        print(f"A palavra {word} não é um palindromo")

verify_palindromo("Ana Ana")
verify_palindromo("1DSTB-SENAI")
verify_palindromo("Subi no Onibus")
