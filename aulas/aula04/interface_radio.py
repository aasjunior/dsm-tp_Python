from tkinter import *

tela = Tk()
tela.title("Teste de Radio Buttons")

Label(tela, text="Escolha uma das cidades do Vale do Ribeira", padx=20).pack()
#Label sem nome interno
#padx - parametro no eixo x do pack: preenche ao redor do widget com espaço em branco (pady - para eixo y)

Cidades = [
    ("Júquia", "Juquiá"),
    ("Registro", "Registro"),
    ("Miracatu", "Miracatu"),
    ("Cajati", "Cajati"),
    ("Jacupiranga", "Jacupiranga")
]#1º é o texto exibido; 2º é o valor armazenado;

pizza = StringVar()
pizza.set("Miracatu") 
#StringVar - gerenciador de valor do Tkinter, armazena valores passados aos comandos da Radiobutton()
#pizza.set() - define radio selecionada ao rodar o programa

for text, valor in Cidades:
    Radiobutton(tela, text=text, variable=pizza, value=valor).pack(anchor=W)
    #anchor - posiciona elemento na tela
    #W - um dos pontos colaterais (NW, N, NE, W, CENTER, E, SW, S, SE). alinha na esquerda
    #text - recebe o valor de algum radio button selecionado 
    #variable - adiciona valor da RadioButton a variavel pizza

def click(value):
    lbl_cidade = Label(tela, text=value)
    lbl_cidade.pack()

btn_botao = Button(tela, text="Escolha uma das Cidades", command = lambda: click(pizza.get()))
#lambda - função nativa do python que não precisa estar declarada no codigo
#click - parametro para funcionamento da função lambda

btn_botao.pack()

tela.mainloop()