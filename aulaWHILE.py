"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
condicao=True
while condicao:
    nome=input('qual o seu nome?')
    print(f'Esse é o seu nome:{nome}')
    if nome == 'sair':
        break

print('Acabou')

contador=0

while contador<10:
    #esse tipo de atribuição tb funciona para strings
    contador+=3
    print(contador)

print('acabou')







