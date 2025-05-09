print("fatorial 3,7,9,25,26.")

def factorial(number):
    if number < 0:
        print(f"O número inserido é inválido! Digite um número positivo")
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
