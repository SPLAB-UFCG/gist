#importação do módulo sys
import sys


if len(sys.argv) == 1:
    print("Indique o arquivo a ser processado como parâmetro. Ex: " + sys.argv[0] + " exemplo.txt")
    exit(1)

def ler_arquivo():
    para = 0
    se = 0
    enquanto = 0
    
    with open(sys.argv[1]) as open_f:
        
        while True:
            
            line = open_f.readline()
            if not line:
                break
            if line.lstrip().startswith("for "):
                para += 1
            if line.lstrip().startswith("if "):
                se += 1
            if line.lstrip().startswith("while "):
                enquanto += 1

    string = "No arquivo indicado existem: \n" + str(para) + " loops For.\n" + str(se) + " condicionais If.\n" + str(enquanto) + " loops While."

            
    return string


print(ler_arquivo())