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
