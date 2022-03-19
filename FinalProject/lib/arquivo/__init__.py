
from FinalProject.lib.interface import *

cadastro = {}

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close
    except:
        print('Houve um erro na criação do arquivo.')
    else:
        print(f'Arquivo {nome} criado com sucesso.')

def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo.')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        print(a.read())
    finally:
        a.close()

def cadastrarPessoas(arq, nome='desconhecido',idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um erro na abertura do arquivo.')
    else:
        try:
            a.write(f'{nome:<30} {idade:>3} anos\n')
        except:
            print('Houve um erro no cadastro.')
        else:
            print(f'Novo cadastro de {nome} efetuado com sucesso.')
            a.close()




