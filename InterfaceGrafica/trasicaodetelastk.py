import functools
import tkinter as t

class Tela(t.Frame):
    def __init__(self, parent, nome):
        t.Frame.__init__(self, parent)
        self.nome = nome
        t.Label(self, text='Voce esta na ' + self.nome).pack()

class Menu(t.Frame):
    def __init__(self, parent, *subtelas):
        t.Frame.__init__(self, parent)
        self.current_frame = self
        for subtela in subtelas:
            t.Button(subtela, text='Voltar',
                command=functools.partial(self.muda_tela, self)).pack()
            t.Button(self, text=subtela.nome, 
                command=functools.partial(self.muda_tela, subtela)).pack()

    def muda_tela(self, qual):
        self.current_frame.pack_forget()
        qual.pack()
        self.current_frame = qual

if __name__ == '__main__':
    root = t.Tk()
    # Define o tamanho da janela (largura x altura)
    largura = 800
    altura = 600
    root.title("Novo Título da Janela")
    root.geometry(f'{largura}x{altura}')
    root.state("zoomed")

    t1 = Tela(root, 'Primeira tela')
    t2 = Tela(root, 'Segunda tela')
    t3 = Tela(root, 'Terceira tela')    

    m = Menu(root, t1, t2, t3)
    m.pack()

    #Como adicionar botão/algo na tela especifica
    btn1=t.Button(t1, text='Texto1')
    btn2=t.Button(t2, text="Texto2")
    
    btn1.pack()
    btn2.pack()
    
    root.mainloop()