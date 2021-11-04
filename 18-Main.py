from ContasBanco import CartaoCredito, ContaCorrente
from Agencia import AgenciaPremium, AgenciaVirtual, AgenciaComum

# programa
conta_phillipe = ContaCorrente("Phillipe", "111.222.333-45", 1234, 34062)

cartao_phillipe = CartaoCredito('Phillipe',conta_phillipe)
cartao_phillipe2 = CartaoCredito('Phillipe',conta_phillipe)




agencia_virtual = AgenciaVirtual('www.AgenciaVirtual.com.br',22224444, 152000000000)
agencia_comum = AgenciaComum(98565874,120369874165)
agencia_premium = AgenciaPremium(98563258,112008999999)


agencia_premium.adicionar_cliente('Phillipe',985625474, 1000)

print(agencia_premium.clientes)