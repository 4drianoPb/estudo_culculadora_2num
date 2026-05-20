opçao = 0

print('------ Calculadora ------')  
n1 = float(input('Digite o primeiro número: '))
print('_-' * 14)
n2 = float(input('Digite o segundo número: '))
print('_-' * 14)

while opçao != 6:
    print('Digite a opção desejada: ')

    print('''    Soma [ 1 ]
    Multiplicação [ 2 ]
    Divisão [ 3 ]
    Subtraçao [ 4 ]
    Digitar novos números [ 5 ]
    Sair [ 6 ]''')
    
    opçao = int(input('Opção: '))

    if opçao == 1:
        print('-' * 20)
        print(f' {n1} + {n2} = {n1 + n2:.2f}')
        print('-' * 20)
    
    elif opçao == 2:
        print('-' * 20)
        print(f' {n1} X {n2} = {n1 * n2:.2f}')
        print('-' * 20)
    
    elif opçao == 3:
        print('-' * 20)
        print(f' {n1} ÷ {n2} = {n1 / n2:.2f}')
        print('-' * 20)
    

    elif opçao == 4:
        print('-' * 20)
        print(f' {n1} - {n2} = {n1 - n2:.2f}')
        print('-' * 20)

    elif opçao == 5:
        print('------ Digite os novos números ------')
        n1 = float(input('Digite o primeiro número: '))
        print('_-' * 14)
        n2 = float(input('Digite o segundo número: '))
        print('_-' * 14)

    else:
        print('-' * 45)
        print('Opção digitada é inválida, digite novamente...')
        print('-' * 45)

print('Você está saindo...')