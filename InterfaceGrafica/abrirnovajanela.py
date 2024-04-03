import tkinter as tk

def abrir_segunda_tela():
    #Cria tela sobreposta
    janelaSecundaria =tk.Toplevel() 

    #Titulo da tela  
    janelaSecundaria.title("Janela Secundaria")

    #dimensiona tela
    largura = 800
    altura = 600
    janelaSecundaria.geometry(f'{largura}x{altura}')

    #Cria texto na tela
    texto1 = tk.Label(janelaSecundaria, text= "Segunda tela")

    #Cria botão na tela com texto e comando para fechar a tela
    botao1 = tk.Button(janelaSecundaria,text= "Botão Fechar",command= janelaSecundaria.destroy)

    #inicia objetos na tela em uma posicao
    texto1.place(x=350,y= 250)
    botao1.place(x=350,y= 290)

#Cria tela principal
janelaPrincipal = tk.Tk()

#dimensiona tela
largura = 800
altura = 600
janelaPrincipal.geometry(f'{largura}x{altura}')
#janelaPrincipal.state("zoomed")

#Titulo da tela
janelaPrincipal.title("Janela Principal")

#cria botão com texto e comando
botao = tk.Button(janelaPrincipal, text="Segunda janela", command= abrir_segunda_tela)

#inicia botao na tela em uma posicao
botao.place(x=350,y= 250)


#mantem a janela aberta
janelaPrincipal.mainloop()

