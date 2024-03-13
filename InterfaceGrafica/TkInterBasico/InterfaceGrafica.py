#O Tkinter é uma biblioteca gráfica padrão do Python para criar interfaces gráficas de usuário (GUI). É uma ferramenta poderosa para desenvolver aplicativos com interfaces intuitivas e interativas. 
#Documentaçção 
#https://docs.python.org/pt-br/3/library/tk.html

import tkinter as tk
from tkinter import PhotoImage

# Cria uma janela principal
janela = tk.Tk()

# Define o título da janela
janela.title("Novo Título da Janela")

# Define o tamanho da janela (largura x altura)
largura = 800
altura = 600
janela.geometry(f'{largura}x{altura}')

# Define a janela para tela cheia
#largura_tela = janela.winfo_screenwidth()
#altura_tela = janela.winfo_screenheight()
#janela.attributes('-fullscreen', True) # -alpha, -transparentcolor, -disabled, -fullscreen, -toolwindow, or -topmost
#janela.geometry(f"{largura_tela}x{altura_tela}+0+0")

# Define a janela para iniciar maximizada
janela.state("zoomed")

# Define o caminho para o arquivo de ícone (.ico, .png, etc.)
caminho_icone = "img/icons/cash.ico"

# Define o ícone da janela
janela.iconbitmap(caminho_icone)


# Adiciona um rótulo à janela
label = tk.Label(janela, text="Olá, Tkinter!")
label.pack()

# Adiciona um botão à janela
botao = tk.Button(janela, text="Clique Aqui!")
botao.pack()

# Adiciona um Campo de texto à janela
entrada = tk.Entry(janela)
entrada.pack()

# Adiciona uma Caixa de Seleção de texto à janela
opcao1 = tk.Checkbutton(janela, text="Opção 1 Caixa de Seleção")
opcao2 = tk.Checkbutton(janela, text="Opção 2 Caixa de Seleção")
opcao1.pack()
opcao2.pack()

# Adiciona uma Caixa de opções à janela
opcao1 = tk.Radiobutton(janela, text="Opção 1 Caixa de Opções", value=1)
opcao2 = tk.Radiobutton(janela, text="Opção 2 Caixa de Opções", value=2)
opcao1.pack()
opcao2.pack()

# Adiciona uma Área de texto à janela
texto = tk.Text(janela)
texto.pack()


#Adiciona um Frame à Janela
frame = tk.Frame(janela)
frame.pack()

def funcao_sair():
    janela.quit()

# Cria um menu
menu = tk.Menu(janela)
janela.config(menu=menu)

# Cria um menu "Arquivo" com uma opção "Sair"
menu_arquivo = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Arquivo", menu=menu_arquivo)
menu_arquivo.add_command(label="Sair", command=funcao_sair)

# Cria um menu "Configurações" com uma opção "Nada, Nada2"
menu_config = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Configurações", menu=menu_config)
menu_config.add_command(label="Nada", command="")
menu_config.add_command(label="Nada2",command="")

#Adicionar Imagem à tela
#adicione 'from tkinter import PhotoImage' ao projeto
# Carrega a imagem 
imagem = PhotoImage(file="img/imagens/imagem3.png")

# Redimensiona a imagem
fator_escala = 0.5  # Fator de escala (0.5 = metade do tamanho)
largura_nova = int(imagem.width() * fator_escala)
altura_nova = int(imagem.height() * fator_escala)
imagem_redimensionada = imagem.subsample(2, 2)  # Subamostragem por um fator de 2


# Cria um rótulo para exibir a imagem
label_imagem = tk.Label(janela, image=imagem_redimensionada)
label_imagem.pack()


#Ajutar posição do Widget
# Cria um botão e o posiciona nas coordenadas (100, 50) da janela
botao2 = tk.Button(janela, text="Clique Aqui!")
botao2.place(x=20, y=50)
#botao2.place(relx=0.5, rely=0.5, anchor="center") #Posisão relativa


def remover_mensagem():
    label_mensagem.config(text="")  # Limpa o texto do rótulo após 2 segundos

def exibir_clicado():
       label_mensagem.config(text="Botão clicado!")
       janela.after(2000, remover_mensagem)


# Cria um rótulo para exibir a mensagem
label_mensagem = tk.Label(janela, text="")
label_mensagem.pack()


# Carrega a imagem do botão
imagem_botao = tk.PhotoImage(file="img/imagens/botao.png")

# Redimensiona pela metade
imagem_botao = imagem_botao.subsample(2, 2)  


# Cria o botão e usa a imagem como imagem de fundo
botao3 = tk.Button(janela, image=imagem_botao, borderwidth=0, highlightthickness=0, command= exibir_clicado)
botao3.pack()


#Ao finalizar todo o aprendizado bora aprender sobre 'ttkthemes'
#Biblioteca de temas que permite estilizar o TKINTER - Deixar com a cara que deseja 
#https://ttkthemes.readthedocs.io/en/latest/themes.html

#Instale a biblioteca 'pip install ttkthemes'
#Depois de instalar a biblioteca ttkthemes, você pode usá-la para aplicar um tema a sua aplicação Tkinter
    #'import tkinter as tk
    #from tkinter import ttk
    #from ttkthemes import ThemedStyle'

# Lembre-se de Cria um estilo temático
#estilo = ThemedStyle(janela)
#estilo.set_theme("arc")  # Escolhe um tema (por exemplo, "arc")

#Por fim ao chamar o widget  em vez de chamar por 'tk' chame por 'ttk', ele já vai usar o tema escolhido
#Exemplo
#botao = ttk.Button(janela, text="Botão com Tema")
#botao.pack(pady=20)


# Inicia o loop principal da aplicação
janela.mainloop()

#Principais Componentes do Tkinter:
#anelas (Windows): As janelas são as principais áreas de trabalho da sua aplicação. Você cria uma janela principal usando tk.Tk().

#Widgets: Os widgets são elementos gráficos, como botões, rótulos, caixas de texto, etc., que você pode adicionar à sua janela. Você cria widgets usando as classes fornecidas pelo Tkinter, como Label, Button, Entry, etc.

#Gerenciadores de Layout: Tkinter fornece vários gerenciadores de layout, como pack, grid e place, que ajudam a organizar e posicionar os widgets dentro da janela.

#Eventos: Você pode vincular funções a eventos de widget, como cliques de botão, movimentos de mouse, teclas pressionadas, etc., para criar interatividade na sua aplicação.