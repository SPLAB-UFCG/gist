import sys
import os

# Aluno: Mateus Aires

# Programa procura por uma função com determinado nome em uma pasta de arquivos e imprime uma lista de combinações completas e/ou parciais entre o nome procurado e as funções achadas

# Pra executar: dentro da pasta com o programa e o diretório de arquivos a ser iterado digite "python3 search_function_in_directory.py {nome da função} {nome do diretório}"

# Observações:
# * o programa não quebrará com outros arquivos ou programas .py vazios, mas provavelmente quebrará se a sintaxe dos programas não estiver correta
# * o critério de determinação de uma combinação parcial será se o nome procurado for uma substring do nome de função achado ou o contrário

def valida(nome):
    if nome == None or len(nome) == 0:
        print("Nome inválido")
        sys.exit(1)


def valida_diretorio(nome_diretorio):
    valida(nome_diretorio)
    if not os.path.isdir(nome_diretorio):
        print("Diretório inexistente")
        sys.exit(1)

# extrai o nome da função de uma sentença do tipo "def {nome da função}():"
def extrai_nome_funcao(string):
    split_string = string.split("(")
    return split_string[0][4::]

# procura o nome da função na linha e retorna:
#   2 se for uma combinação completa
#   1 se for uma combinação parcial
#   0 se não houver combinação

def procura_funcao(linha, nome_funcao):

    funcao_analisada = extrai_nome_funcao(linha)
    if funcao_analisada == nome_funcao:
        return 2
    elif nome_funcao in funcao_analisada or funcao_analisada in nome_funcao:
        return 1
    else:
        return 0


# Lê linha por linha até achar uma que começa com "def ", e então manda a linha para a função acima
# Obs.: o uso do boolean é para assegurar que o programa continue procurando por uma combinação completa e, se não achar, retorne como uma combinação parcial

def ler_arquivo(arquivo, nome_funcao):

    partial_match = False

    with open(arquivo, "r") as python_file:
        while True:
            line = python_file.readline()
            if not line:
                break
            if line.startswith("def "):
                match = procura_funcao(line, nome_funcao)
                if match == 2:
                    return 2
                elif match == 1:
                    partial_match = True
                continue

    if partial_match:
        return 1
    else:
        return 0


nome_funcao = sys.argv[1]
nome_diretorio = sys.argv[2]

valida(nome_funcao)
valida_diretorio(nome_diretorio)

full_match = []
partial_match = []

for arquivo in os.listdir(nome_diretorio):
    arquivo = nome_diretorio + "/" + arquivo
    if arquivo.endswith('.py'):
        match = ler_arquivo(arquivo, nome_funcao)
        if match == 2:
            full_match.append(arquivo)
        elif match == 1:
            partial_match.append(arquivo)
        else:
            continue


print("Combinações completas:")
for file_path in full_match:
    print(os.path.basename(file_path))

print()
    
print("Combinações parciais:")
for file_path in partial_match:
    print(os.path.basename(file_path))
    