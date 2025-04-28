# Sistema Bancário Simples em Python

Projeto desenvolvido durante o **Bootcamp Suzano - Python Developer**.  
O sistema simula operações bancárias básicas utilizando a linguagem **Python**.

## 🔥 Funcionalidades

- Realizar **depósitos**.
- Realizar **saques** (com limites).
- Visualizar o **extrato** das operações.

## 📋 Regras de Negócio

### Depósito

- Não é permitido depositar valores menores ou iguais a R$0,00.

### Saque

- Limite de **3 saques diários**.
- Valor máximo de **R$500,00** por saque.
- Não é possível sacar mais do que o saldo disponível.

## 🛠️ Tecnologias

- **Python 3.x**
- Execução via **terminal** (linha de comando).

## 🚀 Como executar

1. Certifique-se de ter o **Python** instalado na máquina.
2. Baixe ou clone este repositório.
3. Execute o arquivo principal:

```bash
python sistema_bancario.py
```

## 📌 Observações

- As operações são armazenadas apenas em memória (não há banco de dados ou arquivos).
- O controle de saques diários é válido enquanto o programa estiver em execução.
