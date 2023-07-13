frase='Teria maior confiança no desempenho de um homem que espera ter uma grande recompensa do que no daquele que já a recebeu/Não devemos de forma alguma preocupar-nos com o que diz a maioria, mas apenas com a opinião dos que têm conhecimento do justo e do injusto, e com a própria verdade.'

i=0
qtd_apareceu_mais=0
letra_apareceu_mais_vezes=''
while i<len(frase):
    letra_atual=frase[i]
    if letra_atual==' ':
        i+=1
        continue

    quatas_vezes_letra_apareceu=frase.count(letra_atual)

    if qtd_apareceu_mais<quatas_vezes_letra_apareceu:

        qtd_apareceu_mais=quatas_vezes_letra_apareceu

        letra_apareceu_mais_vezes=letra_atual

    i+=1


  
    
print('A letra que apareceu mais vezes foi o '
    f'"{letra_apareceu_mais_vezes}",'
    f' que apareceu {qtd_apareceu_mais}x')