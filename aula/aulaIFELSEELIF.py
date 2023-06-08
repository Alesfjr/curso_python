#if/elif    /else
#se/e não se/ se não 
#As condições estao sempres acompanha das de variaveis e boolean 
# 

'''entrada= input('Você quer "entrar" ou "sair"?') 

if entrada=='entrar':  
    print("Bem vindo ao sistema")

elif entrada=="sair":
    print('Log Out concluido')
    print('Até a proxima ')

else:
    print('Você não digitou nem "entrar" e nem "sair"')
    '''
'''condicao1 = False
condicao2 = False
condicao3 = True
condicao4 = True

if condicao1:
    print('Código para condição 1')
    print('Código para condição 1')
elif condicao2:
    print('Código para condição 2')
elif condicao3:
    print('Código para condição 3')
elif condicao4:
    print('Código para condição 4')
else:
    print('Nenhuma condição foi satisfeita.')

if 10 == 10:
    print('Outro if')

print('Fora do if')
'''
print('Para entrar no sistema é preciso de nos indique algumas informações' )

nome =input('Nome:')
sobrenome =input('Sobrenome:')
idade=int(input('idade:'))
confirme =1 or 0
if idade>=18:
    raca=input('Raça:')

else:
    print('Você não tem a iadde adequada')
    print('Volte quando tiver 18 anos ')

    confirme=input('Podemos confirmar suas informações?(digite "1" para sim  ou "0" para não):')


if confirme==1:
     print(f'Nome:{nome}')
     print(f'Sobrenome:{sobrenome}')
     print(f'Idade;{idade}')
     print(f'Raça:{raca}')

elif confirme==0:
    print('Saida')

else:
    print('Não entendi')



       



