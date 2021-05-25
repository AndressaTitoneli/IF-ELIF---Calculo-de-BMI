# If Elif Calculadora IMC

'''
Qual é a seua Altura em cm:
Qual é o seu peso em kg:
1. Verificar o calculo IMC
2. código da formula 
3. If, Elif, Else
'''

# Menor que 18,5 Magreza
# Entre 18,5 e 24,9 Normal
# Entre 25,0 e 29,9 Sobrepeso
# Entre 30,0 e 39,9 Obesidade
# Maior que 40,0 Obesidade Grave


altura = float(input('Qual é a seua Altura em cm:'))
peso = float(input('Qual é o seu peso em kg:'))


IMC = peso / (altura/100)**2
#print(IMC)

if IMC < 18.5:
    print('Magreza')

elif IMC >= 18.5 and IMC < 24.9:
    print('Normal')

elif IMC >= 25.0 and IMC < 29.9:
    print('Sobrepeso')

elif IMC >= 30.0 and IMC < 39.9:
    print('Obesidade')

else:
    print('Obesidade grave!')


