dis = float(input('Digite a distância da viagem: '))
print('Você está prestes a começar uma viagem de {}Km!'.format(dis))
if dis <= 200:
    dis = dis * 0.50
    print('E o preço da sua passagem será de R${:.2f}'.format(dis))
else:
    dis = dis * 0.45
    print('E o preço da sua passagem será de R${:.2f}'.format(dis))
