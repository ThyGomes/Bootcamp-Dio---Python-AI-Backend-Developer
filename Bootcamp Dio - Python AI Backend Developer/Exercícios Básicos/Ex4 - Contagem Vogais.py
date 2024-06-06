#Objetivo: Escreva um programa que peça ao usuário para digitar uma frase. O programa deve contar e imprimir o número de vogais (a, e, i, o, u) na frase. 

frase = input("Escreva uma frase: ")
print("")
n_vogais = 0

for i in range (0, len(frase)):
    if (frase[i] == "a") or (frase[i] == "e") or (frase[i] == "i") or (frase[i] == "o") or (frase[i] == "u"):
        n_vogais += 1

print (f"A quantidade de vogais na frase é: {n_vogais}")

