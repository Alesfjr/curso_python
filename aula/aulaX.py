a='A'
b='B'
c=56.6
string='a={0} b={0} c={nome3:.2f}'
formato=string.format(
    a,b,nome3=c
    ) # 'nome3' é um parametro dado para chamar a variavel
'''Dentro da função  format contem as variaveis em uma certa ordem  ,essas variaveis serão transportadas para os cochetes  na ordem designada
'''
print(formato)


nome=input('Qual seu nome?')
print(f'{nome}, seu nome foi coletado com sucesso!')

valor_1=int(
    input('Digite um numero:')
)
valor_2=int(
    input('Digite outro numero:')
)

print(f'{nome},a soma dos dois valores é de {valor_1+valor_2}')

#  MAS É MELHOR USAR PUTRO METODO 

nome1=input('Qual seu nome?')
print(f'{nome1}, seu nome foi coletado com sucesso!')

valor_3= input('Digite um numero:')

valor_4=input('Digite outro numero:')

int_valor_3=int(valor_3)
int_valor_4=int(valor_4)


print(f'{nome1},a soma dos dois valores é de {int_valor_3+int_valor_4}')


