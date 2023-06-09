# Importação de Bibliotecas ---------------------------------------------------------------------------------------------

from tkinter import *
from customtkinter import *
from pymongo import MongoClient
from re import *

# Paleta de Cores -------------------------------------------------------------------------------------------------------

from paleta_cores import *

# Expressões Regulares (Regex) -----------------------------------------------------------------------------------------
# # ^ -> inicio de string
# # $ -> final de string
# # [a-zA-Z0-9._%+-] -> conjunto de caracteres permitidos
# # + -> indica que a expressão anterior deve aparecer uma ou mais vezes
# # ? -> representa a correspondencia de um caractere opcional
# # \w -> corresponde a qualquer caractere alfanúmeico (equivalente a [a-zA-Z0-9_])
# # @ -> separa nome do dominio
# # [a-zA-Z0-9.-] -> conjunto de caracteres permitidos para nome de dominio
# # \ -> '\' caractere de escape utilizado para escapar o '.' que separa o dominio da extensão (o '.' tbm significa qualquer caractere, sendo necessário usar escape)
# # [a-zA-Z]{2,} -> sequencia de dois ou mais (',') caracteres alfabéticos (letras maiusculas e minusculas)

def validaEmail(email):

    # r' ' -> declaração de string literal (raw), sem processamento de caracteres especiais
    pattern_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    # Verifica se o email inserido pelo usúario é válido
    if search(pattern_email, email):
        return True
    else:
        return False
    
#def validaTelefone(telefone):
#   pattern_telefone = r'^[0-9]{11}'
#  
#   if search(pattern_telefone, telefone):
#       return True
#   else:
#       return False

# Validação de senha -----------------------------------------------------------------------------------------------------    

def validaSenha(senha):
    if senha != txtConfirmarSenha.get():
        txtConfirmarSenha.configure(border_color=red)
    else:
        txtConfirmarSenha.configure(border_color=light_gray)

def on_key_release(e):
    validaSenha(txtSenha.get())
        
# CRUD com MongoDB -----------------------------------------------------------------------------------------------------

# Conexão com o banco de dados
client = MongoClient('localhost', 27017)

# Seleciona o banco de dados
db = client['Petshop']

# Armazena/cria a coleção
collection = db['Funcionarios']

# Create
def cadastrar():

    email = txtEmail.get()

    if validaEmail(email):
        print("email valido")

        # Cria um novo documento na coleção
        collection.insert_one({
            'nome': txtNome.get(),
            'email': txtEmail.get(),
            'telefone': txtTelefone.get(),
            'senha': txtSenha.get()
        })

        # Limpar os campos
        txtNome.delete(0, END)
        txtEmail.delete(0, END)
        txtTelefone.delete(0, END)
        txtSenha.delete(0, END)
        txtConfirmarSenha.delete(0, END)
        
        msgValidaEmail = "Cadastrado com sucesso"
        
        txtEmail.configure(border_color=light_gray)
        
        # Focar no Frame e não no último campo
        formFieldset.focus()

    else:
        txtEmail.configure(border_color=red)
        txtEmail.focus()
        
        msgValidaEmail = "E-mail inválido"
        
    msg = CTkLabel(formFieldset, text=msgValidaEmail)
    msg.grid(row=7, column=0, pady=10, sticky=W)
        
    
    
# Configuração de Tela --------------------------------------------------------------------------------------------------

tela = CTk()
tela.title("Cadastro")
tela.geometry("600x500")
tela.resizable(False, False)

tela._set_appearance_mode("dark")
set_default_color_theme("green")

# Formulário -----------------------------------------------------------------------------------------------------------

formCadastro = CTkFrame(tela, corner_radius=20)
formFieldset = CTkFrame(formCadastro, fg_color="transparent")

legend = CTkLabel(formFieldset, text="Cadastro", font=("arial bold", 28))

txtNome = CTkEntry(formFieldset, placeholder_text="Nome Completo", width=200)

txtEmail = CTkEntry(formFieldset, placeholder_text="Seu E-mail", width=200)

txtTelefone = CTkEntry(formFieldset, placeholder_text="(99) 99999-9999", width=200)

txtSenha = CTkEntry(formFieldset, placeholder_text="Senha", width=200, show="*")
txtConfirmarSenha = CTkEntry(formFieldset, placeholder_text="Confirmar Senha", width=200, show="*")

btnCadastrar = CTkButton(formFieldset, text="Cadastrar", width=100, command=cadastrar)

# Configurando os Widgets ----------------------------------------------------------------------------------------------

# Associando widget ao evento

txtConfirmarSenha.bind("<KeyRelease>", on_key_release)

# Gerenciadores

formCadastro.pack(padx=100, pady=50, fill=BOTH, expand=TRUE)
formFieldset.place(relx=0.5, rely=0.5, anchor=CENTER)
legend.grid(row=0, column=0, pady=(0, 10), sticky=W)
txtNome.grid(row=1, column=0, padx=(0, 5), pady=5, sticky=W)
txtEmail.grid(row=2, column=0, pady=5, sticky=W)
txtTelefone.grid(row=3, column=0, pady=5, sticky=W)
txtSenha.grid(row=4, column=0, pady=5, sticky=W)
txtConfirmarSenha.grid(row=5, column=0, pady=5, sticky=W)
btnCadastrar.grid(row=6, column=0, pady=10, sticky=W)

# Fim -------------------------------------------------------------------------------------------------------------------

tela.mainloop()