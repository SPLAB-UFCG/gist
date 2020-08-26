import sys

if len(sys.argv) == 1:
    print("Indique o arquivo a ser processado como parâmetro. Ex: " + sys.argv[0] + " exemplo.txt")
    exit(1)

with open(sys.argv[1]) as open_f:
    print(open_f.read().count('\n') + 1)