import sys
import os

# Aluno: Mateus Aires

# Programa procura por uma função com determinado nome em um arquivo e retorna um booleano referente à existência ou não de tal função

# Pra executar: dentro da pasta com o programa arquivo "python3 search_function_in_file.py {nome da função} {nome do arquivo python}"


def valida(nome):
    if nome == None or len(nome) == 0:
        print("Nome inválido")
        sys.exit(1)


def valida_arquivo(nome_arquivo):
    valida(nome_arquivo)
    if not nome_arquivo.endswith(".py"):
        print("Arquivo não é do tipo .py")
        sys.exit(1)
    if not os.path.isfile(nome_arquivo):
        print("Arquivo inexistente")
        sys.exit(1)

# extrai o nome da função de uma sentença do tipo "def {nome da função}():"
def extrai_nome_funcao(string):
    split_string = string.split("(")
    return split_string[0][4::]

# procura o nome da função na linha e retorna um booleano

def procura_funcao(linha, nome_funcao):

    funcao_analisada = extrai_nome_funcao(linha)
    if funcao_analisada == nome_funcao:
        return True
    else:
        return False


# Lê linha por linha do arquivo até achar uma que começa com "def ", e então manda a linha para a função acima

def ler_arquivo(arquivo, nome_funcao):

    with open(arquivo, "r") as python_file:
        while True:
            line = python_file.readline()
            if not line:
                break
            if line.startswith("def "):
                match = procura_funcao(line, nome_funcao)
                if match == True:
                    return match

                continue

    return False


nome_funcao = sys.argv[1]
nome_arquivo = sys.argv[2]

valida(nome_funcao)
valida_arquivo(nome_arquivo)


print(ler_arquivo(nome_arquivo, nome_funcao))

