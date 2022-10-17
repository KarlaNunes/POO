from conta import Conta
from cliente import Cliente
from data import Data

data_01 = Data(17, 10, 2022)

cliente_01 = Cliente("Karla", "Julyana", "1234-5")

conta_1 = Conta('123-4', cliente_01, 120.0, 1000.0, data_01)

conta_1.extrato()



