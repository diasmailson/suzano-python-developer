menu = """

 [1] Depositar
 [2] Sacar
 [3] Extrato
 [0] Sair

"""
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUE = 3

# print (f"voce selecionou {opcao}")

while True:

    opcao = input(menu)

    if opcao == '1':  # Depositar
        valor_deposito = float(input("Informe o valor de depósito: R$ "))

        if valor_deposito > float(0):
            saldo += valor_deposito
            extrato += f"Depósito: R$ {valor_deposito:.2f}\n"

        else:
            print("Srª Cliente, insira valores maior que zero.")

    elif opcao == '2':  # Sacar
        EXCEDEU_SAQUE = numero_saques < LIMITE_SAQUE

        valor_saque = float(input("Informe o valor de Saque: R$ "))

        if valor_saque > float(500):
            print(
                "O valor máximo permitido para saque é de R$ 500.00. Por favor, insira outro valor.")

        elif valor_saque > saldo:
            print(
                "Sr(a) Cliente, não será possível sacar o dinheiro por falta de saldo na conta.")

        elif valor_saque > 0 and EXCEDEU_SAQUE:
            saldo -= valor_saque
            extrato += f"Saque: R$ {valor_saque:.2f}\n"
            numero_saques += 1

        elif numero_saques > EXCEDEU_SAQUE:
            print("Número de saques excedidos. São apenas 3 saques diários.")

        else:
            print("Valor inválido. Insira um valor maior que zero.")

    elif opcao == '3':  # Extrato
        pass

    elif opcao == '0':  # Sair
        break

    else:
        print("Opção inválida, gentileza escolher a operação desejada.")
