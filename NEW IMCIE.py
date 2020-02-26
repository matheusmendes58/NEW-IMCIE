from tkinter import *
from tkinter import messagebox


class Tela:
    def __init__(self, master=None):
        # criação de labels e entrada de texto(Entry, Labels)
        self.widget1 = Frame(master)
        self.widget1.pack()
        self.msg = Label(self.widget1, text='Calculo de IMC')
        self.msg['font'] = ('Verdana', '12', 'italic', 'bold')
        self.msg.configure(background='gray')
        self.msg.pack()

        self.widget2_nome = Label(master, text='Qual é seu nome:')
        self.widget2_nome['font'] = ('Verdana', '10', 'italic')
        self.widget2_nome.configure(background='gray')
        self.widget2_nome.place(x=20, y=50)
        self.entrada_dados_nome = Entry(master)
        self.entrada_dados_nome.place(x=142, y=52)

        self.widget3_idade = Label(master, text='Qual sua idade:')
        self.widget3_idade['font'] = ('Verdana', '10', 'italic')
        self.widget3_idade.configure(background='gray')
        self.widget3_idade.place(x=20, y=80)
        self.entrada_dados_idade = Entry(master)
        self.entrada_dados_idade.place(x=142, y=82)

        self.widget4_kilos = Label(master, text='Qual é o seu peso:')
        self.widget4_kilos['font'] = ('Calibri', '10', 'italic')    # testando novas fontes
        self.widget4_kilos.configure(background='gray')
        self.widget4_kilos.place(x=20, y=110)
        self.entrada_dados_kilos = Entry(master)
        self.entrada_dados_kilos.place(x=142, y=112)
        self.exemplo1 = Label(master, text='exemplo: 72.5 kg')
        self.exemplo1['font'] = ('Times', '9', 'italic', 'bold')
        self.exemplo1.configure(background='gray')
        self.exemplo1.place(x=280, y=112)

        self.widget5_altura = Label(master, text='Qual é sua altura:')
        self.widget5_altura['font'] = ('Times', '10', 'italic')
        self.widget5_altura.configure(background='gray')
        self.widget5_altura.place(x=20, y=150)
        self.entrada_dados_altura = Entry(master)
        self.entrada_dados_altura.place(x=142, y=152)
        self.exemplo2 = Label(master, text='exemplo: 1.90 cm')
        self.exemplo2['font'] = ('Times', '9', 'italic', 'bold')
        self.exemplo2.configure(background='gray')
        self.exemplo2.place(x=280, y=152)

        self.widget6_imc = Label(master, text='O resultado do seu imc é:')
        self.widget6_imc.configure(background='gray')
        self.widget6_imc['font'] = ('Times', '15', 'italic')
        self.widget6_imc.place(x=20, y=200)

        # criação botão calcular
        self.button_calcular = Button(master, text='Calcular')
        self.button_calcular['font'] = ('Verdana', '12', 'italic', 'bold')
        self.button_calcular.configure(background='gray')
        self.button_calcular.place(x=350, y=400)
        self.button_calcular['command'] = self.calcular_imc

        # criação do botão sair
        self.button_sair = Button(master, text='Sair')
        self.button_sair['font'] = ('Verdana', '12', 'italic', 'bold')
        self.button_sair.configure(background='gray')
        self.button_sair.place(x=690, y=549)
        self.button_sair['command'] = self.sair

        # criação do botão limpar
        self.button_limpar = Button(master, text='Limpar')
        self.button_limpar['font'] = ('Verdana', '12', 'italic', 'bold')
        self.button_limpar.configure(background='gray')
        self.button_limpar.place(x=600, y=550)
        self.button_limpar['command'] = self.limpar

        self.widget7_nome = Label(master, text='Nome:')
        self.widget7_nome['font'] = ('Times', '15', 'italic')
        self.widget7_nome.configure(background='gray')
        self.widget7_nome.place(x=20, y=250)
        self.label_nome = Label(master, text='')
        self.label_nome['font'] = ('Verdana', '15', 'italic', 'bold')
        self.label_nome.configure(background='gray')
        self.label_nome.place(x=80, y=247)

        self.widget8_idade = Label(master, text='Idade:')
        self.widget8_idade['font'] = ('Times', '15', 'italic')
        self.widget8_idade.configure(background='gray')
        self.widget8_idade.place(x=20, y=300)
        self.label_idade = Label(master, text='')
        self.label_idade['font'] = ('Verdana', '15', 'italic', 'bold')
        self.label_idade.configure(background='gray')
        self.label_idade.place(x=80, y=297)

        self.widget9_imc = Label(master, text='O Valor calculado é :')
        self.widget9_imc['font'] = ('Times', '15', 'italic')
        self.widget9_imc.configure(background='gray')
        self.widget9_imc.place(x=20, y=350)
        self.label_imc = Label(master, text='0.00')
        self.label_imc['font'] = ('Verdana', '15', 'italic', 'bold')
        self.label_imc.configure(background='gray')
        self.label_imc.place(x=200, y=347)

    def calcular_imc(self):
        # método do botão calcular
        nome = self.entrada_dados_nome.get()
        idade = self.entrada_dados_idade.get()
        nome = str(nome).strip()
        if nome.isnumeric():
            messagebox.showerror('Erro', 'Digite apenas letras')
        else:
            self.label_nome['text'] = nome
        if idade.isnumeric():
            self.label_idade['text'] = idade
        else:
            messagebox.showerror('Erro', 'Digite apenas números')

        peso = self.entrada_dados_kilos.get()
        altura = self.entrada_dados_altura.get()
        peso = float(peso)
        altura = float(altura)
        resultado = peso / altura ** 2
        self.label_imc['text'] = round(resultado, 2)
        if resultado <= 18.5:
            self.label_imc['text'] = round(resultado, 2)
            messagebox.showwarning('***', 'Abaixo do PESO, Se alimente!')
        elif resultado > 18.5 and  resultado <= 24.999:
            messagebox.showinfo('***', 'PESO NORMAL, CONTINUE ASSIM !')
        elif resultado > 25.0 and resultado <= 29.999:
            messagebox.showinfo('***', 'SOBREPESO!!!')
        elif resultado > 30.0 and resultado <= 34.999:
            messagebox.showwarning('***', 'Obesidade GRAU 1 !!!')
        elif resultado > 35.0 and resultado <= 39.999:
            messagebox.showwarning('***', 'OBESIDADE GRAU 2 !!!')
        elif resultado > 40.0:
            messagebox.showwarning('***', 'OBESIDADE GRAU 3 !!!')

    def sair(self):
        # método para sair da aplicação
        rodar_aplicaçao.quit()

    def limpar(self):
        # método para limpar campos de entrada de dados
        self.entrada_dados_nome.delete(0, 'end')
        self.entrada_dados_idade.delete(0, 'end')
        self.entrada_dados_kilos.delete(0, 'end')
        self.entrada_dados_altura.delete(0, 'end')


rodar_aplicaçao = Tk()
rodar_aplicaçao.title('NEW IMCIE')
rodar_aplicaçao.geometry('800x600')
rodar_aplicaçao.configure(background='gray')

# colocando incone na barra de titulo
incone = PhotoImage(file='icon.ico')
rodar_aplicaçao.iconphoto(FALSE, incone)

# colocando foto no progama
imagem = PhotoImage(file='newimc.png')
imagem_label = Label(rodar_aplicaçao, image=imagem)
imagem_label.configure(background='white')
imagem_label.place(x=490, y=30)

Tela(rodar_aplicaçao)
rodar_aplicaçao.mainloop()

