print('Olá! Eu sou Berg um pequeno  sistema e muito limitado...')
test=input('Está preparado para minhas pergutas ?')

if test=='sim':
    print('Então,Vamos lá!')
else:
    print('Até mais pareiro')

nome=input('pode me falar seu nome?')
idade=int (input('pode me falar idade?'))

imp=input(f'{nome},posso tenta te impressiona?')
ano= 2023-idade

if imp=='sim':
    palpite=input(f'Você nasceu em {ano}?')
    
    if palpite =='sim':
        print('Afinal das contas, não sou tão ruim assim hehe')
    elif palpite=='nao'or 'não':
        tentativa1= ano+1
        tentativa2=ano-1
        print(f'Então,você nasceu entre {tentativa1} e {tentativa2}')
elif imp=='nao'or 'não':
     print('Ok,vamos continuar')
else:
    print('Ok,vamos continuar')


print(f'Bom {nome[::-1]} ,vamos continuar com as perguntas')
print('erro404')
print('tive um erro de calculo')
print(f'Bom {nome} ,vamos continuar com as perguntas hehe')


    
    


 

