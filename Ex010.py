# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
# Considere US$1,00 = R$3,27
#pção 1
n = float(input('Quanto dinheiro você tem na carteira? R$'))
print('Com R${} você pode comprar US${:.2f}'.format(n, n/3.27))

#Opção 2
real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real / 3.27
print('Com R${} você pode comprar US${:.2f}'.format(real,dolar))


