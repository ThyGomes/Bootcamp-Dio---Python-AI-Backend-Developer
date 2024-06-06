#dê um núemro ao programa, e ele mostrará quais números primos existem entre 0 e o número dado

n = int(input("Digite um número: "))
print("")
div = 0

print(f"Lista de números primos existentes entre 1 e {n}:")
for i in range (1, n+1):
    for a in range (1, i+1):
        if (i%a == 0):
            div += 1
    if (div == 2):
        print(i, end = ", ")
    div = 0

