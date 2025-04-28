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
        pass

    elif opcao == '3':  # Extrato
        pass

    elif opcao == '0':  # Sair
        break

    else:
        print("Opção inválida, gentileza escolher a operação desejada.")
