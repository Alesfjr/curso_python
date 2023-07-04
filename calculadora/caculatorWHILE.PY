

while True:
    n1=input('Digite um numero:')
    operador=input ('Digite um operador[/*+-]:')
    n2=input('Digite um outro numero :')

    numeros_validos=None
    n1_float=0
    n2_float=0
    try:
        n1_float=float(n1)
        n2_float=float(n2)
        numeros_validos=True

    except Exception as error:
    
        print(error)


    if numeros_validos is None:
        print('Um ou ambos os numeros digitados são invalidos')
        continue
    operadores_permitidos='/*+-'
    if operador not in operadores_permitidos:
        print('Operador invalido')

    if len(operador)>1:
        print('Digite um unico operador')
        continue
    print('Realizando calculo')
    if operador =='+':
        print(n1_float+n2_float)
    elif operador =='-':
            
        print(n1_float-n2_float)
    elif operador =='*':
            
        print(n1_float*n2_float)
    elif operador =='/':
            
        print(n1_float/n2_float)

    ######
    sair= input('Sair?[s]').lower().startswith('s')
    
    if sair is True:
        break