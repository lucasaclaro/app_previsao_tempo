import tkinter
from tkinter import *
from time import sleep
# Biblioteca para acessar os dados de uma API
import requests

master = Tk()
master.geometry('490x560+650+200')
master.title('Previsão do tempo')
fundo = PhotoImage(file='imagens/tela.png')
fundo_tela = Label(master, image=fundo)
fundo_tela.pack()


def bot_click():
    cidade = entrada.get()
    api_key = '80a4ad981dc134d36cc8ddea8b67a00a'
    link = f'https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&lang=pt_br'
    requisicao = requests.get(link)
    requisicao_dic = requisicao.json()
    tempo = requisicao_dic['weather'][0]['description']
    temperatura = int(requisicao_dic['main']['temp'] - 273.15)
    umidade = requisicao_dic['main']['humidity']
    if 'céu limpo' in tempo:
        tela_resultado = tkinter.Toplevel()
        tela_resultado.geometry('490x560+650+200')
        tela_resultado.title(cidade)
        fundo = PhotoImage(file='imagens/tela_sol.png')
        fundo_tela = Label(tela_resultado, image=fundo)
        fundo_tela.pack()
        resultado = Label(tela_resultado, justify=CENTER, bg="#AD9EA5")
        resultado.place(width=300, height=100, x=100, y=200)
        resultado['text'] = f'Condições climáticas: {tempo} \n Temperatura: {temperatura}ºC \n  Umidade: {umidade}%'
        fundo_tela.mainloop()
    if 'chuva' in tempo:
        tela_resultado = tkinter.Toplevel()
        tela_resultado.geometry('490x560+650+200')
        tela_resultado.title(cidade)
        fundo = PhotoImage(file='imagens/tela_chuva.png')
        fundo_tela = Label(tela_resultado, image=fundo)
        fundo_tela.pack()
        resultado = Label(tela_resultado, justify=CENTER, bg="#AD9EA5")
        resultado.place(width=300, height=100, x=100, y=200)
        resultado['text'] = f'Condições climáticas: {tempo} \n Temperatura: {temperatura}ºC \n  Umidade: {umidade}%'
        fundo_tela.mainloop()
    if 'nublado' in tempo:
        tela_resultado = tkinter.Toplevel()
        tela_resultado.geometry('490x560+650+200')
        tela_resultado.title(cidade)
        fundo = PhotoImage(file='imagens/tela_nublado.png')
        fundo_tela = Label(tela_resultado, image=fundo)
        fundo_tela.pack()
        resultado = Label(tela_resultado, justify=CENTER, bg="#AD9EA5")
        resultado.place(width=300, height=100, x=100, y=200)
        resultado['text'] = f'Condições climáticas: {tempo} \n Temperatura: {temperatura}ºC \n  Umidade: {umidade}%'
        fundo_tela.mainloop()
    else:
        tela_resultado = tkinter.Toplevel()
        tela_resultado.geometry('490x560+650+200')
        tela_resultado.title(cidade)
        fundo = PhotoImage(file='imagens/tela_outro.png')
        fundo_tela = Label(tela_resultado, image=fundo)
        fundo_tela.pack()
        resultado = Label(tela_resultado, justify=CENTER, bg="#AD9EA5")
        resultado.place(width=300, height=100, x=100, y=200)
        resultado['text'] = f'Condições climáticas: {tempo} \n Temperatura: {temperatura}ºC \n  Umidade: {umidade}%'
        fundo_tela.mainloop()



texto_inicial = Label(master, text='Previsão do tempo', font=('Verdana', 17, 'bold'), justify=CENTER, bg='#D9D9D9')
texto_inicial.place(width=305, height=30, x=100, y=10)
texto_dois = Label(master, text='Digite abaixo o nome da cidade', font=('Verdana', 12, 'bold'), justify=CENTER, bg='#D9D9D9')
texto_dois.place(width=330, height=50, x=90, y=100)
entrada = Entry(master, font=('Verdana', 12, 'bold'), bg='#D9D9D9', justify=CENTER)
entrada.place(width=280, height=50, x=110, y=250)
botao = Button(master, text='Pesquisar', font=('Verdana', 12, 'bold'), bg='#AD9788', command=bot_click)
botao.place(width=100, height=50, x=200, y=400)




master.mainloop()