#importar biblioteca
from tkinter import *
#criar variavel (tela)
tela = Tk()

#Titulo na barra de tarefas
tela.title("Fatec Registro")

#Configuracao da cor da tela(opcional)
tela.configure(background='#1e3743')

#Configuração do tamanho da tela
tela.geometry("700x600")

#Configuração tamanho maximo da tela
tela.resizable(True, True)

#Tamanho maximo que a tela pode chegar
tela.maxsize(width=900, height=800)

#Tamanho minimo que a tela pode chegar
tela.minsize(width=900, height=800)

#Adicionar Label
#lbl_teste = Label(tela, text="TESTE").place(x=10, y=10)
#-lbl_teste é o nome de identificação interna da label
#-Label é o tipo do componente
#-tela a variavel que a label está ligada
#-text="" e o texto a ser exibido na tela
#-place posicionamento na tela

lbl_nome = Label(tela, text="Nome", font="Arial 20 bold italic", fg="#FF8C00").place(x=10, y=10)
lbl_cpf = Label(tela, text="CPF", font="Times 15 italic", fg="#7CFC00").place(x=10, y=50)

tela.mainloop()