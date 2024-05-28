#ANSI ascape sequence
#\033[XXX;XXX;XXXm  \033[ style; text; back m 
#Ex: \033[0;33;44m

#Especificação das definições de estyle, text , back
# style
    # 0 nenhum estilo 
    # 1 negrito 
    # 4  sublinhado 
    # 7 inverte as configurações

# text
    # 30 branco
    # 31 vermelho
    # 32 verde
    # 33 amarelo
    # 34 azul
    # 35 ciano
    # 36 magenta
    # 37 cinza

# back
    # 40 branco
    # 41 vermelho
    # 42 verde
    # 43 amarelo
    # 44 azul
    # 45 magenta
    # 46 ciano
    # 47 cinza

#Exemplos na prática
#Exemplo1
    #texto branco e fundo vermelho
    #\33[0;30;41m

print("\33[0;30;41m Olá, Mundo! \33[m") #

#Exemplo2
    # texto amarelo, sublinhado e fundo azul
    # \33[4;33;44m
print("\33[4;33;44m Olá, Mundo! \33[m") #

#Exemplo3
    # texto magenta e fundo amarelo
    # \33[1;35;43m
print("\33[1;35;43m Olá, Mundo! \33[m") #

#Exemplo4
    # texto branco e fundo verde
    # \33[0;30;42m
print("\33[0;30;42m Olá, Mundo! \33[m") #

#Exemplo5
    # texto branco e fundo preto #padrão do terminal
    # \33[m     
print("\33[m  Olá, Mundo! \33[m") #

#Exemplo6
    # texto preto e fundo branco
    # \33[7;30m
print("\33[7;30m Olá, Mundo! \33[m") #


#Dicionario de cores
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
