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
        pass

    elif opcao == '2':  # Sacar
        pass

    elif opcao == '3':  # Extrato
        pass

    elif opcao == '0':  # Sair
        break

    else:
        print("Opção inválida, gentileza escolher a operação desejada.")
