repetir = str
while (repetir != "N") and (repetir != "n"):
    print("----------Calculadora----------")
    n1 = int(input("Escreva 1 número: "))
    operador = input("Escreva a operação a ser realizada (+, -, *, /): ")
    invalid_op = (operador != "+") and (operador != "-") and (operador != "*") and (operador != "/")
    while invalid_op:
        operador = input("Operação inválida! Escolha novamente (+, -, *, /): ")
        invalid_op = (operador != "+") and (operador != "-") and (operador != "*") and (operador != "/")
    n2 = int(input("Digite o 2° número: "))
    resultado = float

    if (operador == "+"):
        resultado = (n1 + n2)
    elif (operador == "-"):
        resultado = (n1 - n2)
    elif(operador == "*"):
        resultado = (n1 * n2)
    elif (operador == "/"):
        resultado = (n1 / n2)

    print("")
    print(f"O resultado da operação foi: {resultado}")
    print("")
    repetir = input(print("Deseja repetir a operação? (S/N): "))


print("Calculadora encerrada!")