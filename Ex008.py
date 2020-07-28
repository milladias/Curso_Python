#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milimetros.
m = float(input('Digite uma distância em metros: '))
cm = m * 100
mm = m * 1000
print('A medida de {}m corresponde a {}cm e {}mm'.format(m, cm, mm))

#Opção 2

m = float(input('Digite uma distância em metros: '))
mm = m * 1000
cm = m *100
dm = m * 10
dam = m / 10
hm = m / 100
km = m / 1000
print('A medida de {} corresponde a \n{}mm \n{}cm \n{}dm \n{}dam \n{}hm \n{}km'.format(m, mm, cm, dm, dam, hm, km))







