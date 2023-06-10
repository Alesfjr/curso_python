nome =  input('qual seu nome?')
altura=float(input('qual sua altura?'))
peso=float(input('qual seu peso?'))
imc= peso//(altura*altura)

# o f antes da string serve para colocar variaveis dentro da string
print(f'{nome} tem {altura} de altura, pesa {peso} kg e seu imc é de {imc:.2f}') #.2f serve para reduzir oque vem depois da virgula

if imc<=18:
    print('Você esta abaixo do peso ')

elif imc >=18 and imc<=24:
    print('Peso normal')

elif imc>=25 and imc <= 29.9:
    print('Excessso de peso')

else:
    ...