#Calculadora de IMC

peso = float(input('Qual o seu peso em kg?:'))
altura = float(input('Qual a sua altura em metros?:'))
imc = peso / altura**2
print('o seu imc é de {}'.format(imc))

if imc < 16:
    print('Magreza grave')
elif imc < 17:
    print('Magreza moderada')
elif imc < 18.5:
    print('Magreza leve')
elif imc < 25:
    print('Saudavel')
elif imc < 30:
    print('Sobrepeso')
elif imc < 35:
    print('Obesidade grau 1')
elif imc < 40:
    print('Obesidade grau 2 (Severa)')
else:
    print('Obesidade grau 3 (Mórbida)')