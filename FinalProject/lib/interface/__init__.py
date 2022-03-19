

def linha(tam = 42):
    return '-' * tam

def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m --- \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = readINT('Sua Opção: ')
    return opc



def leiaInt(msg):
    ok = False
    v = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            n = int(n)
            ok = True
        else:
            print('Erro. Digite um número inteiro.')
        if ok:
            break

#usando erros

def readINT(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('Erro, digite um número inteiro.')
        except (KeyboardInterrupt):
            print('Programa interrompido pelo usuário.')
        else:
            return n

def readFLOAT():
    while True:
        try:
            n = float(input('Digite um número: '))
        except (ValueError, TypeError):
            print('Erro, digite um número real.')
        except (KeyboardInterrupt):
            print('Programa interrompido pelo usuário.')
        else:
            return n

def readSTR(msg):
    while True:
        try:
            n = str(input(msg))
        except (ValueError, TypeError):
            print('Erro. Digite um nome.')
        except (KeyboardInterrupt):
            print('Programa interrompido pelo usuário.')
        else:
            return n