from FinalProject.lib.interface import *
from FinalProject.lib.arquivo import *

from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)


while True:
    resp = menu(['CADASTRAR PESSOAS', 'LISTAR PESSOAS', 'SAIR DO SISTEMA'])
    if resp == 1:
        print('OPÇÃO 1')
        cabeçalho('NOVO CADASTRO')
        nome = str(input('NOME:'))
        idade = readINT('IDADE:')
        cadastrarPessoas(arq,nome,idade)
    elif resp == 2:
        print('OPÇÃO 2')
        lerArquivo(arq)
    elif resp == 3:
        print('Programa encerrado.')
        break
    else:
        print('\033[31mPor favor, digite uma opção válida.\033[m')
    sleep(2)
