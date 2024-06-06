#Escreva um programa que peça ao usuário para digitar números inteiros. O programa deve continuar pedindo números até que o usuário digite 0. Quando 0 for digitado, o programa deve imprimir a soma de todos os números digitados.

soma = 0 
n = int
while (n != 0):
    n = int(input("digite um número: "))
    if (n != 0):
        soma += n
    else:
        break

print("")
print(f"A soma total dos número foi: {soma}")
    