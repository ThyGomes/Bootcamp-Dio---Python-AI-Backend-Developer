# Autor: Thyago Gomes - Estudante de Análise e Desenvolvimento de Sistemas (Uninter)
# Linkedin: https://www.linkedin.com/in/thyago-gomes-03325a2b4/
# GitHub: https://github.com/ThyGomes 
# Instagram: @thyag.0

# Desafio 1 - Bootcamp Dio - Python AI Backend Developer
# Sistema bancário simples com as seguintes funções: depósito, saque (limite de 3 saques diários, e R$500,00 por saque) e visualizar extrato

##############################################################################################################################################



#Menu inicial
print("""
_______________          Bem vindo ao Banco Sonserina!          _________________
                      A nova era da moeda digital Python!      

Limites de saque diário: 3
Limites por saque: P$ 500,00 pythons
      
-----------------------           MENU INICIAL          -------------------------

1 - Depositar
2 - Sacar
3 - Verificar Extrato
4 - Sair
""")


# Variáveis
operacao = 0
#
deposito = 0
extrato_depositos = []
#
saque = 0
extrato_saques = []
#
saldo = 0 


# O Seguinte looping se repetirá até que o usuário saia do programa digitando 4
# Enquanto isso ele poderá realizar as operações de depositar, sacar e verificar extrato por repetidas vezes
while (operacao != 4):
    print("________________________________________________________________________________")
    print()
    operacao = int(input("Digite outra operação que deseja realizar (1/2/3/4): "))
    print()


    # Depositar
        # Usuário insere o valor do depósito, que então é incrementado no saldo
        # Após isso a lista "extrato_depositos" armazenará os valores depositados, para este e outros depósitos
        # No final aparecerá a confirmação da operação e o saldo atual do usuário
    if (operacao == 1):
        deposito = float(input("Favor, digite o valor que deseja depositar: "))
        saldo += deposito 
        extrato_depositos.append(deposito)
        print(f"Operação realizada com sucesso! Saldo atual: P$ {saldo:.2f} pythons") 
        
    
    # Sacar
        # O usuário insere o valor que deseja sacar
        # Se o valor do saque for maior que o saldo, ou o limite de saques diários (3) tenha sido atingido, ou o valor do saque seja maior que 500, o saque não acontecerá, aparecendo mensagens de erro específicas pra cada caso (Saldo insuficiente, Limites de saque atingido)
        # Obs: o limite de saques diários é contado com base no tamanho da lista que armazena os saques, "extrato_saques"
        # Senão:
            # O valor do saque será descontado do saldo
            # A lista "extrato_saques" armazenará os saques realizados
            # Por fim aparecerá a confirmação da operação na tela e o saldo atual do usuário 
    elif (operacao == 2):
        saque = float(input("Favor, digite o valor que deseja sacar: "))
        if (saque > saldo):
            print(f"Saldo insuficiente! Não foi possível realizar o saque! Seu saldo atual é de: P$ {saldo:.2f} pythons")
        elif (len(extrato_saques) == 3):
            print("Ops! Limite de saque diário atingido, tente novamente amanhã!")
        elif (saque > 500):
            print("Ops! Não foi possível concluir a operação. O limite por saque é P$ 500,00! Favor tente novamente")
        else:
            saldo -= saque
            extrato_saques.append(saque)
            print(f"Operação realizada com sucesso! Seu saldo atual é de: P$ {saldo:.2f} pythons")
    

    # Verificar Extrato
    # Apresenta os valores de Saque e Depósito armazenados nas variáveis "extrato_saques" e "extrato_depositos" e também o saldo atual do usuário
    elif (operacao == 3):   
        print("Depósitos realizados:")
        for i in range (len(extrato_depositos)):
            print(f"{extrato_depositos[i]:.2f}"
                  )
        print()
        print("Saques realizados:")
        for i in range (len(extrato_saques)):
            print(f"{extrato_saques[i]:.2f}"
                  )
        print()
        print(f"Saldo atual: P$ {saldo:.2f} pythons")
    

    # Caso o usuário não digite uma operação válida (1/2/3/4) o programa fará uma nova solicitação até que ele digite uma opção válida
    else: 
        operacao = int(input("Operação inválida! Favor digite novamente (1/2/3/4): "))
        print()
        continue
    


print("________________________________________________________________________________")
print()
print("Programa encerrado! Tenha um bom dia, boa tarde, boa noite!")
# ~ "O Show de Truman" ;)