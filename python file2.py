#1
num = int(input("Insira um número: \n"))
if num % 2 == 0:
    print("Esse número é par")
else:
    print("Esse número é impar")

#2
num = int(input("Insira um número: \n"))
if num > 10:
    print("O número é maior que 10")
else:
    print("O número é menor que 10")

#3
#Pergunte ao usuário a sua idade e informe se ele é maior de idade (18 anos ou mais) ou menor de idade.
n = int(input("Digite sua idade: \n"))
if n > 18:
    print("Você é maior de idade")
else:
    print("Você é menor de idade")


#4
idade = int(input("Insira sua idade: \n"))
if idade < 16:
    print("Não tem voto")
elif 17 <= idade <=69:
    print("Voto obrigatório")
else:
    print("Voto não obrigatório")


#5
#Pergunte ao usuário para inserir um número e diga se é positivo, negativo ou zero.
n = int(input("Digite um número: \n"))
if n > 0:
    print("O número é positivo")
elif n == 0:
    print("O número é zero")
else:
    print("O número é negativo")


#6
nota = int(input("Digite sua nota: \n"))

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


#7
idade = int(input("Digite sua idade: \n"))
if idade < 13:
    print("Você possui desconto")

elif idade >= 13 and idade < 60:
    print("Você não possui desconto")
else:
    print("Você possui desconto")

#8
a = float(input('Primeiro lado: '))
b = float(input('Segundo  lado: '))
c = float(input('Terceiro lado: '))

if (a + b < c) or (a + c < b) or (b + c < a):
   print('Nao é um triangulo')
elif (a == b) and (a == c):
   print('Equilatero')
elif (a == b) or (a == c) or (b == c):
   print('Isósceles')
else:
   print('Escaleno')

#9
valor = float(input("Digite o valor total da sua compra em R$: \n"))
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
ano = int(input("Digite um ano: \n"))
if (ano%4==0 and ano%100!=0) or (ano%400==0):
    print("É bissexto")
else:
    print("Não é bissexto")

#11
peso = float(input("Insira seu peso em kg: \n"))
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


#12 Solicite ao usuário três números e diga se estão em ordem crescente, decrescente ou se são iguais.
n1 = int(input("Digite o primeiro número: \n"))
n2 = int(input("Digite o segundo número: \n"))
n3 = int(input("Digite o terceiro número: \n"))

if n1 < n2 and n2 < n3:
    print("Ordem crescente")

elif n1 > n2 and n2 > n3:
    print("O número é decrescente")

else:
    print("Os números são iguais")


#13
temperatura = float(input("Digite a temperatura: \n"))
if temperatura < 10:
    print("Frio")

elif temperatura >= 10 and temperatura < 25:
    print("Aconchegante")

elif temperatura >= 25 and temperatura < 40:
    print("Quente")

else:
    print("Muito quente")

#14
from datetime import datetime

data_input = input("Digite uma data no formato dd/mm/aaaa: \n")

data_formatada = datetime.strptime(data_input, "%d/%m/%Y").strftime("%Y-%m-%d")

print("A data formatada é:", data_formatada)

#15
import re

senha = input("Digite uma senha: \n")

if len(senha) < 8:
    print("Sua senha precisa ter pelo menos 8 caracteres. Tente novamente.")
elif not re.search(r"[A-Z]", senha):
    print("A senha deve conter pelo menos uma letra maiúscula. Por favor, adicione uma.")
elif not re.search(r"[a-z]", senha):
    print("A senha precisa de pelo menos uma letra minúscula. Tente incluir uma.")
elif not re.search(r"\d", senha):
    print("Você precisa adicionar pelo menos um número à sua senha.")
elif not re.search(r"[^A-Za-z0-9]", senha):
    print("Sua senha deve incluir pelo menos um caractere especial (como @, #, $, etc.).")
else:
    print("Senha criada com sucesso! Parabéns!")

#16
num = float(input("Digite um número: \n"))

if num < 0:
    print("Não é possível calcular a raiz quadrada de um número negativo.")
elif num > 100:
    print("Número muito grande, reduza para um valor abaixo de 100.")
else:
    raiz = num ** 0.5
    print(f"A raiz quadrada de {num} é {raiz:.2f}.")

#17
data = input("Escreva a data no seguinte formato (dd/mm/aaaa): \n")
partes = data.split("/")
dia = int(partes[0])
mes = int(partes[1])
ano = int(partes[2])

if mes < 1 or mes > 12:
    print("Mês inválido. O mês deve estar entre 1 e 12.")
else:
    if mes == 2:
        if (ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)):
            limite = 29
        else:
            limite = 28
    elif mes in [4, 6, 9, 11]:
        limite = 30
    else:
        limite = 31

    if dia < 1 or dia > limite:
        print(f"Dia inválido. O mês {mes} no ano {ano} tem no máximo {limite} dias.")
    else:
        print(f"{ano:04d}-{mes:02d}-{dia:02d}")

#18

expressao = input("Digite uma expressão matemática: \n")

resultado = eval(expressao)

print(f"O resultado da expressão é: {resultado}")

#19

import re

cpf = input("Digite o número do CPF no formato (XXX.XXX.XXX-XX): \n")
padrao_cpf = r"\d{3}\.\d{3}\.\d{3}\-\d{2}"
formato_valido = re.match(padrao_cpf, cpf)

if formato_valido:
    soma_first = (
        (int(cpf[0]) * 10) + (int(cpf[1]) * 9) + (int(cpf[2]) * 8) + (int(cpf[4]) * 7) +
        (int(cpf[5]) * 6)  + (int(cpf[6]) * 5) + (int(cpf[8]) * 4) + (int(cpf[9]) * 3) + (int(cpf[10]) * 2)) % 11

    soma_seccond = (
        (int(cpf[0]) * 11) + (int(cpf[1]) * 10) + (int(cpf[2]) * 9) + (int(cpf[4]) * 8) +
        (int(cpf[5]) * 7)  + (int(cpf[6]) * 6)  + (int(cpf[8]) * 5) +
        (int(cpf[9]) * 4)  + (int(cpf[10]) * 3) + (int(cpf[12]) * 2)) % 11

    if soma_first >= 2:
        digito1 = 11 - soma_first
    else:
        digito1 = 0

    if soma_seccond >= 2:
        digito2 = 11 - soma_seccond
    else:
        digito2 = 0

    if int(cpf[12]) == digito1 and int(cpf[13]) == digito2:
        print(f"O CPF {cpf} é válido!")
    else:
        print(f"O CPF {cpf} é inválido!")
else:
    print("O CPF não foi digitado corretamente! Tente novamente.")
