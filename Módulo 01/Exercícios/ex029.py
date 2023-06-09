vel = float(input('Qual a velocidade atual do carro? '))
if vel > 80:
    print('Multado! Você excedeu o limite permitido que é 80km/h')
    multa = (vel - 80) * 7
    print('Você deve pagar uma multa de R${:.2f}'.format(multa))
    
print('Tenho um bom dia! Dirija com segurança!')