#Escreva um programa que peça ao usuário para digitar um número inteiro positivo n. O programa deve então imprimir todos os números de 0 a n, indicando se cada número é par ou ímpar.

n = int(input("Escreva um número: "))
for i in range(n+1):
    print(i, end="")
    if (i%2 == 0):
        print ("- par")
    else:
        print("- ímpar")
    print("")