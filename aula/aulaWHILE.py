"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
'''condicao=True
while condicao:
    nome=input('qual o seu nome?')
    print(f'Esse é o seu nome:{nome}')
    if nome == 'sair':
        break

print('Acabou')
'''
'''contador=0

while contador<100:
    #esse tipo de atribuição tb funciona para strings
    contador+=10
    if contador ==50:
        print('Não vou mostrar o 50')
        #continue pula o que foi indicado pelo if 
        continue
    
    if contador == 40:
        print('Não vou mostrar o ',contador)
        continue
        
    print(contador)
    #Forçando a parada o while
    if contador==60:
        break
print('acabou')
'''
qtd_linhas=5
colunas=5

linhas=1

while linhas <= qtd_linhas:

    coluna=1
    while coluna<=colunas:
        
        print(f'{linhas=}, {coluna=}')
        coluna += 1
    linhas += 1

print('Acabou')





