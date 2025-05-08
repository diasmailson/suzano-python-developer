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