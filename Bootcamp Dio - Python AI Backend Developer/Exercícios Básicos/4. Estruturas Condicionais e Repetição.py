valor = int(input("Digite um valor: "))

if (valor >= 100): 
    print ("Valor suficiente")
else:
    print ("Valor insuficiente")

saldo = 1000
saque = 500
Status = "Sucesso!" if saldo >= saque else "Falha!"
print(Status)

palavra = "python"
for letra in palavra:
    print(letra)

frase = "Lógica de Programação e Algoritmos"
for i in range(0, len(frase), 1):
    print(frase[i], end="")
print("")

frutas = ["maça", "banana", "laranja"]
for fruta in frutas:
    print(fruta)