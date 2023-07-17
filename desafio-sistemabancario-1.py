menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
    
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            
        else:
            print("A operação falhou! O valor informado é inválido!")

    elif opcao == "s":
        valor = float(input("Informe o valor de saque: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        
        if excedeu_saldo:
            print("Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("O valor do saque excedeu o limite.")

        elif excedeu_saques:
            print("O valor excedeu o numero de saques.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("O valor informado é inválido.")
    
    elif opcao == "e":
        print("==================== EXTRATO ====================")
        print("Não foram realizadas movimentações" if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=================================================")

    elif opcao == "q":
        break

    else:
        print("Operação invalida, por favor, selecione a operação desejada.")