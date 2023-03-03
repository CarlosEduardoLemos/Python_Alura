class ContaCorrente:
    def __init__(self, numero, titular, saldo, limite):
        print(f"Construindo objeto ... {self}")
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite


    def extrato(self):
        print(f"Saldo {self.__saldo} do titular {self.__titular}")


    def deposita(self, valor):
        self.__saldo += valor


    def saca(self, valor):
        self.__saldo -= valor


    def trasnfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)