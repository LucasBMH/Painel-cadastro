def criararquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('falha ao criar arquivo')
    else:
        print(f'arquivo {nome} criado com sucesso')

def arquivoexiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def lerarquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('houve um erro ao ler o arquivo')
    else:
        print(a.read())

def cadastranome(nome = 'inválido'):
    n = input('nome')
    nome = n
    a = open('pessoas.txt', 'a')
    a.write(nome)
    a.close()


def cadastraidade(idade = 0):
    i = input('idade')
    idade = i
    a = open('pessoas.txt', 'a')
    a.write(f'{idade.rjust(20)} anos')
    a.write('\n')
    a.close()
    print(f'novo registro adicionado com sucesso')


def cadastranovo():
    n = input('nome')
    i = input('idade')
    nome = n
    idade = i
    a = open('pessoas.txt', 'a')
    a.write('{:<30}'.format(nome))
    a.write('{:>3} anos\n'.format(idade))
    a.close()
    print(f'novo registro {nome} adicionado com sucesso!')
