# bibliotecas
from tkinter import *
from tkinter import ttk

# cores
cor_azul = "#272e3b"
cor_laranja = "#db6a1f"
cor_branco = "#fcfbfa"

# definindo janela
janela = Tk()
janela.title("Calculadora")
janela.geometry("235x300")

frame_tela = Frame(janela, width=235, height=50, bg=cor_azul)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=235, height=260)
frame_corpo.grid(row=1, column=0)

todos_valores = ''

# criando funções
def entrada_valores(event):
    global todos_valores # para que os vaores possão ser acessados em todo o código, a variável precisa ser global
    todos_valores = todos_valores + str(event)
    valor_texto.set(todos_valores)

def resultado(event):
    global todos_valores
    todos_valores = str(eval(todos_valores)) 
    valor_texto.set(todos_valores)

def limpar():
    global todos_valores
    todos_valores = ''
    valor_texto.set(todos_valores)

# criando label
valor_texto = StringVar()
card_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor="e", font=("Ivi 18"), justify=RIGHT, bg=cor_azul, fg=cor_branco)
card_label.place(x=0, y=0)

# criando botões
btn_clean = Button(frame_corpo, command= lambda: limpar(), text="C", width=11, height=2, font=("Ivi 13 bold"), relief=RAISED, overrelief=RIDGE)
btn_clean.place(x=0, y=0)
btn_resto = Button(frame_corpo, command= lambda: entrada_valores('%'), text="%", width=5, height=2 , font=("Ivi 13 bold"), relief=RAISED, overrelief=RIDGE)
btn_resto.place(x=118, y=0)
btn_divisao = Button(frame_corpo, command= lambda: entrada_valores('/'), text="/", width=5, height=2, bg=cor_laranja, fg=cor_branco , font=("Ivi 13 bold"), relief=RAISED, overrelief=RIDGE)
btn_divisao.place(x=177, y=0)

btn_7 = Button(frame_corpo, command= lambda: entrada_valores('7'), text="7", width=5, height=2, font=("Ivi 13 bold"), relief=RAISED, overrelief=RIDGE)
btn_7.place(x=0, y=50)
btn_8 = Button(frame_corpo, command= lambda: entrada_valores('8'), text="8", width=5, height=2, font=("Ivi 13 bold"), relief=RAISED, overrelief=RIDGE)
btn_8.place(x=59, y=50)
btn_9 = Button(frame_corpo, command= lambda: entrada_valores('9'), text="9", width=5, height=2, font=("Ivi 13 bold"), relief=RAISED, overrelief=RIDGE)
btn_9.place(x=118, y=50)
btn_multiplicacao = Button(frame_corpo, command= lambda: entrada_valores('*'), text="*", width=5, height=2, bg=cor_laranja, fg=cor_branco, font=("Ivi 13 bold"), relief=RAISED, overrelief=RIDGE)
btn_multiplicacao.place(x=177, y=50)

btn_4 = Button(frame_corpo, command= lambda: entrada_valores('4'), text="4", width=5, height=2, font=("Ivi 13 bold"), relief=RAISED, overrelief=RIDGE)
btn_4.place(x=0, y=100)
btn_5 = Button(frame_corpo, command= lambda: entrada_valores('5'), text="5", width=5, height=2, font=("Ivi 13 bold"), relief=RAISED, overrelief=RIDGE)
btn_5.place(x=59, y=100)
btn_6 = Button(frame_corpo, command= lambda: entrada_valores('6'), text="6", width=5, height=2, font=("Ivi 13 bold"), relief=RAISED, overrelief=RIDGE)
btn_6.place(x=118, y=100)
btn_subtracao = Button(frame_corpo, command= lambda: entrada_valores('-'), text="-", width=5, height=2, bg=cor_laranja, fg=cor_branco, font=("Ivi 13 bold"), relief=RAISED, overrelief=RIDGE)
btn_subtracao.place(x=177, y=100)

btn_1 = Button(frame_corpo, command= lambda: entrada_valores('1'), text="1", width=5, height=2, font=("Ivi 13 bold"), relief=RAISED, overrelief=RIDGE)
btn_1.place(x=0, y=150)
btn_2 = Button(frame_corpo, command= lambda: entrada_valores('2'), text="2", width=5, height=2, font=("Ivi 13 bold"), relief=RAISED, overrelief=RIDGE)
btn_2.place(x=59, y=150)
btn_3 = Button(frame_corpo, command= lambda: entrada_valores('3'), text="3", width=5, height=2, font=("Ivi 13 bold"), relief=RAISED, overrelief=RIDGE)
btn_3.place(x=118, y=150)
btn_soma = Button(frame_corpo, command= lambda: entrada_valores('+'), text="+", width=5, height=2, bg=cor_laranja, fg=cor_branco, font=("Ivi 13 bold"), relief=RAISED, overrelief=RIDGE)
btn_soma.place(x=177, y=150)

btn_0 = Button(frame_corpo, command= lambda: entrada_valores('0'), text="0", width=11, height=2, font=("Ivi 13 bold"), relief=RAISED, overrelief=RIDGE)
btn_0.place(x=0, y=200)
btn_ponto = Button(frame_corpo, command= lambda: entrada_valores('.'), text=".", width=5, height=2, font=("Ivi 13 bold"), relief=RAISED, overrelief=RIDGE)
btn_ponto.place(x=118, y=200)
btn_resultado = Button(frame_corpo, command= lambda: resultado(todos_valores), text="=", width=5, height=2, bg=cor_laranja, fg=cor_branco, font=("Ivi 13 bold"), relief=RAISED, overrelief=RIDGE)
btn_resultado.place(x=177, y=200)

# mostrar janela
janela.mainloop()