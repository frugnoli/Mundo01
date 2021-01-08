# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos
# quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado
dias = int(input("Quantos dias o alugados: "))
qtd_km = float(input("Quantos km rodados: "))
pago = (dias * 60) + (qtd_km * 0.15)
print("O total a pagar é R$ {:.2f}".format(pago))
