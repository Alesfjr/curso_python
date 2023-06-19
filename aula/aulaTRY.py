'''
não é  desta maneira que se usa TRY E EXCEPT
'''
numero_str=input('Vou dobrar o numero que voce digitar:')



try :
    print('  STR:',numero_str)
    numero_int=float(numero_str)
    print('FLOAT:',numero_int)
    print(f'O dobro de {numero_str} é {numero_int*2}')

except:
    print('Isso não é um numero')