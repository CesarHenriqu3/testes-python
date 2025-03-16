dias = float(input("Dias alugados? "))
rodados = float(input("Quantos km rodados? "))
pagar = dias * 60
carro = rodados * 0.15
total = pagar + carro
print("O total a pagar é de R$",total)