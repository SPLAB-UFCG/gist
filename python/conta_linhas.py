#importação do módulo sys
import sys

#Caso um segundo parâmetro, contendo o caminho de um arquivo,
#não seja informado o programa retorna apenas o conteúdo do print().

if len(sys.argv) == 1:
    print("Indique o arquivo a ser processado como parâmetro. Ex: " + sys.argv[0] + " exemplo.txt")
    exit(1)

#Abre o arquivo passado no segundo argumento e em seguida
#conta quantas quebras de linha o texto possui, informando
#ao usuário o número de linhas que o arquivo possui

with open(sys.argv[1]) as open_f:
    print(open_f.read().count('\n') + 1)