from tkinter import *

#Paleta de Cores -------------------------------------------

black = "#010409"
gray = "#0d1117"

#Configuração de Tela --------------------------------------

tela = Tk()
tela.title("PetShop")
tela.geometry("500x300")
tela.resizable(False, False)

#Frames ----------------------------------------------------

wrapper = Frame(tela, bg=black)
wrapper.pack(fill='both', expand=True)
container = Frame(wrapper, width=300, height=300, bg=gray)
container.place(relx=0.5, rely=0.5, anchor=CENTER)

#Campos ----------------------------------------------------

lbl_usuario = Label(container, text="Usuário").pack()
txt_usuario = Entry(container, width=20).pack()

lbl_senha = Label(container, text="Senha").pack()
txt_senha = Entry(container, width=20).pack()

tela.mainloop()