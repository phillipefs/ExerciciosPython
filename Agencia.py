from random import randint


class Agencia:
    def __init__(self, telefone, cnpj, numero):
        self.telefone = telefone
        self.cnpj = cnpj
        self.numero = numero
        self.clientes = []
        self.caixa = 0
        self.emprestimos = []


    def verificar_caixa(self):
        if self.caixa < 1000000:
            print(f'Caixa abaixo do nível recomendado. Caixa atual: {self.caixa}')
        else:
            print(f'O valor de caixa esta OK. Caixa atual: {self.caixa}')

    def emprestar_dinheiro(self, valor, cpf, juros):
        if self.caixa > valor:
            self.emprestimos.append((valor, cpf, juros))
        else:
            print('Emprestimo não é possível. Dinheiro não disponível em caixa')

    def adicionar_cliente (self, nome, cpf, patrimonio):
        self.clientes.append((nome, cpf, patrimonio))


class AgenciaVirtual(Agencia):
    def __init__(self, site, telefone, cnpj):
        self.site = site
        super().__init__(telefone, cnpj, 1000)
        self.caixa = 1000000
        self.caixa_paypal = 0
    
    def depositar_paypal(self, valor):
        self.caixa -=valor
        self.caixa_paypal += valor

    def sacar_paypal(self, valor):
        self.caixa_paypal -= valor
        self.caixa += valor

class AgenciaComum(Agencia):
    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, numero=randint(1000,9999))
        self.caixa = 1000000

class AgenciaPremium(Agencia):
    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, numero=randint(1000,9999))
        self.caixa = 10000000

    def adicionar_cliente(self, nome, cpf, patrimonio):
        if patrimonio > 1000000:
            super().adicionar_cliente(nome, cpf, patrimonio)
        else:
            print('O Cliente não tem patrimônio necessário para entrar na agência premium')

if __name__ == '__main__':

    agencia_virtual = AgenciaVirtual('www.AgenciaVirtual.com.br',22224444, 152000000000)
    agencia_comum = AgenciaComum(98565874,120369874165)
    agencia_premium = AgenciaPremium(98563258,112008999999)


    agencia_premium.adicionar_cliente('Phillipe',985625474, 1000)

    print(agencia_premium.clientes)