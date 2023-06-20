"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
entrada=input('escreva um numero int:')

if entrada.isdigit():
    numero_int=int(entrada)
    if numero_int % 2 ==0:
        print( 'Este numero é par')

    else:
        print('Este numero é impar')
else:
    print('Este numero é float')