from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from dateutil.relativedelta import relativedelta
from datetime import date

preto = "#0d0c0c"
cinza = "#171616"
branco = "#ffffff"
laranja = "#ed7226"

janela = Tk()
janela.title("Calculadora")
janela.geometry("310x400")

def calcular():
    data_nascimento = cal_data_inicial.get()
    data_atual = cal_data_final.get()

    dia_nascimento, mes_nascimento, ano_nascimento = [int(f) for f in data_nascimento.split("/")]
    nascimento = date(ano_nascimento, mes_nascimento, dia_nascimento)

    dia_atual, mes_atual, ano_atual = [int(f) for f in data_atual.split("/")]
    atual = date(ano_atual, mes_atual, dia_atual)

    anos = relativedelta(atual, nascimento).years
    meses = relativedelta(atual, nascimento).months
    dias = relativedelta(atual, nascimento).days

    num_anos['text'] = anos
    num_meses['text'] = meses
    num_dias['text'] = dias

frame_cima = Frame(janela, width=310, height=140, pady=0, padx=0, relief=FLAT, bg=preto)
frame_cima.grid(row=0, column=0)

frame_baixo = Frame(janela, width=310, height=260, pady=0, padx=0, relief=FLAT, bg=cinza)
frame_baixo.grid(row=1, column=0)

text_branco = Label(frame_cima, text="CALCULADORA", width=25, height=1, padx=3, relief="flat", anchor="center", font="Ivi 15 bold", bg=preto, fg=branco)
text_branco.place(x=0, y=40)

text_laranja = Label(frame_cima, text="DE IDEADE", width=16, height=1, padx=0, relief="flat", anchor="center", font="Arial 24 bold", fg=laranja, bg=preto)
text_laranja.place(x=0, y=70)


text_data_inicial = Label(frame_baixo, text="Data de nascimento", height=1, padx=0, pady=0, relief="flat", anchor=NW, font="Ivi 11 bold", fg=branco, bg=cinza)
text_data_inicial.place(x=30, y=30)

cal_data_inicial = DateEntry(frame_baixo, width=13, bg=cinza, fg=branco, borderwidth=2, date_pattern= "dd/mm/y", y="2023")
cal_data_inicial.place(x=180, y=30)

text_data_final = Label(frame_baixo, text="Data atual", height=1, padx=0, pady=0, relief="flat", anchor=NW, font="Ivi 11 bold", fg=branco, bg=cinza)
text_data_final.place(x=30, y=80)

cal_data_final = DateEntry(frame_baixo, width=13, bg=cinza, fg=branco, borderwidth=2, date_pattern= "dd/mm/y", y="2023")
cal_data_final.place(x=180, y=80)

num_anos = Label(frame_baixo, text="00", height=1, width=3, padx=4, relief="flat", anchor="center", font="Arial 36 bold", fg=branco, bg=cinza)
num_anos.place(x=13, y=120)
text_anos = Label(frame_baixo, text="Anos", height=1, width=11, padx=2, relief="flat", anchor="center", font="Ivi 11 bold", fg=branco, bg=cinza)
text_anos.place(x=10, y=180)

num_meses = Label(frame_baixo, text="00", height=1, width=3, padx=4, relief="flat", anchor="center", font="Arial 36 bold", fg=branco, bg=cinza)
num_meses.place(x=106, y=120)
text_meses = Label(frame_baixo, text="Meses", height=1, width=11, padx=2, relief="flat", anchor="center", font="Ivi 11 bold", fg=branco, bg=cinza)
text_meses.place(x=103, y=180)

num_dias = Label(frame_baixo, text="00", height=1, width=3, padx=4, relief="flat", anchor="center", font="Arial 36 bold", fg=branco, bg=cinza)
num_dias.place(x=198, y=120)
text_dias = Label(frame_baixo, text="Dias", height=1, width=11, padx=2, relief="flat", anchor="center", font="Ivi 11 bold", fg=branco, bg=cinza)
text_dias.place(x=195, y=180)

btn_calcular = Button(frame_baixo, command= calcular, text="Calcular Idade", width=28, height=1, relief="raised",overrelief="ridge", font="Ivi 10 bold", bg=preto, fg=branco)
btn_calcular.place(x=38, y=220)

janela.mainloop()