"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome=input('Escreva seu nome:')

n_letras= len(nome)
if n_letras<=4:
    print('Seu nome é curto')
elif n_letras>=  5 and n_letras<= 6:
     print('Seu  nome é normal ')
elif n_letras>=7 :
    print('seu nome é muito grande')
else:
    print(' Nada foi escrito')