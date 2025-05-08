import textwrap

def menu():
    menu = """
================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))


def depositar(saldo, valor, extrato, /):    
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n === Depósito realizado com sucesso! ===" \
        "")
    else:
        print("\n @@@Valor inválido. Insira um valor maior que zero. @@@")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saque):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saque

    if excedeu_saldo:
        print("\n @@@ Saldo insuficiente! @@@")
    elif excedeu_limite:
        print("\n @@@ O valor máximo para saque é de R$ 500.00 @@@")
    elif excedeu_saques:
        print("\n @@@ Número máximo de saques diários atingido! @@@")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1  
    else:
        print("\n @@@ Valor inválido. Insira um valor maior que zero. @@@")
    return saldo, extrato 

def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n @@@ Já existe usuário com esse CPF! @@@")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")  
    endereco = input("Informe o endereço (logradouro, número - bairro - cidade/UF): ")  

    usuarios.append({
       "nome": nome,
       "data_nascimento": data_nascimento,
       "cpf": cpf,
       "endereco": endereco
    })
    print("\n === Usuário cadastrado com sucesso! ===")

def filtrar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario
    return None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n === Conta criada com sucesso! ===")
        return {
            "agencia": agencia,
            "numero_conta": numero_conta,
            "usuario": usuario
        }
    else:
        print("\n @@@ Usuário não encontrado. @@@")  

def listar_contas(contas):
    if not contas:
        print("\n @@@ Não há contas cadastradas. @@@")
        return

    for conta in contas:
        linha = f"""Agência:\t{conta['agencia']}
        Número da conta:\t{conta['numero_conta']}
        Titular:\t{conta['usuario']['nome']}
        CPF:\t{conta['usuario']['cpf']}
        Endereço:\t{conta['usuario']['endereco']}
        Data de nascimento:\t{conta['usuario']['data_nascimento']}"""

        print("=" * 100)
        print(textwrap.dedent(linha))
        print("=" * 100)   

def main():
    AGENCIA = "0001"
    
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    limites_saques = 3
    usuarios = []
    contas = []

    while True:
        opcao = menu()
        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)
        
        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            
            saldo, extrato = sacar(saldo = saldo, valor = valor, extrato = extrato, limite = limite, numero_saques = numero_saques, limite_saque = limites_saques)               
        
        elif opcao == "e":
            exibir_extrato(saldo, extrato = extrato)
       
        elif opcao == "nu":
           criar_usuario(usuarios)
       
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
                print("\n === Conta criada com sucesso! ===")
        
        elif opcao == "lc":
            listar_contas(contas)
        
        elif opcao == "q":
            print("Obrigado por usar o sistema! Até logo.")
            break
        else:
            print("Opção inválida! Por favor, selecione uma opção válida.")

main()