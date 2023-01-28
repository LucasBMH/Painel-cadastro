cores =(
    '\033[m',#0 sem cor
    '\033[:31m',#1 - vermelho
    '\033[:32m',#2 - verde
    '\033[:34m',#3 - azul
    '\033[7:30m' ,#4 - branco
)


def linha(tam=42):
    return '-'*tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except( ValueError, TypeError):
            print(f'{cores[1]}por favor digite um numero inteiro valido{cores[0]}')
            continue #volta para o while
        except (KeyboardInterrupt):
            print('Usuario preferiu não digitar o numero ')
            return 0
        else:
            return n


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{cores[2]} {c} - {cores[3]} {item} {cores[0]}')
        c += 1
    print(linha())
    opc = leiaint(f'{cores[4]}sua opção -> {cores[0]}')
    return opc
