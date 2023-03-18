from tkinter import *

tela = Tk()

#btn_botao - nome interno do botão
#Button - tipo do widget
#text - nome a ser exibido
#pack - tipo de gerenciador
#Ao criar a tela priorizar o tipo de gerenciador
#txt_nome - Nome interno
#Entry - para adicionar informação em uma caixa de texto
#width - tamanho do campo
#borderwidth - tamanho da borda
#fg - cor de fundo
#bg - background
#0 - parametro para funcionamento da caixa de texto

def meu_click():
    lbl_hello = Label(tela, text="Bem-Vindo " + txt_nome.get())
    lbl_hello.pack()

txt_nome = Entry(tela, width=20 , borderwidth=5, fg="blue", bg="white")
txt_nome.pack()
txt_nome.insert(0, "Digite o seu nome")

btn_botao = Button(tela, text="Click", command=meu_click)
btn_botao.pack()

tela.mainloop()