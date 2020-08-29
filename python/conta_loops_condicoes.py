#importação do módulo sys
import sys

#Checa se algum parâmetro (Nome de algum arquivo) foi passado para o programa 
if len(sys.argv) == 1:
    print("Indique o arquivo a ser processado como parâmetro. Ex: " + sys.argv[0] + " exemplo.txt")
    exit(1)

#Checa linha a linha se as condicionais ou loops se encontram nela e armazena em contadores suas quantidade.
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