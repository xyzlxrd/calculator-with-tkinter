from tkinter import *
from tkinter import ttk

#JANELA PRINCIPAL-------------------------------------------------------------------------
janela = Tk()
janela.title("Calculadora")
janela.config(bg='#545454')

ttk.Style().configure('cor_azul.TButton', background='lightblue', relief='flat')

#DISPLAY----------------------------------------------------------------------------------
numero_da_tela = StringVar()
numero_da_tela.set('')

display = Label(janela,bg='black',fg='white' , textvariable=numero_da_tela, font=('Arial', 24), width=21, anchor='e')
display.grid(column=0, row=0, columnspan=4, ipady=20)

def adicionar_numero(num):
    valor_atual = numero_da_tela.get()
    numero_da_tela.set(valor_atual + str(num))

def calcular():
    try:
        resultado = eval(numero_da_tela.get())
        numero_da_tela.set(str(resultado))
    except Exception:
        numero_da_tela.set('ERRO')

def limpar_display():
    numero_da_tela.set('')

#BOTOES
botoes_linha1 = Button(janela, text='C', bg='#ff6666', fg='white', width=53, command=limpar_display)
botoes_linha1.grid(row=1, column=0, columnspan=4, padx=1, pady=1, ipadx=10, ipady=30)

lista_botoes_linha2 = ['7','8','9','*']
for i, texto in enumerate(lista_botoes_linha2):
    botoes_linha2 = ttk.Button(janela, text=(texto), command=lambda t=texto: adicionar_numero(t))
    botoes_linha2.grid(row=2, column=i, padx=1, pady=1, ipadx=10, ipady=30)

lista_botoes_linha3 = ['4','5','6','+']
for i, texto in enumerate(lista_botoes_linha3):
    botoes_linha3 = ttk.Button(janela, text=(texto), command=lambda t=texto: adicionar_numero(t))
    botoes_linha3.grid(row=3, column=i, padx=1, pady=1, ipadx=10, ipady=30)

lista_botoes_linha4 = ['1','2','3','-']
for i, texto in enumerate(lista_botoes_linha4):
    botoes_linha4 = ttk.Button(janela, text=(texto), command=lambda t=texto: adicionar_numero(t))
    botoes_linha4.grid(row=4, column=i, padx=1, pady=1, ipadx=10, ipady=30)

lista_botoes_linha5 = [',','0','/','=']
for i, texto in enumerate(lista_botoes_linha5):
    calculo = calcular if texto == '=' else lambda t=texto: adicionar_numero(t)
    if texto == '=':
        botoes_linha5 = Button(janela, text=(texto), bg='lightblue', fg='black', command=calculo, width=9)
    else:
        botoes_linha5 = Button(janela, text=(texto), fg='black', command=calculo, width=9)
    botoes_linha5.grid(row=5, column=i, padx=1, pady=1, ipadx=10, ipady=30)


janela.mainloop()
