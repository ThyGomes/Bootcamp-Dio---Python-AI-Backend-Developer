#Objetivo: Escreva um programa que peça ao usuário para digitar um número inteiro positivo e determine se o número é primo ou não.

n = int(input("Digite um número: "))
print("")
div = 0

for i in range (1, n):
    if (n%i == 0):
        div += 1

if (div > 2):
    print(f"{n} não é um número primo")
else:
    print(f"{n} é um número primo")