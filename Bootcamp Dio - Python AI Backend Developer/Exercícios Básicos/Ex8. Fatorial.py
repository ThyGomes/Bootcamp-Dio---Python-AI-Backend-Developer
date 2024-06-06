#Objetivo: Escreva um programa que peça ao usuário para digitar um número inteiro positivo e calcule o fatorial desse número.

n = int(input("Escreva um número: "))
print("")
fat = n

for i in range (n-1, 0, -1):
    fat *= i

print(f"O fatorial de {n} é: {fat}")