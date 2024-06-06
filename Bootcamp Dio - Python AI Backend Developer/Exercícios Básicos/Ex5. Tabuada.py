#Escreva um programa que peça ao usuário para digitar um número inteiro positivo. O programa deve imprimir a tabuada desse número de 1 a 10.

n = int(input("Digite um número: "))
print("")

for i in range(1, 11):
    print(n*i, end=", ")
