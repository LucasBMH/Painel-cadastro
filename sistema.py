from lib.interface import *
from lib.arquivo import *  
from time import sleep
arq = 'pessoas.txt'

if not arquivoexiste(arq): # se o arquivo nao existe , criar
    criararquivo(arq)

while True:
    resposta = menu(['ver pessoas cadastradas ','cadastrar nova pessoa','sair do programa'])
    if resposta == 1:
        cabeçalho('VER PESSOAS CADASTRADAS')
        lerarquivo(arq)
    elif resposta == 2:
        cabeçalho('CADASTRAR NOVA PESSOA')
        cadastranovo()
    elif resposta == 3:
        cabeçalho('SAINDO DO PROGRAMA , ATÉ LOGO')
        break
    else:
        print('\033[31mERRO , digite algo válido\033[m')
    sleep(1)
