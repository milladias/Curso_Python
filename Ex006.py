# Crie um algoritimo que leia um número e mostre o seu dobro,triplo e raiz quadrada.
#Opção 1
n = int(input('Digite um número: '))
d = n * 2
t = n * 3
r = n **(1/2)
print('O dobro de {} é {}. \nO triplo de {} é {} \nÉ a raiz quadrada de {} é {:.2f}'.format(n, d, n, t, n, r))

#Opção 2
n = int(input('Digite um número: '))
print('O dobro de {} é {}. \nO triplo de {} é {}. \nÉ a raiz quadrada de {} é {:.2f}.'.format(n,(n*2), n,(n*3), n,(n**(1/2))))



