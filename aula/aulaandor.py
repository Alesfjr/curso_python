entrada=input('[E]ntrar [S]air:')
senha=input('Senha:')
senha_permitida='123456'
#Tudo que esta entre parenteses sera exutado primeiro 
if (entrada == 'E' or entrada=='e') and senha==senha_permitida:
    print('Entrou')


else:
    print('Sair')

# O or sempre retornara o primeiro valor verdadeiro encontrado o resto sera descosiderado

   