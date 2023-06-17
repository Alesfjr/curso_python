nome=input('Qual o seu nome?')
idade=input('Qual a sua idade?')

if nome and idade:
    print(f'Seu nome é {nome} ')
    print(f'Seu nome invertido é {nome[::-1]}')
    if '' in nome: 
        print(f'Seu nome contem   espaços')
    else:
        print('Seu nome não tem espaços')
    
    print(f'Seu nome tem letras {len(nome)}')
    print(f'A ultima letra do seu nome é {nome[-1]}')

else :
    print('Desculpe, você deixou campos vazios')
