from tkinter import *
from tkinter import Tk, ttk
from tkinter import messagebox

#cores------------------------------
co0 = "#050303"  # Preta / black
co1 = "#feffff"  # branca / white
co2 = "#3fb5a3"  # verde / green
co3 = "#38576b"  # valor / value
co4 = "#403d3d"   # letra / letters

#configurando janela-----------------------
janela = Tk()
janela.title("")
janela.geometry('310x300')
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

#dividindo a janela------------------------
frame_cima = Frame(janela, width=310, height=50, bg=co1, relief='flat')
frame_cima.grid(row=0, column=0, padx=0, pady=1, sticky=NSEW)

frame_baixo = Frame(janela, width=310, height=250, bg=co1, relief='flat')
frame_baixo.grid(row=1, column=0, padx=0, pady=1, sticky=NSEW)


credenciais = ['rafael', '123456789']


#funcao para verificar login
def verfificar_senha():
    nome = entry_nome.get()
    senha = entry_pass.get()

    #funcao apos verificacao
    if nome == 'admin' and senha == 'admin':
        messagebox.showinfo('Login', 'Seja bem vindo Admin!')
    elif credenciais[0] == nome and credenciais[1] == senha:
        messagebox.showinfo('Login', 'Seja bem vindo de volta ' +credenciais[0])

        #deletar itens no frame
        for widget in frame_cima.winfo_children():
            widget.destroy()

        for widget in frame_baixo.winfo_children():
            widget.destroy()

        nova_janela()

    else:
        messagebox.showwarning('Erro', 'Verifique o nome e a senha')

def nova_janela():
    #configurando frame cima
    label_nome = Label(frame_cima, text='Usuario: ' +credenciais[0], anchor=NE, font='Ivy 20', bg=co1, fg=co4)
    label_nome.place(x=5, y=5)

    label_linha = Label(frame_cima, text='', width=290, anchor=NW, font='Ivy 1', bg=co2, fg=co4)
    label_linha.place(x=5, y=45)

    label_nome = Label(frame_baixo, text='Seja bem vindo ' +credenciais[0], anchor=NE, font='Ivy 20', bg=co1, fg=co4)
    label_nome.place(x=5, y=95)


#configurando frame cima
label_nome = Label(frame_cima, text='LOGIN', anchor=NE, font='Ivy 25', bg=co1, fg=co4)
label_nome.place(x=5, y=5)

label_linha = Label(frame_cima, text='', width=290, anchor=NW, font='Ivy 1', bg=co2, fg=co4)
label_linha.place(x=5, y=45)

#configurando frame baixo
label_nome = Label(frame_baixo, text='Nome *', anchor=NW, font='Ivy 11', bg=co1, fg=co4)
label_nome.place(x=10, y=20)
entry_nome = Entry(frame_baixo, width=25, justify='left', font=('', 15), highlightthickness=1, relief='solid')
entry_nome.place(x=15,y=50)

label_pass = Label(frame_baixo, text='Senha *', anchor=NW, font='Ivy 11', bg=co1, fg=co4)
label_pass.place(x=10, y=95)
entry_pass = Entry(frame_baixo, width=25, justify='left',show='*', font=('', 15), highlightthickness=1, relief='solid')
entry_pass.place(x=15,y=130)
b_confirmar = Button(frame_baixo,command=verfificar_senha, text='Entrar', width=39, height=2, font='Ivy 8 bold', bg=co2, fg=co1, relief=RAISED, overrelief=RIDGE)
b_confirmar.place(x=15, y=180)

janela.mainloop()