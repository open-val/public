# Limite de 3 saques diários
# Saques com limite de 500

# Saque e Depósito devem ser armazenados no Extrato
# Não pode contem valores negativos.

menu = """

[1] Depósito
[2] Saque
[3] Extrato
[0] Sair

"""
saldo = 0
limite_saque = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor que deseja depositar: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "2":
        valor = float(input("Informe o valor a ser sacado: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite_saque
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite diário.")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques atingido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque realizado no valor de: R$ {valor: .2f}\n"
            numero_saques += 1
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "3":
        print("\n ============= EXTRATO =============")
        print("Não foram realizados movimentações." if not extrato else extrato)
        print(f"\n Saldo: R$ {saldo: .2f}")
        print("====================================")
    elif opcao == "0":
        print("Encerrando atendimento... Obrigada por utilizar nossos serviços.")
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
