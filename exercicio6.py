"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
entrada=input('Digite a hora em numero int:')

try:
    hora=int(entrada)
    if hora >=0 and hora<=11:
        print('Bom dia')
    elif hora>11 and hora<=17:
        print('Boa tarde')
    elif hora>17 and hora<=23:
         print('Boa noite')
    else:
         print( 'Nada foi digitado')
         

except:
        print('Por favor digite numeros ineiros')

