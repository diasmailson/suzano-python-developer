from datetime import datetime, date
from abc import ABC, abstractmethod, property


class Cliente:
    def __init__ (self, endereco, contas):
        self._endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
       transacao.registrar(conta)
    
    def adicionar_conta(self, conta):
        self.contas.append(conta)
            
    
class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._cpf = cpf


class Conta:
    
    def __init__ (self,numero, cliente, Historico):
        self._saldo = 0
        self._numero = numero
        self._agencia = "1100"
        self._cliente = cliente 
        self._historico = Historico()
    
    def saldo(self):
        return self.saldo

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(0, numero, cls._agencia, cliente, "Conta criada com sucesso")
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo
        
        if excedeu_saldo:
            print("Saldo insuficiente")
            
        elif valor > 0:
            self.saldo -= valor
            print(f"Saque realizado com sucesso")
            return True
        else:
            print("O valor informado é inválido")
            
        return False

    def depositar(self, valor: float):
        if valor > 0:
            self.saldo += valor
            print(f"Deposito realizado com sucesso")            
        else:
            print("O valor informado é inválido")
            return False
        
        return True

class ContaCorrente(Conta): 
    def __init__(self, numero, cliente, limite = 500, limite_saques = 3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques
    
    def sacar(self, valor):
        numero_saques = len([transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__])

        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saques

        if excedeu_limite:
            print("Limite de saque excedido")            

        elif excedeu_saques:
            print("Limite de saques excedido")           
    
        else:
            return super().sacar(valor)

        return False
    
    def __str__(self):
        return f"Agencia: {self.agencia}, Conta Corrente: {self.numero},  Cliente: {self.cliente._nome}"
  

class Historico:
    def __init__(self):
        self._transacoes = []
    
    @property
    def transacoes(self):
        return self._transacoes
    
    def adicionar_transacao(self, transacao):
        self.transacoes.append({
            "tipo": transacao.__class__.__name__,
            "valor": transacao.valor,
            "data": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        })


class Transacao(ABC):
    @property
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass


class Saque:
    def __init__(self, valor):
        self._valor = valor
    
    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


class Deposito:
    def __init__(self, valor):
        self._valor = valor
    
    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)
   
