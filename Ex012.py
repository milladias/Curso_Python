# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
p1 = float(input('Qual é o preço do produto? R$'))
p2 = p1 - (p1 *5 / 100)
print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'. format(p1, p2))






