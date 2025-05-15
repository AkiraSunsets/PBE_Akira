'''
num = int(input("Insira um número: "))
if num % 2 == 0:
    print("Esse número é par")
else:
    print("Esse número é impar")


num = int(input("Insira um número: "))
if num > 10:
    print("O número é maior que 10")
else:
    print("O número é menor que 10")


idade = int(input("Insira sua idade: "))
if idade < 16:
    print("Não tem voto")
elif 17 <= idade <=69:
    print("Voto obrigatório")
else:
    print("Voto não obrigatório")


nota = int(input("Digite sua nota: "))

if nota >= 9 and nota < 10:
    print("A")

elif nota >= 7 and nota < 9:
    print("B")

elif nota >= 5 and nota < 7:
    print("C")

elif nota >= 3 and nota < 5:
    print("D")

elif nota >= 0 and nota < 3:
    print("E")

else:
    print("Nota fora do intervalo")



idade = int(input("Digite sua idade: "))
if idade < 13:
    print("Você possui desconto")

elif idade >= 13 and idade < 60:
    print("Você não possui desconto")
else:
    print("Você possui desconto")



a = float(input('Primeiro lado: '))
b = float(input('Segundo  lado: '))
c = float(input('Terceiro lado: '))

# Testando se é triângulo
if (a + b < c) or (a + c < b) or (b + c < a):
   print('Nao é um triangulo')
elif (a == b) and (a == c):
   print('Equilatero')
elif (a == b) or (a == c) or (b == c):
   print('Isósceles')
else:
   print('Escaleno')

#9
valor = float(input("Digite o valor total da sua compra em R$: "))
if valor < 100:
    desconto = 0.05
    print("Você possui 5% de desconto")

elif valor >= 100 and valor < 500:
    desconto = 0.10
    print("Você possui 10% de desconto")

else:
    desconto = 0.15
    print("Você possui 15% de desconto")

valor_desconto = valor * desconto
valor_final = valor - valor_desconto

print(f"Desconto: R$ {valor_desconto:.2f}")
print(f"Valor final a pagar: R$ {valor_final:.2f}")


#10
ano = int(input("Digite um ano: "))
if (ano%4==0 and ano%100!=0) or (ano%400==0):
    print("É bissexto")
else:
    print("Não é bissexto")

#11
peso = float(input("Insira seu peso em kg: "))
altura = float(input("Insira sua altura em metros: "))
imc = peso / (altura ** 2)

if imc < 18.5:
    print("Abaixo do peso")

elif imc >= 18.5 and imc <= 24.9:
    print("Peso Normal")

elif imc >= 25 and imc <= 29.9:
    print("Sobrepeso")

else:
    print("Obesidade")



#12
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))

if



#13
temperatura = float(input("Digite a temperatura: "))
if temperatura < 10:
    print("Frio")

elif temperatura >= 10 and temperatura < 25:
    print("Aconchegante")

elif temperatura >= 25 and temperatura < 40:
    print("Quente")

else:
    print("Muito quente")

'''

data =
