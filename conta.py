class Conta:
    def __init__(self,numero, titular, saldo, limite, data_abertura):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        self.data_abertura = data_abertura

    def deposita(self, valor):
        self.saldo += valor

    def saca(self, valor):
        if(self.saldo < valor):
            print("Saldo insuficiente!")
            return False
        else:
            self.saldo -= valor
            print("Saque realizado!")
            return True
    
    def transfere_para(self, conta_destino, valor):
        retirou = self.saca(valor)
        if(retirou):
            conta_destino.deposita(valor)
            print("Transferência realizada!")
            return True
        else:
            print("Houve um problema ao tentar realizar a transferência!")
            return False            

    def extrato(self):
        print(f"-------- dados da conta -----------")
        print(f"conta {self.numero}\nextrato: {self.saldo}")
        print(f"data de criação: {self.data_abertura.dia}/{self.data_abertura.mes}/{self.data_abertura.ano}")
        print(f"-------- dados do cliente -----------")
        print(f"{self.titular.nome} {self.titular.sobrenome}\ncpf:{self.titular.cpf}")
            
    pass