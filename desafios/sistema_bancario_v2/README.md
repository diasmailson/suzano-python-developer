# 💰 Sistema Bancário em Python

Este é um projeto simples de sistema bancário desenvolvido em Python como parte de um desafio de programação. O sistema permite realizar operações básicas como **depósito**, **saque**, **consulta de extrato**, além de funcionalidades para **gerenciar usuários e contas bancárias**.

## 📌 Funcionalidades

- **Depositar**: Permite adicionar dinheiro à conta.
- **Sacar**: Permite realizar saques com limite por valor e por quantidade diária.
- **Extrato**: Exibe o histórico de transações e o saldo atual.
- **Novo Usuário**: Cadastro de novos usuários com CPF, nome, data de nascimento e endereço.
- **Nova Conta**: Criação de contas vinculadas a usuários já cadastrados.
- **Listar Contas**: Exibe a lista de contas cadastradas.
- **Sair**: Encerra o sistema.

## 🛠️ Tecnologias utilizadas

- Python 3
- Estruturas básicas como listas e dicionários
- Funções com parâmetros posicionais e nomeados
- Manipulação de strings e entrada de dados

## ▶️ Como usar

1. Clone o repositório ou copie o código para um arquivo `sistema_bancario.py`.
2. Execute o script:

```bash
python sistema_bancario.py
```

3. Use o menu interativo para navegar pelas funcionalidades do sistema.

---

## 📋 Exemplo de Menu

```
================ MENU ================
[d]	Depositar
[s]	Sacar
[e]	Extrato
[nc]	Nova conta
[lc]	Listar contas
[nu]	Novo usuário
[q]	Sair
=> 
```

## 📌 Regras de negócio

- Limite de **R$ 500,00** por saque.
- Máximo de **3 saques** por dia.
- Depósitos e saques devem ter valor maior que zero.
- CPF deve ser único por usuário.
