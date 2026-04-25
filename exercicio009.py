# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar. Considere USS1.00 = 3.27.

dinheiro = float(input('Quanto dinheiro você tem no banco? '))

print(f'Com esse dinheiro você pode comprar {dinheiro / 3.27 :.2f} dólares. ')