# -*- coding:UTF-8 -*-

import six
import webbrowser, pickle, random

if six.PY3:
    import tkinter as t
    import tkinter.messagebox as tkMessageBox
    import tkinter.filedialog as tkFileDialog
elif six.PY2:
    import Tkinter as t
    import tkMessageBox
    import tkFileDialog

# import tkMessageBox, webbrowser, pickle, tkFileDialog, random

class MontyPython:
    """
        Programa para Mestres de Tormenta RPG, que consiste em uma serie de ferramentas para ajudar nos combates.
    """

    def __init__(self, janela):
        #variaveis utilizadas em todo o programa
        self.turno = 0
        self.turno1 = 0
        self.comba = {
            'Indice': ['NOME', 'PV', 'NIVEL', 'INICI', 'ORDEM DA INICIATIVA', ['DESCRIÇÂOSTATUS', 'TURNO DURAÇÂO STATUS'],
                       'TAMANHO', 'TIPO DE PERSONAGEM', 'MUNIÇÃO']}
        self.ordem = {}
        self.tagtext = {}

        #Opçõs de janela
        janela.title('Controle de Combate - Beta 0.3')
        janela.resizable(width=False, height=False)

        #Menu Superior
        principal = t.Menu(janela)
        arquivo = t.Menu(principal)
        arquivo.add_command(label="Abrir", command=self.abrir)
        arquivo.add_command(label="Salvar", command=self.salvar)
        principal.add_cascade(label="Arquivo", menu=arquivo)
        principal.add_command(label="Ajuda", command=self.ajuda)
        principal.add_command(label="Sobre", command=self.sobre)
        janela.configure(menu=principal)

        #Layout do Programa
        self.frame = t.Frame(janela)
        self.frame.pack(pady=10, padx=10)
        self.frame1 = t.Frame(self.frame, borderwidth=3, relief=t.RAISED)
        self.frame1.pack(fill=t.X, pady=5, padx=5)
        self.frame2 = t.Frame(self.frame)
        self.frame2.pack()
        self.frame2_1 = t.Frame(self.frame2, borderwidth=3, relief=t.RAISED)
        self.frame2_1.pack(side=t.LEFT, expand=1, fill=t.X, pady=5, padx=5)
        self.frame2_1_1 = t.Frame(self.frame2_1, borderwidth=3, relief=t.GROOVE)
        self.frame2_1_1.pack(pady=10, padx=5)
        self.frame2_1_1_1 = t.Frame(self.frame2_1_1)
        self.frame2_1_1_1.pack()
        self.frame2_1_1_2 = t.Frame(self.frame2_1_1)
        self.frame2_1_1_2.pack()
        self.frame2_1_1_2_1 = t.Frame(self.frame2_1_1_2)
        self.frame2_1_1_2_1.pack(side=t.LEFT)
        self.frame2_1_1_2_1_1 = t.Frame(self.frame2_1_1_2_1)
        self.frame2_1_1_2_1_1.pack()
        self.frame2_1_1_2_1_1_1 = t.Frame(self.frame2_1_1_2_1_1)
        self.frame2_1_1_2_1_1_1.pack(side=t.LEFT)
        self.frame2_1_1_2_1_1_2 = t.Frame(self.frame2_1_1_2_1_1)
        self.frame2_1_1_2_1_1_2.pack(side=t.LEFT)
        self.frame2_1_1_2_1_1_3 = t.Frame(self.frame2_1_1_2_1_1)
        self.frame2_1_1_2_1_1_3.pack(side=t.LEFT)
        self.frame2_1_1_2_1_1_4 = t.Frame(self.frame2_1_1_2_1_1)
        self.frame2_1_1_2_1_1_4.pack(side=t.LEFT)
        self.frame2_1_1_2_1_1_5 = t.Frame(self.frame2_1_1_2_1_1)
        self.frame2_1_1_2_1_1_5.pack(side=t.LEFT)
        self.frame2_1_1_2_1_2 = t.Frame(self.frame2_1_1_2_1)
        self.frame2_1_1_2_1_2.pack()
        self.frame2_1_1_2_2 = t.Frame(self.frame2_1_1_2)
        self.frame2_1_1_2_2.pack(side=t.LEFT)
        self.frame2_1_2 = t.Frame(self.frame2_1, borderwidth=3, relief=t.GROOVE)
        self.frame2_1_2.pack(fill=t.X, pady=10, padx=5)
        self.frame2_1_2_1 = t.Frame(self.frame2_1_2)
        self.frame2_1_2_1.pack()
        self.frame2_1_2_2 = t.Frame(self.frame2_1_2)
        self.frame2_1_2_2.pack()
        self.frame2_1_2_2_1 = t.Frame(self.frame2_1_2_2)
        self.frame2_1_2_2_1.pack(side=t.LEFT, pady=5, padx=5)
        self.frame2_1_2_2_1_1 = t.Frame(self.frame2_1_2_2_1)
        self.frame2_1_2_2_1_1.pack()
        self.frame2_1_2_2_1_2 = t.Frame(self.frame2_1_2_2_1)
        self.frame2_1_2_2_1_2.pack()
        self.frame2_1_2_2_1_2_1 = t.Frame(self.frame2_1_2_2_1_2)
        self.frame2_1_2_2_1_2_1.pack()
        self.frame2_1_2_2_1_2_2 = t.Frame(self.frame2_1_2_2_1_2)
        self.frame2_1_2_2_1_2_2.pack()
        self.frame2_1_2_2_2 = t.Frame(self.frame2_1_2_2)
        self.frame2_1_2_2_2.pack(side=t.LEFT, pady=5, padx=5)
        self.frame2_1_2_2_2_1 = t.Frame(self.frame2_1_2_2_2)
        self.frame2_1_2_2_2_1.pack()
        self.frame2_1_2_2_2_2 = t.Frame(self.frame2_1_2_2_2)
        self.frame2_1_2_2_2_2.pack()
        self.frame2_1_2_2_2_2_1 = t.Frame(self.frame2_1_2_2_2_2)
        self.frame2_1_2_2_2_2_1.pack()
        self.frame2_1_2_2_2_2_2 = t.Frame(self.frame2_1_2_2_2_2)
        self.frame2_1_2_2_2_2_2.pack()
        self.frame2_1_2_3 = t.Frame(self.frame2_1_2)
        self.frame2_1_2_3.pack()
        self.frame2_1_3 = t.Frame(self.frame2_1, borderwidth=3, relief=t.GROOVE)
        self.frame2_1_3.pack(fill=t.X, pady=10, padx=5)
        self.frame2_1_3_1 = t.Frame(self.frame2_1_3)
        self.frame2_1_3_1.pack()
        self.frame2_1_3_2 = t.Frame(self.frame2_1_3)
        self.frame2_1_3_2.pack()
        self.frame2_1_4 = t.Frame(self.frame2_1, borderwidth=3, relief=t.GROOVE)
        self.frame2_1_4.pack(fill=t.X, pady=5, padx=5)
        self.frame2_1_4_1 = t.Frame(self.frame2_1_4)
        self.frame2_1_4_1.pack()
        self.frame2_1_4_2 = t.Frame(self.frame2_1_4)
        self.frame2_1_4_2.pack()
        self.frame2_2 = t.Frame(self.frame2, borderwidth=3, relief=t.RAISED)
        self.frame2_2.pack(side=t.LEFT, pady=5, padx=5)
        self.frame2_2_1 = t.Frame(self.frame2_2, borderwidth=3, relief=t.GROOVE)
        self.frame2_2_1.pack(fill=t.X, pady=5, padx=5)
        self.frame2_2_1_1 = t.Frame(self.frame2_2_1)
        self.frame2_2_1_1.pack()
        self.frame2_2_1_2 = t.Frame(self.frame2_2_1)
        self.frame2_2_1_2.pack(fill=t.X, expand=True, pady=5, padx=5)
        self.frame2_2_1_2_1 = t.Frame(self.frame2_2_1_2, borderwidth=3, relief=t.RAISED)
        self.frame2_2_1_2_1.pack(side=t.LEFT, pady=5, padx=5)
        self.frame2_2_1_2_1_1 = t.Frame(self.frame2_2_1_2_1)
        self.frame2_2_1_2_1_1.pack()
        self.frame2_2_1_2_1_2 = t.Frame(self.frame2_2_1_2_1)
        self.frame2_2_1_2_1_2.pack()
        self.frame2_2_1_2_1_3 = t.Frame(self.frame2_2_1_2_1)
        self.frame2_2_1_2_1_3.pack()
        self.frame2_2_1_2_2 = t.Frame(self.frame2_2_1_2, borderwidth=3, relief=t.GROOVE)
        self.frame2_2_1_2_2.pack(side=t.LEFT, fill=t.X, expand=True, pady=5, padx=5)
        self.frame2_2_1_2_2_1 = t.Frame(self.frame2_2_1_2_2)
        self.frame2_2_1_2_2_1.pack()
        self.frame2_2_1_2_2_2 = t.Frame(self.frame2_2_1_2_2)
        self.frame2_2_1_2_2_2.pack()
        self.frame2_2_2 = t.Frame(self.frame2_2, borderwidth=3, relief=t.GROOVE)
        self.frame2_2_2.pack(fill=t.X, pady=5, padx=5)
        self.frame2_2_2_1 = t.Frame(self.frame2_2_2)
        self.frame2_2_2_1.pack()
        self.frame2_2_2_2 = t.Frame(self.frame2_2_2)
        self.frame2_2_2_2.pack()
        self.frame2_2_3 = t.Frame(self.frame2_2, borderwidth=3, relief=t.GROOVE)
        self.frame2_2_3.pack(fill=t.X, pady=5, padx=5)
        self.frame2_2_3_1 = t.Frame(self.frame2_2_3)
        self.frame2_2_3_1.pack()
        self.frame2_2_3_2 = t.Frame(self.frame2_2_3)
        self.frame2_2_3_2.pack()

        #Fontes
        fonte1 = ('Ariel', '9', 'bold')
        fonte2 = ('Ariel', '10', 'bold')

        #Titulo
        self.titulo = t.Label(self.frame1, text='Controle de Combate - Beta', fg='darkblue',
                            font=('Verdana', '14', 'bold'))
        self.titulo.pack()
        self.titulob = t.Label(self.frame1, text='Acessem dadosedesventuras.blogspot.com', font=('Verdana', '9'))
        self.titulob.pack()

        #Campo Adicionar Combatente (contido no frame2_1_1)
        self.t_add_com = t.Label(self.frame2_1_1_1, text='Adicionar Combatente', font=fonte2, height=2)
        self.t_add_com.pack()
        self.nome = t.Label(self.frame2_1_1_2_1_1_1, text='Nome', font=fonte1)
        self.nome.pack()
        self.campo_nome = t.Entry(self.frame2_1_1_2_1_1_1, width=10)
        self.campo_nome.pack()
        self.pv = t.Label(self.frame2_1_1_2_1_1_2, text='P.V.', font=fonte1)
        self.pv.pack()
        self.campo_pv = t.Entry(self.frame2_1_1_2_1_1_2, width=10)
        self.campo_pv.pack()
        self.nivel = t.Label(self.frame2_1_1_2_1_1_3, text='Nivel', font=fonte1)
        self.nivel.pack()
        self.campo_nivel = t.Entry(self.frame2_1_1_2_1_1_3, width=10)
        self.campo_nivel.pack()
        self.iniciativa = t.Label(self.frame2_1_1_2_1_1_4, text='Iniciativa', font=fonte1)
        self.iniciativa.pack()
        self.campo_iniciativa = t.Entry(self.frame2_1_1_2_1_1_4, width=10)
        self.campo_iniciativa.pack()
        self.municao = t.Label(self.frame2_1_1_2_1_1_5, text='Munição', font=fonte1)
        self.municao.pack()
        self.campo_municao = t.Entry(self.frame2_1_1_2_1_1_5, width=10)
        self.campo_municao.pack()
        self.tamanho = t.StringVar(self.frame2_1_1_2_1_2)
        self.tamanho.set(0)
        for txt, val in (
                ('Medio ou menor', '0'), ('Grande', '1'), ('Enorme', '2'), ('Descomunal', '3'), ('Colossal', '4')):
            a = t.Radiobutton(self.frame2_1_1_2_1_2, text=txt, value=val, variable=self.tamanho)
            a.pack(side=t.LEFT)
        self.botaopersonagem = t.Button(self.frame2_1_1_2_2, text='Personagem', width=10, command=self.adicionarper)
        self.botaopersonagem.pack(pady=5, padx=10)
        self.botaomonstro = t.Button(self.frame2_1_1_2_2, text='NPC', width=10, command=self.adicionarmon)
        self.botaomonstro.pack(pady=5, padx=10)

        #Campo Controle de Status(contido no frame2_1_2)
        self.t_con_sta = t.Label(self.frame2_1_2_1, text='Controle de Status', font=fonte2, height=2)
        self.t_con_sta.pack()
        self.t_con_sta1 = t.Label(self.frame2_1_2_2_1_1, text='Pontos de Vida', font=fonte2)
        self.t_con_sta1.pack()
        self.botaocura = t.Button(self.frame2_1_2_2_1_2_1, width=14, text='Curar', command=self.curar)
        self.botaocura.pack(side=t.LEFT)
        self.campo_recuperacao = t.Entry(self.frame2_1_2_2_1_2_1, width=10)
        self.campo_recuperacao.pack(side=t.LEFT)
        self.botaodano = t.Button(self.frame2_1_2_2_1_2_2, width=14, text='Causar Dano', command=self.dano_recebido)
        self.botaodano.pack(side=t.LEFT)
        self.campo_dano = t.Entry(self.frame2_1_2_2_1_2_2, width=10)
        self.campo_dano.pack(side=t.LEFT)
        self.t_con_sta2 = t.Label(self.frame2_1_2_2_2_1, text='Outros', font=fonte2)
        self.t_con_sta2.pack()
        self.botaoaltini = t.Button(self.frame2_1_2_2_2_2_1, width=14, text='Alterar Iniciativa', command=self.altini)
        self.botaoaltini.pack(side=t.LEFT)
        self.campo_altini = t.Entry(self.frame2_1_2_2_2_2_1, width=10)
        self.campo_altini.pack(side=t.LEFT)
        self.botaomonstro = t.Button(self.frame2_1_2_2_2_2_2, text='Passar Dias', width=14, command=self.passar_dias)
        self.botaomonstro.pack(side=t.LEFT)
        self.campo_dias = t.Entry(self.frame2_1_2_2_2_2_2, width=10)
        self.campo_dias.pack(side=t.LEFT)
        self.botaoaddsta = t.Button(self.frame2_1_2_3, text='ADD Outros Status', command=self.addstatus)
        self.botaoaddsta.pack(pady=5, padx=5)

        #Campo Controle de Turno(contido no frame2_1_3)        
        self.t_con_turn = t.Label(self.frame2_1_3_1, text='Controle de Turnos', font=fonte2, height=2)
        self.t_con_turn.pack()
        self.botaoordcomb = t.Button(self.frame2_1_3_2, text='Ordenar', command=self.ordenar)
        self.botaoordcomb.pack(side=t.LEFT, pady=5, padx=5)
        self.botaopassturn = t.Button(self.frame2_1_3_2, text='Passar Turno', command=self.passturn)
        self.botaopassturn.pack(side=t.LEFT, pady=5, padx=5)

        #Campo Tabuleiro de Combate(contido no frame2_1_4)
        self.t_tab_con = t.Label(self.frame2_1_4_1, text='Tabuleiro de Combate', font=fonte2, height=2)
        self.t_tab_con.pack()
        self.botaoaddsta = t.Button(self.frame2_1_4_2, text='Gerar Tabuleiro', command=self.gerarmatriz)
        self.botaoaddsta.pack(side=t.LEFT, pady=5, padx=5)

        #Campo Combate(contido no frame2_2_1)
        self.t_con = t.Label(self.frame2_2_1_1, text='Combate', font=fonte2)
        self.t_con.pack()
        self.controlecom = t.Label(self.frame2_2_1_2_1_1, text='Lista de Combate', font=fonte1)
        self.controlecom.pack()
        self.explitabp = t.Label(self.frame2_2_1_2_1_1, text='Nome - PV ')
        self.explitabp.pack()
        self.scrollbarp = t.Scrollbar(self.frame2_2_1_2_1_2)
        self.scrollbarp.pack(side=t.RIGHT)
        self.listboxp = t.Listbox(self.frame2_2_1_2_1_2)
        self.listboxp.pack()
        self.listboxp.config(yscrollcommand=self.scrollbarp.set)
        self.scrollbarp.config(command=self.listboxp.yview)
        self.botaoremover = t.Button(self.frame2_2_1_2_1_3, text='Remover', font=fonte1, command=self.remover)
        self.botaoremover.pack()
        self.vez = t.Label(self.frame2_2_1_2_2_1, text='Turno do combatente:', font=fonte1)
        self.vez.pack()

        #Campo Anotações(contido no frame2_2_2)
        self.titulo1 = t.Label(self.frame2_2_2_1, text='Anotações', font=fonte1)
        self.titulo1.pack()
        self.text = t.Text(self.frame2_2_2_2, width=35, height=6)
        self.text.pack(side=t.LEFT)
        scrollbar = t.Scrollbar(self.frame2_2_2_2)
        scrollbar.pack(side=t.RIGHT, fill=t.Y)
        self.text.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.text.yview)

        #Campo outros(contido no frame2_2_3)
        self.t_out = t.Label(self.frame2_2_3_1, text='Outros', font=fonte2, width=10)
        self.t_out.pack()
        self.botaoxp = t.Button(self.frame2_2_3_2, text='Calcular XP', font=fonte1, command=self.calculoxp)
        self.botaoxp.pack(side=t.LEFT, pady=5, padx=5)
        self.botaocritico = t.Button(self.frame2_2_3_2, text='Acerto Critico', font=fonte1, command=self.critico)
        self.botaocritico.pack(side=t.LEFT, pady=5, padx=5)

    #Definindo comando dos Botões--------------------
    #Criar Matriz de Combate:
    def critico(self):
        self.janelacr = t.Tk()
        self.janelacr.title('Critico')
        self.janelacr.resizable(width=False, height=False)
        self.framejanelacrd1 = t.Frame(self.janelacr, borderwidth=3, relief=t.GROOVE)
        self.framejanelacrd1.pack(fill=t.X, pady=5, padx=5)
        self.framejanelacr1 = t.Frame(self.framejanelacrd1)
        self.framejanelacr1.pack()
        self.framejanelacr1e = t.Frame(self.framejanelacrd1)
        self.framejanelacr1e.pack()
        self.framejanelacrd2 = t.Frame(self.janelacr, borderwidth=3, relief=t.GROOVE)
        self.framejanelacrd2.pack(fill=t.X, pady=5, padx=5)
        self.framejanelacr2 = t.Frame(self.framejanelacrd2)
        self.framejanelacr2.pack()
        self.framejanelacr2e = t.Frame(self.framejanelacrd2)
        self.framejanelacr2e.pack()
        self.framejanelacrd3 = t.Frame(self.janelacr, borderwidth=3, relief=t.GROOVE)
        self.framejanelacrd3.pack(fill=t.X, pady=5, padx=5)
        self.framejanelacr3 = t.Frame(self.framejanelacrd3)
        self.framejanelacr3.pack()
        self.framejanelacr3e = t.Frame(self.framejanelacrd3)
        self.framejanelacr3e.pack()
        self.framejanelacrd4 = t.Frame(self.janelacr, borderwidth=3, relief=t.GROOVE)
        self.framejanelacrd4.pack(fill=t.X, pady=5, padx=5)
        self.framejanelacr4 = t.Frame(self.framejanelacrd4)
        self.framejanelacr4.pack()
        self.framejanelacr4e = t.Frame(self.framejanelacrd4)
        self.framejanelacr4e.pack()
        self.framejanelacrd5 = t.Frame(self.janelacr, borderwidth=3, relief=t.GROOVE)
        self.framejanelacrd5.pack(fill=t.X, pady=5, padx=5)
        self.framejanelacr5 = t.Frame(self.framejanelacrd5)
        self.framejanelacr5.pack()
        self.framejanelacr5e = t.Frame(self.framejanelacrd5)
        self.framejanelacr5e.pack()
        self.framejanelacr6 = t.Frame(self.janelacr)
        self.framejanelacr6.pack()

        armaa = t.Label(self.framejanelacr1, text='Qual é o tipo de dano causado pela arma do atacante?')
        armaa.pack()
        self.arma = t.StringVar(self.framejanelacr1e)
        self.arma.set(0)
        for txt1, val1 in (('Corte', '0'), ('Esmagamento', '1'), ('Perfuração', '2'), ('Energia', '3')):
            arma = t.Radiobutton(self.framejanelacr1e, text=txt1, value=val1, variable=self.arma)
            arma.pack(side=t.LEFT)
        multic = t.Label(self.framejanelacr2, text='Qual é o multiplicador da arma do atacante?')
        multic.pack()
        self.multi = t.StringVar(self.framejanelacr2e)
        self.multi.set(0)
        for txt2, val2 in (('x2', '0'), ('x3', '1'), ('x4', '2')):
            multi = t.Radiobutton(self.framejanelacr2e, text=txt2, value=val2, variable=self.multi)
            multi.pack(side=t.LEFT)
        tam = t.Label(self.framejanelacr3, text='Qual é o tamanho do atacante?')
        tam.pack()
        self.taman = t.StringVar(self.framejanelacr3e)
        self.taman.set(0)
        for txt3, val3 in (
                ('Mínimo ou menor', '0'), ('Pequeno', '1'), ('Média', '2'), ('Grande', '3'), ('Enorme ou Maior', '4')):
            taman = t.Radiobutton(self.framejanelacr3e, text=txt3, value=val3, variable=self.taman)
            taman.pack(side=t.LEFT)
        arm = t.Label(self.framejanelacr4, text='Qual é a armadura do defensor')
        arm.pack()
        self.armad = t.StringVar(self.framejanelacr4e)
        self.armad.set(0)
        for txt4, val4 in (('Nenhuma', '0'), ('Leve', '1'), ('Média', '2'), ('Pesada', '3')):
            armad = t.Radiobutton(self.framejanelacr4e, text=txt4, value=val4, variable=self.armad)
            armad.pack(side=t.LEFT)
        esc = t.Label(self.framejanelacr5, text='O defensor usa escudo?')
        esc.pack()
        self.escu = t.StringVar(self.framejanelacr5e)
        self.escu.set(0)
        for txt5, val5 in (('Nenhum', '0'), ('Escudo Braço Direito', '1'), ('Escudo Braço esquerdo', '2')):
            escu = t.Radiobutton(self.framejanelacr5e, text=txt5, value=val5, variable=self.escu)
            escu.pack(side=t.LEFT)

        self.gerarcri = t.Button(self.framejanelacr6, text='Gerar Critico', command=self.gecritico)
        self.gerarcri.pack(side=t.LEFT, pady=5, padx=5)

    def gecritico(self):
        des = 0
        ARMA = self.arma.get()
        MULTI = self.multi.get()
        TAMANHO = self.taman.get()
        ARMAD = self.armad.get()
        ESCUDO = self.escu.get()

        n1 = random.random
        local = random.randrange(2, 11)
        severidade = random.randrange(2, 11)

        if MULTI == '0':
            severidade += 0
        elif MULTI == '1':
            severidade += 2
        elif MULTI == '2':
            severidade += 4

        if TAMANHO == '0':
            severidade -= 2
        elif TAMANHO == '1':
            severidade -= 1
        elif TAMANHO == '2':
            severidade += 0
        elif TAMANHO == '3':
            severidade += 1
        elif TAMANHO == '4':
            severidade += 2

        if ARMAD == '0':
            severidade += 1
        elif ARMAD == '1':
            severidade += 0
        elif ARMAD == '2':
            severidade -= 1
        elif ARMAD == '3':
            severidade -= 2

        if local == 8 and ESCUDO == '1':
            severidade -= 1
            des = 1
        elif local == 9 and ESCUDO == '2':
            severidade -= 1
            des = 1

        if ARMA == '0':
            if local == 1:
                if severidade >= 1 and severidade <= 3:
                    tkMessageBox.showinfo("Critico na Perna Direita",
                                          "Golpe certeiro na perna direita, cortando um musculo.\n\n2 Pontos de dano em Destreza.")
                elif severidade >= 4 and severidade <= 6:
                    tkMessageBox.showinfo("Critico na Perna Direita",
                                          "Golpe profundo na perna direita, cortando vários musculos.\n\n2 Pontos de dano em Destreza. O Alvo cai no chão.")
                elif severidade >= 7 and severidade <= 8:
                    tkMessageBox.showinfo("Critico na Perna Direita",
                                          "Golpe cruel na perna direita, cortando musculos e tendões.\n\n4 Pontos de dano em Destreza. Perna com corte aberto: sempre que o alvo deslocar-se 3m ou mais em uma rodada, sofre 1 ponto de dano de Constituição. Esta condição dura até o alvo receber uma cura menor.")
                elif severidade >= 9 and severidade <= 10:
                    tkMessageBox.showinfo("Critico na Perna Direita",
                                          "Golpe perfeito na perna direita, dilacerando musculos e tendões.\n\n4 Pontos de dano em Destreza e Força. Perna Ferida.")
                elif severidade >= 11 and severidade <= 12:
                    tkMessageBox.showinfo("Critico na Perna Direita",
                                          "Golpe monumental na perna direita, rasgando uma artéria.\n\n4 Pontos de dano em Destreza e Força. Perna Ferida. Sangramento Maior")
                elif severidade >= 13:
                    tkMessageBox.showinfo("Critico na Perna Direita",
                                          "Perna direita decepada.\n\n4 Pontos de dano em Destreza e Força. Perna Inutilizada. Sangramento Maior. O Alvo cai no chão")
            elif local == 2:
                if severidade >= 1 and severidade <= 3:
                    tkMessageBox.showinfo("Critico na Perna Esquerda",
                                          "Golpe certeiro na perna esquerda, cortando um musculo.\n\n2 Pontos de dano em Destreza.")
                elif severidade >= 4 and severidade <= 6:
                    tkMessageBox.showinfo("Critico na Perna Esquerda",
                                          "Golpe profundo na perna esquerda, cortando vários musculos.\n\n2 Pontos de dano em Destreza. O Alvo cai no chão.")
                elif severidade >= 7 and severidade <= 8:
                    tkMessageBox.showinfo("Critico na Perna Esquerda",
                                          "Golpe cruel na perna esquerda, cortando musculos e tendões.\n\n4 Pontos de dano em Destreza. Perna com corte aberto: sempre que o alvo deslocar-se 3m ou mais em uma rodada, sofre 1 ponto de dano de Constituição. Esta condição dura até o alvo receber uma cura menor.")
                elif severidade >= 9 and severidade <= 10:
                    tkMessageBox.showinfo("Critico na Perna Esquerda",
                                          "Golpe perfeito na perna esquerda, dilacerando musculos e tendões.\n\n4 Pontos de dano em Destreza e Força. Perna Ferida.")
                elif severidade >= 11 and severidade <= 12:
                    tkMessageBox.showinfo("Critico na Perna Esquerda",
                                          "Golpe monumental na perna esquerda, rasgando uma artéria.\n\n4 Pontos de dano em Destreza e Força. Perna Ferida. Sangramento Maior")
                elif severidade >= 13:
                    tkMessageBox.showinfo("Critico na Perna Esquerda",
                                          "Perna esquerda decepada.\n\n4 Pontos de dano em Destreza e Força. Perna Inutilizada. Sangramento Maior. O Alvo cai no chão")
            elif local >= 3 and local <= 7:
                if severidade >= 1 and severidade <= 3:
                    tkMessageBox.showinfo("Critico no Tronco",
                                          "Corte leve mas dolorido no peito.\n\n2 Pontos de dano em Constituição.")
                elif severidade >= 4 and severidade <= 6:
                    tkMessageBox.showinfo("Critico no Tronco",
                                          "Corte moderado na clavícula.\n\n2 Pontos de dano em Constituição. Penalidade de -2 nos ataques até o alvo receber uma cura menor")
                elif severidade >= 7 and severidade <= 8:
                    tkMessageBox.showinfo("Critico no Tronco",
                                          "Corte grave nas costelas\n\n4 Pontos de dano em Constituição. Penalidade de -2 nos ataques até o alvo receber uma cura maior")
                elif severidade >= 9 and severidade <= 10:
                    tkMessageBox.showinfo("Critico no Tronco",
                                          "Estômago aberto, expondo os intestinos.\n\nA cada rodada, o alvo deve deixar um braço livre e usar uma ação de movimento para manter as tripas dentro de si. Caso não faça isso, sofre 4 pontos de dano em Constituição. Esta condição dura até o alvo receber uma cura maior.")
                elif severidade >= 11 and severidade <= 12:
                    tkMessageBox.showinfo("Critico no Tronco",
                                          "Corte profundo no peito, atingindo e expondo órgãos internos.\n\n4 Pontos de dano permanente de Constituição. Sangramento Maior")
                elif severidade >= 13:
                    tkMessageBox.showinfo("Critico no Tronco", "O Alvo é cortado no meio. Morte instantânea.")
            elif local == 8:
                if des == 1:
                    if severidade >= 1 and severidade <= 3:
                        tkMessageBox.showinfo("Critico no Braço Direito",
                                              "Golpe certeiro no braço direito, cortando um musculo importante.\n\n2 Pontos de dano em Força. Escuto recebe -1 na CA.")
                    elif severidade >= 4 and severidade <= 6:
                        tkMessageBox.showinfo("Critico no Braço Direito",
                                              "Golpe profundo no braço direito, cortando vários musculos.\n\n2 Pontos de dano em Força. O Alvo derruba qualquer item que estava segurando com o braço atingido. Escuto recebe -1 na CA.")
                    elif severidade >= 7 and severidade <= 8:
                        tkMessageBox.showinfo("Critico no Braço Direito",
                                              "Golpe cruel no braço direito, cortando musculos e tendões.\n\n4 Pontos de dano em Força. Braço com corte aberto: sempre que o alvo realizar um ataque com o braço atingido, sofre 1 ponto de dano de Constituição. Esta condição dura até o alvo receber uma cura menor. Escuto recebe -1 na CA.")
                    elif severidade >= 9 and severidade <= 10:
                        tkMessageBox.showinfo("Critico no Braço Direito",
                                              "Golpe perfeito no braço direito, dilacerando musculos e tendões.\n\n4 Pontos de dano em Destreza e Força. Braço Ferido. Escuto recebe -1 na CA.")
                    elif severidade >= 11 and severidade <= 12:
                        tkMessageBox.showinfo("Critico no Braço Direito",
                                              "Golpe monumental no braço direito, rasgando uma artéria.\n\n4 Pontos de dano em Destreza e Força. Braço Ferido. Sangramento Maior. Escuto recebe -1 na CA.")
                    elif severidade >= 13:
                        tkMessageBox.showinfo("Critico no Braço Direito",
                                              "Braço direito decepada.\n\n4 Pontos de dano em Destreza e Força. Braço Inutilizado. Sangramento Maior. O Alvo derruba qualquer item que estava segurando com o braço atingido. Escuto recebe -1 na CA.")
                else:
                    if severidade >= 1 and severidade <= 3:
                        tkMessageBox.showinfo("Critico no Braço Direito",
                                              "Golpe certeiro no braço direito, cortando um musculo importante.\n\n2 Pontos de dano em Força.")
                    elif severidade >= 4 and severidade <= 6:
                        tkMessageBox.showinfo("Critico no Braço Direito",
                                              "Golpe profundo no braço direito, cortando vários musculos.\n\n2 Pontos de dano em Força. O Alvo derruba qualquer item que estava segurando com o braço atingido.")
                    elif severidade >= 7 and severidade <= 8:
                        tkMessageBox.showinfo("Critico no Braço Direito",
                                              "Golpe cruel no braço direito, cortando musculos e tendões.\n\n4 Pontos de dano em Força. Braço com corte aberto: sempre que o alvo realizar um ataque com o braço atingido, sofre 1 ponto de dano de Constituição. Esta condição dura até o alvo receber uma cura menor.")
                    elif severidade >= 9 and severidade <= 10:
                        tkMessageBox.showinfo("Critico no Braço Direito",
                                              "Golpe perfeito no braço direito, dilacerando musculos e tendões.\n\n4 Pontos de dano em Destreza e Força. Braço Ferido.")
                    elif severidade >= 11 and severidade <= 12:
                        tkMessageBox.showinfo("Critico no Braço Direito",
                                              "Golpe monumental no braço direito, rasgando uma artéria.\n\n4 Pontos de dano em Destreza e Força. Braço Ferido. Sangramento Maior")
                    elif severidade >= 13:
                        tkMessageBox.showinfo("Critico no Braço Direito",
                                              "Braço direito decepada.\n\n4 Pontos de dano em Destreza e Força. Braço Inutilizado. Sangramento Maior. O Alvo derruba qualquer item que estava segurando com o braço atingido.")
            elif local == 9:
                if des == 1:
                    if severidade >= 1 and severidade <= 3:
                        tkMessageBox.showinfo("Critico no Braço Esquerdo",
                                              "Golpe certeiro no braço direito, cortando um musculo importante.\n\n2 Pontos de dano em Força. Escuto recebe -1 na CA.")
                    elif severidade >= 4 and severidade <= 6:
                        tkMessageBox.showinfo("Critico no Braço Esquerdo",
                                              "Golpe profundo no braço direito, cortando vários musculos.\n\n2 Pontos de dano em Força. O Alvo derruba qualquer item que estava segurando com o braço atingido. Escuto recebe -1 na CA.")
                    elif severidade >= 7 and severidade <= 8:
                        tkMessageBox.showinfo("Critico no Braço Esquerdo",
                                              "Golpe cruel no braço direito, cortando musculos e tendões.\n\n4 Pontos de dano em Força. Braço com corte aberto: sempre que o alvo realizar um ataque com o braço atingido, sofre 1 ponto de dano de Constituição. Esta condição dura até o alvo receber uma cura menor. Escuto recebe -1 na CA.")
                    elif severidade >= 9 and severidade <= 10:
                        tkMessageBox.showinfo("Critico no Braço Esquerdo",
                                              "Golpe perfeito no braço direito, dilacerando musculos e tendões.\n\n4 Pontos de dano em Destreza e Força. Braço Ferido. Escuto recebe -1 na CA.")
                    elif severidade >= 11 and severidade <= 12:
                        tkMessageBox.showinfo("Critico no Braço Esquerdo",
                                              "Golpe monumental no braço direito, rasgando uma artéria.\n\n4 Pontos de dano em Destreza e Força. Braço Ferido. Sangramento Maior. Escuto recebe -1 na CA.")
                    elif severidade >= 13:
                        tkMessageBox.showinfo("Critico no Braço Esquerdo",
                                              "Braço direito decepada.\n\n4 Pontos de dano em Destreza e Força. Braço Inutilizado. Sangramento Maior. O Alvo derruba qualquer item que estava segurando com o braço atingido. Escuto recebe -1 na CA.")
                else:
                    if severidade >= 1 and severidade <= 3:
                        tkMessageBox.showinfo("Critico no Braço Esquerdo",
                                              "Golpe certeiro no braço direito, cortando um musculo importante.\n\n2 Pontos de dano em Força.")
                    elif severidade >= 4 and severidade <= 6:
                        tkMessageBox.showinfo("Critico no Braço Esquerdo",
                                              "Golpe profundo no braço direito, cortando vários musculos.\n\n2 Pontos de dano em Força. O Alvo derruba qualquer item que estava segurando com o braço atingido.")
                    elif severidade >= 7 and severidade <= 8:
                        tkMessageBox.showinfo("Critico no Braço Esquerdo",
                                              "Golpe cruel no braço direito, cortando musculos e tendões.\n\n4 Pontos de dano em Força. Braço com corte aberto: sempre que o alvo realizar um ataque com o braço atingido, sofre 1 ponto de dano de Constituição. Esta condição dura até o alvo receber uma cura menor.")
                    elif severidade >= 9 and severidade <= 10:
                        tkMessageBox.showinfo("Critico no Braço Esquerdo",
                                              "Golpe perfeito no braço direito, dilacerando musculos e tendões.\n\n4 Pontos de dano em Destreza e Força. Braço Ferido.")
                    elif severidade >= 11 and severidade <= 12:
                        tkMessageBox.showinfo("Critico no Braço Esquerdo",
                                              "Golpe monumental no braço direito, rasgando uma artéria.\n\n4 Pontos de dano em Destreza e Força. Braço Ferido. Sangramento Maior")
                    elif severidade >= 13:
                        tkMessageBox.showinfo("Critico no Braço Esquerdo",
                                              "Braço direito decepada.\n\n4 Pontos de dano em Destreza e Força. Braço Inutilizado. Sangramento Maior. O Alvo derruba qualquer item que estava segurando com o braço atingido.")
            elif local == 10:
                if severidade >= 1 and severidade <= 3:
                    tkMessageBox.showinfo("Critico na Cabeça", "Corte na bochecha.\n\n2 Pontos de dano em Carisma.")
                elif severidade >= 4 and severidade <= 6:
                    tkMessageBox.showinfo("Critico na Cabeça",
                                          "Corte no nariz.\n\n2 Pontos de dano em Carisma. Sangramento")
                elif severidade >= 7 and severidade <= 8:
                    tkMessageBox.showinfo("Critico na Cabeça",
                                          "Orelha decepada.\n\n4 Pontos de dano em Carisma. Penalidade de - em testes de Iniciativa e Percepção.")
                elif severidade >= 9 and severidade <= 10:
                    tkMessageBox.showinfo("Critico na Cabeça",
                                          "Corte na testa.\n\n4 Pontos de dano em Carisma. Sangramento Maior. Alvo coloca a mão na cabeça, em dor e fica atordoado por uma rodada.")
                elif severidade >= 11 and severidade <= 12:
                    tkMessageBox.showinfo("Critico na Cabeça",
                                          "Corte na jugular.\n\nO Alvo perde 20% de seus PV máximos por rodada. Esta condição dura até o alvo receber uma cura maior, ou morrer.")
                elif severidade >= 13:
                    tkMessageBox.showinfo("Critico na Cabeça", "O Alvo é decapitado.\n\nMorte instantânea.")
        if ARMA == '1':
            if local == 1:
                if severidade >= 1 and severidade <= 3:
                    tkMessageBox.showinfo("Critico na Perna Direita",
                                          "Pancada certeiro na perna direita, esmagando os musculos.\n\n2 Pontos de dano em Destreza.")
                elif severidade >= 4 and severidade <= 6:
                    tkMessageBox.showinfo("Critico na Perna Direita",
                                          "Pancada forte na perna direita, causando uma fratura.\n\n2 Pontos de dano em Destreza. O Alvo perde a sua próxima ação de movimento.")
                elif severidade >= 7 and severidade <= 8:
                    tkMessageBox.showinfo("Critico na Perna Direita",
                                          "Pancada Terrivel na perna direita, causando várias fraturas e contrações nos músculos\n\n4 Pontos de dano em Destreza. O Deslocamento do alvo é reduzido à metade por um minuto.")
                elif severidade >= 9 and severidade <= 10:
                    tkMessageBox.showinfo("Critico na Perna Direita",
                                          "Golpe cruel na perna direita, quebrando o membro.\n\n4 Pontos de dano em Destreza e Força. Perna Ferida.")
                elif severidade >= 11 and severidade <= 12:
                    tkMessageBox.showinfo("Critico na Perna Direita",
                                          "Golpe devastador na perna direita, quebrando o membro em vários lugares ou estraçalhando o joelho.\n\n4 Pontos de dano em Destreza e Força. 2 pontos de dano permanente em Destreza. Perna Ferida.")
                elif severidade >= 13:
                    tkMessageBox.showinfo("Critico na Perna Direita",
                                          "Golpe perfeito na perna direita.\n\nO membro se parte em varios lugares, o osso torna-se uma pasta esbranquiçada. 4 pontos de dano em Força e Destreza. 2 pontos de dano permanente em Destreza. Perna inutilizada. O alvo cai no chão.")
            elif local == 2:
                if severidade >= 1 and severidade <= 3:
                    tkMessageBox.showinfo("Critico na Perna Esquerda",
                                          "Pancada certeiro na perna esquerda, esmagando os musculos.\n\n2 Pontos de dano em Destreza.")
                elif severidade >= 4 and severidade <= 6:
                    tkMessageBox.showinfo("Critico na Perna Esquerda",
                                          "Pancada forte na perna esquerda, causando uma fratura.\n\n2 Pontos de dano em Destreza. O Alvo perde a sua próxima ação de movimento.")
                elif severidade >= 7 and severidade <= 8:
                    tkMessageBox.showinfo("Critico na Perna Esquerda",
                                          "Pancada Terrivel na perna esquerda, causando várias fraturas e contrações nos músculos\n\n4 Pontos de dano em Destreza. O Deslocamento do alvo é reduzido à metade por um minuto.")
                elif severidade >= 9 and severidade <= 10:
                    tkMessageBox.showinfo("Critico na Perna Esquerda",
                                          "Golpe cruel na perna esquerda, quebrando o membro.\n\n4 Pontos de dano em Destreza e Força. Perna Ferida.")
                elif severidade >= 11 and severidade <= 12:
                    tkMessageBox.showinfo("Critico na Perna Esquerda",
                                          "Golpe devastador na perna esquerda, quebrando o membro em vários lugares ou estraçalhando o joelho.\n\n4 Pontos de dano em Destreza e Força. 2 pontos de dano permanente em Destreza. Perna Ferida.")
                elif severidade >= 13:
                    tkMessageBox.showinfo("Critico na Perna Esquerda",
                                          "Golpe perfeito na perna esquerda.\n\nO membro se parte em varios lugares, o osso torna-se uma pasta esbranquiçada. 4 pontos de dano em Força e Destreza. 2 pontos de dano permanente em Destreza. Perna inutilizada. O alvo cai no chão.")
            elif local >= 3 and local <= 7:
                if severidade >= 1 and severidade <= 3:
                    tkMessageBox.showinfo("Critico no Tronco",
                                          "Pancada forte, abalando os órgãos internos do alvo.\n\n2 Pontos de dano em Constituição.")
                elif severidade >= 4 and severidade <= 6:
                    tkMessageBox.showinfo("Critico no Tronco",
                                          "Pancada muito forte, causando uma fratura.\n\n2 Pontos de dano em Constituição. O alvo é empurrado 1,5m em uma direção à escolha do atacante.")
                elif severidade >= 7 and severidade <= 8:
                    tkMessageBox.showinfo("Critico no Tronco",
                                          "Pancada terrível, rompendo inúmeros órgãos.\n\n4 Pontos de dano em Constituição e o alvo ainda perde sua próxima ação padrão.")
                elif severidade >= 9 and severidade <= 10:
                    tkMessageBox.showinfo("Critico no Tronco",
                                          "Golpe brutal, quebrando o esterno e várias costelas\n\n4 Pontos de dano em Constituiçã. Alvo fica enjoado por 1 minuto.")
                elif severidade >= 11 and severidade <= 12:
                    tkMessageBox.showinfo("Critico no Tronco",
                                          "Golpe assustador.\n\nO esterno se quebra, várias costelas se esfacelam, fragmentos de ossos perfuram multiplos órgãos internos. A saúde do alvo é comprometida para sempre. 4 pontos de dano em Constituição. Alvo fica atordoado por 1 rodada e enjoado por 1 minuto.")
                elif severidade >= 13:
                    tkMessageBox.showinfo("Critico no Tronco",
                                          "Algo se parte dentro do alvo, perfurando um órgão vital. Morte instantânea.")
            elif local == 8:
                if des == 1:
                    if severidade >= 1 and severidade <= 3:
                        tkMessageBox.showinfo("Critico no Braço Direito",
                                              "Pancada forte no braço direito, abalando os músculos do alvo e talvez causando uma fratura.\n\n2 Pontos de dano em Força. Escuto recebe -1 na CA.")
                    elif severidade >= 4 and severidade <= 6:
                        tkMessageBox.showinfo("Critico no Braço Direito",
                                              "Pancada muito forte, causando uma fraturado no braço direito.\n\n2 Pontos de dano em Força. O Alvo derruba qualquer item que estava segurando com o braço atingido. Escuto recebe -1 na CA.")
                    elif severidade >= 7 and severidade <= 8:
                        tkMessageBox.showinfo("Critico no Braço Direito",
                                              "Pancada terrívelno braço direito, causando várias fraturas e contrações nos músculos.\n\n4 Pontos de dano em Força. Na próxima rodada o alvo não pode atacar com o braço direito. Escuto recebe -1 na CA.")
                    elif severidade >= 9 and severidade <= 10:
                        tkMessageBox.showinfo("Critico no Braço Direito",
                                              "Golpe perfeito, quebrando o braço direito.\n\n4 Pontos de dano em Destreza e Força. Braço Ferido. Escuto recebe -1 na CA.")
                    elif severidade >= 11 and severidade <= 12:
                        tkMessageBox.showinfo("Critico no Braço Direito",
                                              "Golpe devastador, quebrando o braço direito em varios lugares ou estraçalhando o cotovelo.\n\n4 Pontos de dano em Destreza e Força. Braço Ferido. Dor latejante impõe penalidade de -2 em jogadas e teste por 1 minuto. Escuto recebe -1 na CA.")
                    elif severidade >= 13:
                        tkMessageBox.showinfo("Critico no Braço Direito",
                                              "Golpe perfeito. O braço direito se parte em vários lugares, o osso torna-se uma pasta esbranquiçada.\n\n4 pontos de dano em Força e Destreza. 2 pontos de dano permanente em Força.Braço inutilizado. Obviamente, o alvo derruba qualquer item que estava segurando com o braço atingido. Escuto recebe -1 na CA.")
                else:
                    if severidade >= 1 and severidade <= 3:
                        tkMessageBox.showinfo("Critico no Braço Direito",
                                              "Pancada forte no braço direito, abalando os músculos do alvo e talvez causando uma fratura.\n\n2 Pontos de dano em Força.")
                    elif severidade >= 4 and severidade <= 6:
                        tkMessageBox.showinfo("Critico no Braço Direito",
                                              "Pancada muito forte, causando uma fraturado no braço direito.\n\n2 Pontos de dano em Força. O Alvo derruba qualquer item que estava segurando com o braço atingido.")
                    elif severidade >= 7 and severidade <= 8:
                        tkMessageBox.showinfo("Critico no Braço Direito",
                                              "Pancada terrívelno braço direito, causando várias fraturas e contrações nos músculos.\n\n4 Pontos de dano em Força. Na próxima rodada o alvo não pode atacar com o braço direito.")
                    elif severidade >= 9 and severidade <= 10:
                        tkMessageBox.showinfo("Critico no Braço Direito",
                                              "Golpe perfeito, quebrando o braço direito.\n\n4 Pontos de dano em Destreza e Força. Braço Ferido. Escuto recebe -1 na CA.")
                    elif severidade >= 11 and severidade <= 12:
                        tkMessageBox.showinfo("Critico no Braço Direito",
                                              "Golpe devastador, quebrando o braço direito em varios lugares ou estraçalhando o cotovelo.\n\n4 Pontos de dano em Destreza e Força. Braço Ferido. Dor latejante impõe penalidade de -2 em jogadas e teste por 1 minuto.")
                    elif severidade >= 13:
                        tkMessageBox.showinfo("Critico no Braço Direito",
                                              "Golpe perfeito. O braço direito se parte em vários lugares, o osso torna-se uma pasta esbranquiçada.\n\n4 pontos de dano em Força e Destreza. 2 pontos de dano permanente em Força.Braço inutilizado. Obviamente, o alvo derruba qualquer item que estava segurando com o braço atingido.")
            elif local == 9:
                if des == 1:
                    if severidade >= 1 and severidade <= 3:
                        tkMessageBox.showinfo("Critico no Braço Esquerdo",
                                              "Pancada forte no braço esquerdo, abalando os músculos do alvo e talvez causando uma fratura.\n\n2 Pontos de dano em Força. Escuto recebe -1 na CA.")
                    elif severidade >= 4 and severidade <= 6:
                        tkMessageBox.showinfo("Critico no Braço Esquerdo",
                                              "Pancada muito forte, causando uma fraturado no braço esquerdo.\n\n2 Pontos de dano em Força. O Alvo derruba qualquer item que estava segurando com o braço atingido. Escuto recebe -1 na CA.")
                    elif severidade >= 7 and severidade <= 8:
                        tkMessageBox.showinfo("Critico no Braço Esquerdo",
                                              "Pancada terrívelno braço esquerdo, causando várias fraturas e contrações nos músculos.\n\n4 Pontos de dano em Força. Na próxima rodada o alvo não pode atacar com o braço direito. Escuto recebe -1 na CA.")
                    elif severidade >= 9 and severidade <= 10:
                        tkMessageBox.showinfo("Critico no Braço Esquerdo",
                                              "Golpe perfeito, quebrando o braço esquerdo.\n\n4 Pontos de dano em Destreza e Força. Braço Ferido. Escuto recebe -1 na CA.")
                    elif severidade >= 11 and severidade <= 12:
                        tkMessageBox.showinfo("Critico no Braço Esquerdo",
                                              "Golpe devastador, quebrando o braço esquerdo em varios lugares ou estraçalhando o cotovelo.\n\n4 Pontos de dano em Destreza e Força. Braço Ferido. Dor latejante impõe penalidade de -2 em jogadas e teste por 1 minuto. Escuto recebe -1 na CA.")
                    elif severidade >= 13:
                        tkMessageBox.showinfo("Critico no Braço Esquerdo",
                                              "Golpe perfeito. O braço esquerdo se parte em vários lugares, o osso torna-se uma pasta esbranquiçada.\n\n4 pontos de dano em Força e Destreza. 2 pontos de dano permanente em Força.Braço inutilizado. Obviamente, o alvo derruba qualquer item que estava segurando com o braço atingido. Escuto recebe -1 na CA.")
                else:
                    if severidade >= 1 and severidade <= 3:
                        tkMessageBox.showinfo("Critico no Braço Esquerdo",
                                              "Pancada forte no braço esquerdo, abalando os músculos do alvo e talvez causando uma fratura.\n\n2 Pontos de dano em Força.")
                    elif severidade >= 4 and severidade <= 6:
                        tkMessageBox.showinfo("Critico no Braço Esquerdo",
                                              "Pancada muito forte, causando uma fraturado no braço esquerdo.\n\n2 Pontos de dano em Força. O Alvo derruba qualquer item que estava segurando com o braço atingido.")
                    elif severidade >= 7 and severidade <= 8:
                        tkMessageBox.showinfo("Critico no Braço Esquerdo",
                                              "Pancada terrívelno braço esquerdo, causando várias fraturas e contrações nos músculos.\n\n4 Pontos de dano em Força. Na próxima rodada o alvo não pode atacar com o braço direito.")
                    elif severidade >= 9 and severidade <= 10:
                        tkMessageBox.showinfo("Critico no Braço Esquerdo",
                                              "Golpe perfeito, quebrando o braço esquerdo.\n\n4 Pontos de dano em Destreza e Força. Braço Ferido. Escuto recebe -1 na CA.")
                    elif severidade >= 11 and severidade <= 12:
                        tkMessageBox.showinfo("Critico no Braço Esquerdo",
                                              "Golpe devastador, quebrando o braço esquerdo em varios lugares ou estraçalhando o cotovelo.\n\n4 Pontos de dano em Destreza e Força. Braço Ferido. Dor latejante impõe penalidade de -2 em jogadas e teste por 1 minuto.")
                    elif severidade >= 13:
                        tkMessageBox.showinfo("Critico no Braço Esquerdo",
                                              "Golpe perfeito. O braço esquerdo se parte em vários lugares, o osso torna-se uma pasta esbranquiçada.\n\n4 pontos de dano em Força e Destreza. 2 pontos de dano permanente em Força.Braço inutilizado. Obviamente, o alvo derruba qualquer item que estava segurando com o braço atingido.")
            elif local == 10:
                if severidade >= 1 and severidade <= 3:
                    tkMessageBox.showinfo("Critico na Cabeça",
                                          "Pancada forte na cabeça, causando tontura.\n\n2 Pontos de dano em Sabedoria.")
                elif severidade >= 4 and severidade <= 6:
                    tkMessageBox.showinfo("Critico na Cabeça",
                                          "Pancada muito forte na cabeça, causando desorientação.\n\n2 Pontos de dano em Sabedoria. Alvo fica pasmo por uma rodada.")
                elif severidade >= 7 and severidade <= 8:
                    tkMessageBox.showinfo("Critico na Cabeça",
                                          "Pancada terrível na cabeça, causando forte desorientação. \n\n4 pontos de dano em Sabedoria. Alvo fica atordoado uma rodada.")
                elif severidade >= 9 and severidade <= 10:
                    tkMessageBox.showinfo("Critico na Cabeça",
                                          "Golpe certeiro na cabeça, com força devastadora.\n\n4 Pontos de dano em Inteligencia e Sabedoria. Alvo fica atordoado por 1d3 rodadas.")
                elif severidade >= 11 and severidade <= 12:
                    tkMessageBox.showinfo("Critico na Cabeça",
                                          "Golpe monstruoso na cabeça. O crânio do alvo racha, num ferimento horrível\n\nO alvo nunca mais será o mesmo. 4 pontos de dano em Inteligência e Sabedoria. 2 pontos de dano permanente em inteligência e Sabedoria. Alvo fica atordoado por 1d3 rodadas.")
                elif severidade >= 13:
                    tkMessageBox.showinfo("Critico na Cabeça",
                                          "O Crânio do alvo é esmagado, num golpe brutal. Morte Instantânea.")


    def gerarmatriz(self):
        self.tagtext = {}
        self.result = tkMessageBox.askquestion("Gerador de Tabuleiro de Combate",
                                               "Você gostaria de um Tabuleiro separado para os jogadores?\n\nTodas as modificações no Tabuleiro do mestre será replicada automaticamente para o Tabuleiro dos jogadores.",
                                               icon='question')
        try:
            self.matrizjoga.destroy()
        except:
            pass
        try:
            self.matrizmest.destroy()
            self.botaoacrema.destroy()
        except:
            pass

        if self.result == 'yes':
            self.matrizmest = t.Tk()
            self.matrizmest.title('Tabuleiro de Combate - Mestre')
            self.framematrizm = t.Frame(self.matrizmest)
            self.framematrizm.pack()
            self.matrizjoga = t.Tk()
            self.matrizjoga.title('Tabuleiro de Combate - Jogador')
            self.framematriz = t.Frame(self.matrizjoga)
            self.framematriz.pack()
            self.matriz = t.Canvas(self.framematrizm, width=455, height=455, cursor='X_cursor', bd=5, bg='white')
            self.matriz.pack(pady=5, padx=5)
            self.matriz1 = t.Canvas(self.framematriz, width=455, height=455, cursor='X_cursor', bd=5, bg='white')
            self.matriz1.pack(pady=5, padx=5)
            self.botaoacrema = t.Button(self.frame2_1_4_2, text='Add ao Tabuleiro', width=14, command=self.add_matriz)
            self.botaoacrema.pack(side=t.LEFT)
            for i in range(10, 480, 30):
                for z in range(10, 480, 30):
                    self.matriz.create_line(i, z, -i, z)
                    self.matriz1.create_line(i, z, -i, z)
            for i in range(10, 480, 30):
                for z in range(10, 480, 30):
                    self.matriz.create_line(i, z, i, -z)
                    self.matriz1.create_line(i, z, i, -z)
            self.matriz.bind('<B1-Motion>', self.movermatriz)
        else:
            self.matrizmest = t.Tk()
            self.matrizmest.title('Tabuleiro de Combate - Mestre')
            self.framematrizm = t.Frame(self.matrizmest)
            self.framematrizm.pack()
            self.matriz = t.Canvas(self.framematrizm, width=455, height=455, cursor='X_cursor', bd=5, bg='white')
            self.matriz.pack(pady=5, padx=5)
            self.botaoacrema = t.Button(self.frame2_1_4_2, text='Add ao Tabuleiro', width=14, command=self.add_matriz)
            self.botaoacrema.pack(side=t.LEFT)
            for i in range(10, 480, 30):
                for z in range(10, 480, 30):
                    self.matriz.create_line(i, z, -i, z)
            for i in range(10, 480, 30):
                for z in range(10, 480, 30):
                    self.matriz.create_line(i, z, i, -z)
            self.matriz.bind('<B1-Motion>', self.movermatriz)

    #Movendo circulo na Matriz:        
    def movermatriz(self, event):
        if self.result == 'yes':
            a = map(int, self.listboxp.curselection())
            c = self.listboxp.get(a[0], last=None)
            c = c.split(' - ')
            nome = c[0]
            x = self.matriz.canvasx(event.x)
            y = self.matriz.canvasy(event.y)
            if self.comba[nome][6] == '0':
                coordsa = [x, y, x - 30, y - 30]
                self.matriz.coords((self.tagtext[nome]), coordsa[2] + 15, coordsa[3] + 15)
                self.matriz1.coords((self.tagtext[nome]), coordsa[2] + 15, coordsa[3] + 15)
            elif self.comba[nome][6] == '1':
                coordsa = [x, y, x - 60, y - 60]
                self.matriz.coords((self.tagtext[nome]), coordsa[2] + 30, coordsa[3] + 30)
                self.matriz1.coords((self.tagtext[nome]), coordsa[2] + 30, coordsa[3] + 30)
            elif self.comba[nome][6] == '2':
                coordsa = [x, y, x - 90, y - 90]
                self.matriz.coords((self.tagtext[nome]), coordsa[2] + 45, coordsa[3] + 45)
                self.matriz1.coords((self.tagtext[nome]), coordsa[2] + 45, coordsa[3] + 45)
            elif self.comba[nome][6] == '3':
                coordsa = [x, y, x - 120, y - 120]
                self.matriz.coords((self.tagtext[nome]), coordsa[2] + 60, coordsa[3] + 60)
                self.matriz1.coords((self.tagtext[nome]), coordsa[2] + 60, coordsa[3] + 60)
            elif self.comba[nome][6] == '4':
                coordsa = [x, y, x - 180, y - 180]
                self.matriz.coords((self.tagtext[nome]), coordsa[2] + 90, coordsa[3] + 90)
                self.matriz1.coords((self.tagtext[nome]), coordsa[2] + 90, coordsa[3] + 90)
            self.matriz.coords((nome), coordsa[0], coordsa[1], coordsa[2], coordsa[3])
            self.matriz1.coords((nome), coordsa[0], coordsa[1], coordsa[2], coordsa[3])
        else:
            a = map(int, self.listboxp.curselection())
            c = self.listboxp.get(a[0], last=None)
            c = c.split(' - ')
            nome = c[0]
            x = self.matriz.canvasx(event.x)
            y = self.matriz.canvasy(event.y)
            if self.comba[nome][6] == '0':
                coordsa = [x, y, x - 30, y - 30]
                self.matriz.coords((self.tagtext[nome]), coordsa[2] + 15, coordsa[3] + 15)
            elif self.comba[nome][6] == '1':
                coordsa = [x, y, x - 60, y - 60]
                self.matriz.coords((self.tagtext[nome]), coordsa[2] + 30, coordsa[3] + 30)
            elif self.comba[nome][6] == '2':
                coordsa = [x, y, x - 90, y - 90]
                self.matriz.coords((self.tagtext[nome]), coordsa[2] + 45, coordsa[3] + 45)
            elif self.comba[nome][6] == '3':
                coordsa = [x, y, x - 120, y - 120]
                self.matriz.coords((self.tagtext[nome]), coordsa[2] + 60, coordsa[3] + 60)
            elif self.comba[nome][6] == '4':
                coordsa = [x, y, x - 180, y - 180]
                self.matriz.coords((self.tagtext[nome]), coordsa[2] + 90, coordsa[3] + 90)
            self.matriz.coords((nome), coordsa[0], coordsa[1], coordsa[2], coordsa[3])

    #Botão adicionar Matriz
    def add_matriz(self):
        if self.result == 'yes':
            a = map(int, self.listboxp.curselection())
            c = self.listboxp.get(a[0], last=None)
            c = c.split(' - ')
            nome = c[0]
            try:
                if self.tagtext[nome] == True:
                    pass
            except:
                if self.comba[nome][6] == '0':
                    if self.comba[nome][7] == 0:
                        self.matriz.create_oval(30, 30, 60, 60, tag=nome, fill='dodgerblue')
                        a = texto = self.matriz.create_text(45, 45, tag=nome, text=nome, font=('Arial', '7'),
                                                            anchor=t.CENTER)
                        self.matriz1.create_oval(30, 30, 60, 60, tag=nome, fill='dodgerblue')
                        a = texto = self.matriz1.create_text(45, 45, tag=nome, text=nome, font=('Arial', '7'),
                                                             anchor=t.CENTER)
                    elif self.comba[nome][7] == 1:
                        self.matriz.create_oval(30, 30, 60, 60, tag=nome, fill='red')
                        a = texto = self.matriz.create_text(45, 45, tag=nome, text=nome, font=('Arial', '7'),
                                                            anchor=t.CENTER)
                        self.matriz1.create_oval(30, 30, 60, 60, tag=nome, fill='red')
                        a = texto = self.matriz1.create_text(45, 45, tag=nome, text=nome, font=('Arial', '7'),
                                                             anchor=t.CENTER)
                elif self.comba[nome][6] == '1':
                    if self.comba[nome][7] == 0:
                        self.matriz.create_oval(30, 30, 90, 90, tag=nome, fill='dodgerblue')
                        a = texto = self.matriz.create_text(60, 60, tag=nome, text=nome, font=('Arial', '8'),
                                                            anchor=t.CENTER)
                        self.matriz1.create_oval(30, 30, 90, 90, tag=nome, fill='dodgerblue')
                        a = texto = self.matriz1.create_text(60, 60, tag=nome, text=nome, font=('Arial', '8'),
                                                             anchor=t.CENTER)
                    elif self.comba[nome][7] == 1:
                        self.matriz.create_oval(30, 30, 90, 90, tag=nome, fill='red')
                        a = texto = self.matriz.create_text(60, 60, tag=nome, text=nome, font=('Arial', '8'),
                                                            anchor=t.CENTER)
                        self.matriz1.create_oval(30, 30, 90, 90, tag=nome, fill='red')
                        a = texto = self.matriz1.create_text(60, 60, tag=nome, text=nome, font=('Arial', '8'),
                                                             anchor=t.CENTER)
                elif self.comba[nome][6] == '2':
                    if self.comba[nome][7] == 0:
                        self.matriz.create_oval(30, 30, 120, 120, tag=nome, fill='dodgerblue')
                        a = texto = self.matriz.create_text(75, 75, tag=nome, text=nome, font=('Arial', '9'),
                                                            anchor=t.CENTER)
                        self.matriz1.create_oval(30, 30, 120, 120, tag=nome, fill='dodgerblue')
                        a = texto = self.matriz1.create_text(75, 75, tag=nome, text=nome, font=('Arial', '9'),
                                                             anchor=t.CENTER)
                    elif self.comba[nome][7] == 1:
                        self.matriz.create_oval(30, 30, 120, 120, tag=nome, fill='red')
                        a = texto = self.matriz.create_text(75, 75, tag=nome, text=nome, font=('Arial', '9'),
                                                            anchor=t.CENTER)
                        self.matriz1.create_oval(30, 30, 120, 120, tag=nome, fill='red')
                        a = texto = self.matriz1.create_text(75, 75, tag=nome, text=nome, font=('Arial', '9'),
                                                             anchor=t.CENTER)
                elif self.comba[nome][6] == '3':
                    if self.comba[nome][7] == 0:
                        self.matriz.create_oval(30, 30, 150, 150, tag=nome, fill='dodgerblue')
                        a = texto = self.matriz.create_text(90, 90, tag=nome, text=nome, font=('Arial', '10'),
                                                            anchor=t.CENTER)
                        self.matriz1.create_oval(30, 30, 150, 150, tag=nome, fill='dodgerblue')
                        a = texto = self.matriz1.create_text(90, 90, tag=nome, text=nome, font=('Arial', '10'),
                                                             anchor=t.CENTER)
                    elif self.comba[nome][7] == 1:
                        self.matriz.create_oval(30, 30, 150, 150, tag=nome, fill='red')
                        a = texto = self.matriz.create_text(90, 90, tag=nome, text=nome, font=('Arial', '10'),
                                                            anchor=t.CENTER)
                        self.matriz1.create_oval(30, 30, 150, 150, tag=nome, fill='red')
                        a = texto = self.matriz1.create_text(90, 90, tag=nome, text=nome, font=('Arial', '10'),
                                                             anchor=t.CENTER)
                elif self.comba[nome][6] == '4':
                    if self.comba[nome][7] == 0:
                        self.matriz.create_oval(30, 30, 180, 180, tag=nome, fill='dodgerblue')
                        a = texto = self.matriz.create_text(105, 105, tag=nome, text=nome, font=('Arial', '11'),
                                                            anchor=t.CENTER)
                        self.matriz1.create_oval(30, 30, 180, 180, tag=nome, fill='dodgerblue')
                        a = texto = self.matriz1.create_text(105, 105, tag=nome, text=nome, font=('Arial', '11'),
                                                             anchor=t.CENTER)
                    elif self.comba[nome][7] == 1:
                        self.matriz.create_oval(30, 30, 180, 180, tag=nome, fill='red')
                        a = texto = self.matriz.create_text(105, 105, tag=nome, text=nome, font=('Arial', '11'),
                                                            anchor=t.CENTER)
                        self.matriz1.create_oval(30, 30, 180, 180, tag=nome, fill='red')
                        a = texto = self.matriz1.create_text(105, 105, tag=nome, text=nome, font=('Arial', '11'),
                                                             anchor=t.CENTER)
                self.tagtext[nome] = a
        else:
            a = map(int, self.listboxp.curselection())
            c = self.listboxp.get(a[0], last=None)
            c = c.split(' - ')
            nome = c[0]
            try:
                if self.tagtext[nome] == True:
                    pass
            except:
                if self.comba[nome][6] == '0':
                    if self.comba[nome][7] == 0:
                        self.matriz.create_oval(30, 30, 60, 60, tag=nome, fill='dodgerblue')
                        a = texto = self.matriz.create_text(45, 45, tag=nome, text=nome, font=('Arial', '7'),
                                                            anchor=t.CENTER)
                    elif self.comba[nome][7] == 1:
                        self.matriz.create_oval(30, 30, 60, 60, tag=nome, fill='red')
                        a = texto = self.matriz.create_text(45, 45, tag=nome, text=nome, font=('Arial', '7'),
                                                            anchor=t.CENTER)
                elif self.comba[nome][6] == '1':
                    if self.comba[nome][7] == 0:
                        self.matriz.create_oval(30, 30, 90, 90, tag=nome, fill='dodgerblue')
                        a = texto = self.matriz.create_text(60, 60, tag=nome, text=nome, font=('Arial', '8'),
                                                            anchor=t.CENTER)
                    elif self.comba[nome][7] == 1:
                        self.matriz.create_oval(30, 30, 90, 90, tag=nome, fill='red')
                        a = texto = self.matriz.create_text(60, 60, tag=nome, text=nome, font=('Arial', '8'),
                                                            anchor=t.CENTER)
                elif self.comba[nome][6] == '2':
                    if self.comba[nome][7] == 0:
                        self.matriz.create_oval(30, 30, 120, 120, tag=nome, fill='dodgerblue')
                        a = texto = self.matriz.create_text(75, 75, tag=nome, text=nome, font=('Arial', '9'),
                                                            anchor=t.CENTER)
                    elif self.comba[nome][7] == 1:
                        self.matriz.create_oval(30, 30, 120, 120, tag=nome, fill='red')
                        a = texto = self.matriz.create_text(75, 75, tag=nome, text=nome, font=('Arial', '9'),
                                                            anchor=t.CENTER)
                elif self.comba[nome][6] == '3':
                    if self.comba[nome][7] == 0:
                        self.matriz.create_oval(30, 30, 150, 150, tag=nome, fill='dodgerblue')
                        a = texto = self.matriz.create_text(90, 90, tag=nome, text=nome, font=('Arial', '10'),
                                                            anchor=t.CENTER)
                    elif self.comba[nome][7] == 1:
                        self.matriz.create_oval(30, 30, 150, 150, tag=nome, fill='red')
                        a = texto = self.matriz.create_text(90, 90, tag=nome, text=nome, font=('Arial', '10'),
                                                            anchor=t.CENTER)
                elif self.comba[nome][6] == '4':
                    if self.comba[nome][7] == 0:
                        self.matriz.create_oval(30, 30, 180, 180, tag=nome, fill='dodgerblue')
                        a = texto = self.matriz.create_text(105, 105, tag=nome, text=nome, font=('Arial', '11'),
                                                            anchor=t.CENTER)
                    elif self.comba[nome][7] == 1:
                        self.matriz.create_oval(30, 30, 180, 180, tag=nome, fill='red')
                        a = texto = self.matriz.create_text(105, 105, tag=nome, text=nome, font=('Arial', '11'),
                                                            anchor=t.CENTER)
                self.tagtext[nome] = a

    #Botão Adicionar Personagens
    def altini(self):
        try:
            INICI = self.campo_altini.get()
            a = map(int, self.listboxp.curselection())
            c = self.listboxp.get(a[0], last=None)
            d = c.split(' - ')
            self.comba[d[0]][3] = int(INICI)
            self.ordem[d[0]] = [int(INICI)]
            self.listboxp.delete(t.ANCHOR)
            self.listboxp.insert(a[0], str(self.comba[d[0]][0]) + ' - ' + str(self.comba[d[0]][1]))
        except:
            tkMessageBox.showerror("Faltou Informações",
                                   "Certifique-se que o campo Alterar iniciativa esta preenchido com um numero inteiro e que um combatente esteja selecionado.")
        z = self.ordem
        y = z
        w = {}
        a = 1
        z = sorted(self.ordem.values())
        z = z[::-1]
        for i in z:
            for x in y:
                if y[x] == i:
                    w[x] = a
                    a += 1
        for i in w:
            for x in self.comba:
                if i == x:
                    self.comba[x][4] = w[i]

        self.listboxp.delete(0, t.END)
        for i in range(a):
            for x in self.comba:
                if i + 1 == self.comba[x][4]:
                    self.listboxp.insert(t.END, str(self.comba[x][0]) + ' - ' + str(self.comba[x][1]))

                    #Botão adicionar personagem

    def adicionarper(self):
        try:
            PV = int(self.campo_pv.get())
        except:
            tkMessageBox.showerror("Faltou Informações",
                                   "Certifique-se que o campo Pontos de Vida esta preenchido com um numero inteiro.")
        try:
            NIVEL = float(self.campo_nivel.get())
        except:
            tkMessageBox.showerror("Faltou Informações",
                                   "Certifique-se que o campo Nivel esta preenchido com um numero Real.")
        try:
            INICI = int(self.campo_iniciativa.get())
        except:
            tkMessageBox.showerror("Faltou Informações",
                                   "Certifique-se que o campo Iniciativa esta preenchido com um numero inteiro.")
        try:
            NOME = str(self.campo_nome.get())
            if NOME == '':
                del (NOME)
                NOME += 1
        except:
            tkMessageBox.showerror("Faltou Informações",
                                   'Certifique-se que o campo "Nome" esta preenchido com um texto.')
        try:
            for i in self.comba:
                if i == NOME:
                    del (NOME)
                    NOME += 1
        except:
            tkMessageBox.showerror("Nome Repetido",
                                   'Certifique-se que o campo "Nome" esta preenchido com um nome que não exista.\nCaso seja um personagem padrão, coloque um numero para diferênciar.')
        try:
            TAMANHO = self.tamanho.get()
            self.comba[NOME] = [NOME, PV, NIVEL, INICI, 0, ['', 0], TAMANHO, 0]
            self.ordem[NOME] = [INICI]
            self.listboxp.insert(t.END, str(NOME) + ' - ' + str(PV))
        except:
            pass

    #Botão Adicionar NPC    
    def adicionarmon(self):
        try:
            PV = int(self.campo_pv.get())
        except:
            tkMessageBox.showerror("Faltou Informações",
                                   "Certifique-se que o campo Pontos de Vida esta preenchido com um numero inteiro.")
        try:
            NIVEL = float(self.campo_nivel.get())
        except:
            tkMessageBox.showerror("Faltou Informações",
                                   "Certifique-se que o campo Nivel esta preenchido com um numero Real.")
        try:
            INICI = int(self.campo_iniciativa.get())
        except:
            tkMessageBox.showerror("Faltou Informações",
                                   "Certifique-se que o campo Iniciativa esta preenchido com um numero inteiro.")
        try:
            NOME = str(self.campo_nome.get())
            if NOME == '':
                del (NOME)
                NOME += 1
        except:
            tkMessageBox.showerror("Faltou Informações",
                                   'Certifique-se que o campo "Nome" esta preenchido com um texto.')
        try:
            for i in self.comba:
                if i == NOME:
                    del (NOME)
                    NOME += 1
        except:
            tkMessageBox.showerror("Nome Repetido",
                                   'Certifique-se que o campo "Nome" esta preenchido com um nome que não exista.\nCaso seja um personagem padrão, coloque um numero para diferênciar.')
        try:
            TAMANHO = self.tamanho.get()
            self.comba[NOME] = [NOME, PV, NIVEL, INICI, 0, ['', 0], TAMANHO, 1]
            self.ordem[NOME] = [INICI]
            self.listboxp.insert(t.END, str(NOME) + ' - ' + str(PV))
        except:
            pass

            #Botão Ordenar

    def ordenar(self):
        z = self.ordem
        y = z
        w = {}
        a = 1
        z = sorted(self.ordem.values())
        z = z[::-1]
        for i in z:
            for x in y:
                if y[x] == i:
                    w[x] = a
                    a += 1
        for i in w:
            for x in self.comba:
                if i == x:
                    self.comba[x][4] = w[i]

        self.listboxp.delete(0, t.END)
        for i in range(a):
            for x in self.comba:
                if i + 1 == self.comba[x][4]:
                    self.listboxp.insert(t.END, str(self.comba[x][0]) + ' - ' + str(self.comba[x][1]))

    #Botão Passar Turno           
    def passturn(self):
        fonte1 = ('Ariel', '9', 'bold')
        a = self.listboxp.get(0, t.END)
        b = self.listboxp.get(self.turno)
        b = b.split(' - ')
        b = b[0]
        self.NOME = self.comba[b][0]
        STATUS = self.comba[b][5][0]
        TURSTA = self.comba[b][5][1]
        SANGUE = self.comba[b][1]
        if SANGUE <= 0:
            self.turno1 += 1
            c = '%s' % self.NOME
            d = 'Está fora de combate'
            if TURSTA > 0:
                self.comba[b][5][1] -= 1
        else:
            self.turno1 += 1
            if TURSTA > 0:
                c = '%s' % self.NOME
                d = '%s por %i turnos' % (STATUS, int(TURSTA))
                self.comba[b][5][1] -= 1
            else:
                c = self.NOME
                d = ''
        try:
            self.vez.destroy()
            self.vez1.destroy()
            self.vez2.destroy()
        except:
            pass
        self.vez = t.Label(self.frame2_2_1_2_2_2, text='Turno: ' + str(self.turno1), fg='darkblue')
        self.vez.pack()
        self.vez1 = t.Label(self.frame2_2_1_2_2_2, text=c, fg='darkblue', font=('Verdana', '12', 'bold'))
        self.vez1.pack()
        self.vez2 = t.Label(self.frame2_2_1_2_2_2, text=d, fg='darkblue')
        self.vez2.pack()
        if self.turno < len(a) - 1:
            self.turno += 1
        else:
            self.turno = 0

    #Botão Adicionar Status    
    def addstatus(self):
        try:
            a = map(int, self.listboxp.curselection())
            c = self.listboxp.get(a[0], last=None)
            c = c.split(' - ')
            self.nomestat = c[0]
            self.z = t.Tk()
            self.z.title('Status')
            self.z.resizable(width=False, height=False)
            frame1 = t.Frame(self.z)
            frame1.pack()
            frame2 = t.Frame(self.z)
            frame2.pack()
            frame21 = t.Frame(frame2)
            frame21.pack(side=t.LEFT)
            frame22 = t.Frame(frame2)
            frame22.pack(side=t.LEFT)
            frame3 = t.Frame(self.z)
            frame3.pack()
            titulo = t.Label(frame1, text='Preencha o Status', width=20, height=2)
            titulo.pack()
            desst = t.Label(frame21, text='Descrição do Status', width=20, height=2)
            desst.pack()
            self.campo_desst = t.Entry(frame21, width=20)
            self.campo_desst.pack()
            turnat = t.Label(frame22, text='Duração(turnos)', width=20, height=2)
            turnat.pack()
            self.campo_turnat = t.Entry(frame22, width=10)
            self.campo_turnat.pack()
            botaostatus = t.Button(frame3, width=14, text='ADD Status', command=self.status)
            botaostatus.pack()
        except:
            tkMessageBox.showinfo("Combatente não selecionado", "Certifique-se que você escolheu um combatente.")

    #Botão Status 
    def status(self):
        self.comba[self.nomestat][5][0] = self.campo_desst.get()
        self.comba[self.nomestat][5][1] = int(self.campo_turnat.get())
        self.z.destroy()

    #Botão Passar Dias    
    def passar_dias(self):
        try:
            DIASPASS = self.campo_dias.get()
            DIASPASS = int(DIASPASS)
            self.listboxp.delete(0, t.END)
            for i in self.comba:
                self.comba[i][1] = self.comba[i][1] + (int(self.comba[i][2]) * DIASPASS)
                self.listboxp.insert(t.END, str(self.comba[i][0]) + ' - ' + str(self.comba[i][1]))
        except:
            tkMessageBox.showerror("Faltou Informações",
                                   "Certifique-se que o campo Passar Dias esta preenchido com um numero inteiro.")

    #Botão Curar
    def curar(self):
        try:
            CURA = self.campo_recuperacao.get()
            a = map(int, self.listboxp.curselection())
            c = self.listboxp.get(a[0], last=None)
            d = c.split(' - ')
            self.comba[d[0]][1] += int(CURA)
            self.listboxp.delete(t.ANCHOR)
            self.listboxp.insert(a[0], str(self.comba[d[0]][0]) + ' - ' + str(self.comba[d[0]][1]))
        except:
            tkMessageBox.showerror("Faltou Informações",
                                   "Certifique-se que o campo Curar esta preenchido com um numero inteiro e que um combatente esteja selecionado.")

    #Botão Dano
    def dano_recebido(self):
        try:
            DANO = self.campo_dano.get()
            a = map(int, self.listboxp.curselection())
            c = self.listboxp.get(a[0], last=None)
            d = c.split(' - ')
            self.comba[d[0]][1] -= int(DANO)
            self.listboxp.delete(t.ANCHOR)
            self.listboxp.insert(a[0], str(self.comba[d[0]][0]) + ' - ' + str(self.comba[d[0]][1]))
        except:
            tkMessageBox.showerror("Faltou Informações",
                                   "Certifique-se que o campo Causar Dano esta preenchido com um numero inteiro e que um combatente esteja selecionado.")

    #Botão Remover
    def remover(self):
        try:
            b = map(int, self.listboxp.curselection())
            c = self.listboxp.get(b[0], last=None)
            d = c.split(' - ')
            del self.comba[d[0]]
            self.listboxp.delete(t.ANCHOR)
        except:
            tkMessageBox.showinfo("Combatente não selecionado", "Certifique-se que você escolheu um combatente.")

    #Botão Calculo de XP
    def calculoxp(self):
        NDC = 0
        NDP = 0
        GXP = 0
        XP = 0
        XPCJ = 0
        z = self.comba.keys()
        for i in z:
            if self.comba[i][7] == 0:
                NDP += self.comba[i][2]
                if self.comba[i][1] > 0:
                    GXP += 1
            elif self.comba[i][7] == 1:
                NDC += self.comba[i][2]
        if NDC <= NDP - 5:
            tkMessageBox.showinfo("Luta Fácil", "Esta luta foi muito fácil, nada de XP desta vez")
        else:
            XP = NDC * 300
            XPCJ = XP / GXP
            tkMessageBox.showinfo("XP ganho",
                                  "Esse combate da um total de %i XP \n Cada jogador que sobrevivel recebe %i XP" % (
                                      XP, XPCJ))

    #Botão Abrir         
    def abrir(self):
        jan = t.Tk()
        jan.withdraw()
        filename = tkFileDialog.askopenfilename(parent=jan, title='Open file to encrypt')
        try:
            b = pickle.load(open(filename))
            self.comba = b[0]
            self.ordem = b[1]
            self.turno = b[2]
            self.turno1 = b[3]
            self.tagtext = b[4]
            z = self.ordem
            y = z
            w = {}
            a = 1
            z = sorted(self.ordem.values())
            z = z[::-1]
            for i in z:
                for x in y:
                    if y[x] == i:
                        w[x] = a
                        a += 1
            for i in w:
                for x in self.comba:
                    if i == x:
                        self.comba[x][4] = w[i]
            self.listboxp.delete(0, t.END)
            for i in range(a):
                for x in self.comba:
                    if i + 1 == self.comba[x][4]:
                        self.listboxp.insert(t.END, str(self.comba[x][0]) + ' - ' + str(self.comba[x][1]))
            fonte1 = ('Ariel', '9', 'bold')
            a = self.listboxp.get(0, t.END)
            b = self.listboxp.get(self.turno)
            b = b.split(' - ')
            b = b[0]
            self.NOME = self.comba[b][0]
            STATUS = self.comba[b][5][0]
            TURSTA = self.comba[b][5][1]
            SANGUE = self.comba[b][1]
            if SANGUE <= 0:
                self.turno1 += 1
                c = '%s' % self.NOME
                d = 'Está fora de combate'
                if TURSTA > 0:
                    self.comba[b][5][1] -= 1
            else:
                self.turno1 += 1
                if TURSTA > 0:
                    c = '%s' % self.NOME
                    d = '%s por %i turnos' % (STATUS, int(TURSTA))
                    self.comba[b][5][1] -= 1
                else:
                    c = self.NOME
                    d = ''
            try:
                self.vez.destroy()
                self.vez1.destroy()
                self.vez2.destroy()
            except:
                pass
            self.vez = t.Label(self.frame2_2_1_2_2_2, text='Turno: ' + str(self.turno1), fg='darkblue')
            self.vez.pack()
            self.vez1 = t.Label(self.frame2_2_1_2_2_2, text=c, fg='darkblue', font=('Verdana', '12', 'bold'))
            self.vez1.pack()
            self.vez2 = t.Label(self.frame2_2_1_2_2_2, text=d, fg='darkblue')
            self.vez2.pack()
            if self.turno < len(a) - 1:
                self.turno += 1
            else:
                self.turno = 0
        except IOError:
            pass

    def salvar(self):
        a = [self.comba, self.ordem, self.turno, self.turno1, self.tagtext]
        z = t.Tk()
        z.withdraw()
        savename = tkFileDialog.asksaveasfilename(parent=z, title='Salvar combate')
        try:
            pickle.dump(a, open(savename, 'w'))
        except IOError:
            pass


    def ajuda(self):
        webbrowser.open('http://dadosedesventuras.blogspot.com.br/p/ajuda-controle-de-combate.html')

    def sobre(self):
        tkMessageBox.showinfo("Sobre",
                              "Controle de Combate foi criado por Lário Diniz e distribuído pela Dados&Desventuras.\n\n Para criticas, sugestões de programas que ajudem mestre e jogadores ou reportar erros, enviar email para dadosedesventuras@gmail.com.\n\n O Sistema utilizado para calculo de XP é o do Tormenta RPG.\n\nEntre no Blog dadosedesventuras.blogspot.com.br para mais informações.")


swallow = t.Tk()
MontyPython(swallow)
swallow.mainloop()
