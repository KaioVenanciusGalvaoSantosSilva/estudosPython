#Dicionário de Cores
cores_letra = {
                "limpa":"\33[m ",
                "vermelho":"\33[31m ",
                "verde":"\33[32m ",
                "amarelo":"\33[33m ",
                "azul":"\33[34m ",
                "magenta":"\33[35m ",
                "ciano":"\33[36m ",
                "branco":"\33[37m ",
                "negrito":"\33[1m ",
                "sublinhado":"\33[4m ",
                "inverso":"\33[7m ",  
          }
cores_fundo = {
                "limpa_fundo":"\33[m ",
                "vermelho_fundo":"\33[0;0;41m ",
                "verde_fundo":"\33[0;0;42m ",
                "amarelo_fundo":"\33[0;0;43m ",
                "azul_fundo":"\33[0;0;44m ",
                "magenta_fundo":"\33[0;0;45m ",
                "ciano_fundo":"\33[0;0;46m ",
                "branco_fundo":"\33[0;0;47m ",
            }

nome = "Kaio"
#print("Olá Mundo, seja bem-vindo {}{}{} !!!".format("\33[m" , nome ,"\33[m" ))
#---------------------------------------formata cor do texto da variavel e formata fundo após variavel
print("Olá Mundo, seja bem-vindo{}{}{}!!!".format(cores_letra["verde"] ,nome,cores_fundo["limpa_fundo"] ))
print("Olá Mundo, seja bem-vindo{}{} !!!".format(cores_letra["verde"] ,nome))
