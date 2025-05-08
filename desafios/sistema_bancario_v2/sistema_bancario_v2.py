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