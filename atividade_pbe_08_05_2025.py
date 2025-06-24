# 1)
print("Calcular o dobro do preço de 3 produtos para uma promoção")
print("produto A: 5,00")
print("produto B: 8,00")
print("produto C: 12,00")
a = 5.00
b = 8.00
c = 12.00

def dobro(number):
    calc = number * 2
    return calc

result = dobro(a)
print(f"O dobro de {a} será {result}")
print("=" * 50)

# 2)
print("Boas vindas curso online, 3 alunos se matricularam, João, Maria, Carlos")

def boas_vindas():
    print("Sejam bem-vindos ao curso online, João!")
    print("Sejam bem-vindos ao curso online, Maria!")
    print("Sejam bem-vindos ao curso online, Carlos!")

boas_vindas()
print("=" * 50)

# 3)
print("Tabuleiro 10 faces, 4,7,10, pares ou ímpares")

def start_finish(jogadas):
    if jogadas % 2 == 0:
        print("Par! Avance!")
    else:
        print("Ímpar! Fim!")
    return jogadas

start_finish(4)
start_finish(7)
start_finish(10)
print("=" * 50)

# 5)
#print("Tabuada 2,3,4")

def tabuada(numero):
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} X {i} = {resultado}")

tabuada(2)
tabuada(3)
tabuada(4)
print("=" * 50)

# 6)
#print("Verificação clientes 8, 15, 20, cinema")

def verify(age):
    if age < 20:
        if age == 8 or age == 15:
            print("Sua idade é inferior à permitida, proibido entrar!\n")
        else:
            print("Sua idade é inferior à permitida, proibido entrar!\n")
    else:
        print("Idade adequada, entrada permitida!\n")

verify(15)
verify(20)
verify(8)
print("=" * 50)

# 7)
print("Desconto 10% em 3 produtos, calcule o preço final")

def desconto_produto(product):
    result = product - (product * 0.10)
    print(f"O preço do produto {product:.2f} com desconto de 10% é: {result:.2f}\n")

desconto_produto(50.00)
desconto_produto(120.00)
desconto_produto(200.00)
print("=" * 50)

# 8)
print("Quantidade de letras (python, paralelepípedo)")

def letter(word):
    print(f"A palavra {word} possui {len(word)} letras.")

letter("casa")
letter("paralelepipedo")
letter("python")
print("=" * 50)

# 9)
print("Converter Celsius para Fahrenheit")

def fah(temp):
    result = (temp * 1.8) + 32
    print(f"A temperatura {temp:.2f} ºC em Fahrenheit é {result:.2f} ºF")
    return result

fah(30)
fah(100)
fah(0)
print("=" * 50)

# 10)
print("RPG - small, medium, large")

def size_number(number):
    if number <= 5:
        print(f"O número {number} é pequeno!")
    elif number <= 10:
        print(f"O número {number} é médio!")
    else:
        print(f"O número {number} é grande!")

size_number(3)
size_number(9)
size_number(12)
print("=" * 50)

# 11)
print("Palíndromos")

def verify_palindromo(word):
    cleaned = word.replace(" ", "").lower()
    invert_word = cleaned[::-1]
    if cleaned == invert_word:
        print(f"A palavra \"{word}\" é um palíndromo")
    else:
        print(f"A palavra \"{word}\" não é um palíndromo")

verify_palindromo("Ana Ana")
verify_palindromo("1DSTB-SENAI")
verify_palindromo("Subi no Onibus")
print("=" * 50)

# 12)
print("Fatorial 3, 7, 9, 25, 26.")

def factorial(number):
    if number < 0:
        print("O número inserido é inválido! Digite um número positivo")
    else:
        result = 1
        for i in range(1, number + 1):
            result *= i
        print(f"O fatorial de {number} é: {result}")
        return result

factorial(3)
factorial(7)
factorial(9)
factorial(25)
factorial(26)
