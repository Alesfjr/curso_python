"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
'''senha='jujutsu'

for letra  in senha:
    letra=input('Digite a senha:')

    if letra in senha:
        print(letra)
    elif letra not in  senha:
        print('incoreto')

 '''
import os 

senha='jujutsu'
acerto=''
tentativas=0
while True:
    
    letra_dig=input('Digite uma letra:')
    tentativas+=1
    if len(letra_dig)>1:
      print('Digite uma unica letra')
      continue

    if letra_dig in senha:
        acerto+=letra_dig
    senha_formada=''
    for letra_senha in senha:
       if letra_senha in acerto:
          senha_formada+=letra_senha
        
       else:
           senha_formada += '*'
    print(senha_formada)

    if senha_formada == senha:
        
       print('Acesso permitido')
       print('Tentativas', tentativas)
       break


