print (1+ 10 + 49320)
print (1.5 + 3 )
print(0)
print (True)
print ("Python")

int()
str()
float()
bool()

nome, idade = "Guilherme", 28
print(nome, idade)

limite_saque_diário = 1000
print(limite_saque_diário)

BRAZILIAN_STATES = ["SP", "RJ", "SC"]
print(BRAZILIAN_STATES)


#Convertendo tipos
valor = 10
preco = 10.0
taxa = "20"

print (float(valor))
print (int(preco))
print (int(taxa))
print (int(taxa) + preco)
print (str(valor) + taxa)

print(type(valor))
print(type(preco))
print(type(taxa))

print(valor//2)
print(valor/2)


nome = input("Informe o seu nome: ")
idade = input("Informe sua idade ")
print (nome, idade, sep=", ")