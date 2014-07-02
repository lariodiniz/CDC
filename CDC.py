# -*- coding:UTF-8 -*-

from __future__ import unicode_literals
from operator import attrgetter
import gettext
import locale
import os
import pickle
import random
import six
import webbrowser

if six.PY3:
    import tkinter as t
    import tkinter.messagebox as tkMessageBox
    import tkinter.filedialog as tkFileDialog
elif six.PY2:
    import Tkinter as t
    import tkMessageBox
    import tkFileDialog

# SetUP the I18N support. On windows, the LANG environment variable doesnt exist
# and must be got through locale.getdefaultlocale, otherwise the translations
# will not appear (courtesy of the fallback=True).
PROJECT_ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
if not os.getenv('LANG'):
    lang, enc = locale.getdefaultlocale()
    os.environ['LANG'] = lang

translate = gettext.translation('cdc',
                                os.path.join(PROJECT_ROOT_PATH, 'locale'),
                                fallback=True)
_ = translate.gettext


class Character(object):
    """ Base class for players or monsters creation.

    CHAR_STATUS_TYPE = (
        ('Player', 0),
        ('NPC', 1)
    )
    """

    name = None
    level = None
    hp = None
    init_value = None
    ammo = None
    char_type = None
    size = None
    errors = None

    def __init__(self):
        self.status = set()

    def __repr__(self):
        return "%s - %s.%s" % (self.name, self.hp, self.init_value)

    def clean_int_fields(self, field):
        try:
            field = int(field)
            return field
        except ValueError:
            self.errors = "A INT value must be provided for the field %s" \
                          % field
            return False
        except TypeError:
            self.errors = "No value defined for field %s" % field
            return False

    @property
    def cleaned_data(self):
        """ Check all the fields and runs clean methods for each one """
        if None in [self.name, self.level, self.hp, self.init_value,
                    self.char_type, self.size]:
            self.errors = "All attributes muste be provided."
            return False

        self.level = self.clean_int_fields(self.level)
        self.hp = self.clean_int_fields(self.hp)
        self.init_value = self.clean_int_fields(self.init_value)
        self.char_type = self.clean_int_fields(self.char_type)
        return True

    def clean_char_type(self):
        """
        Verify if the chartype defined is one of the expected options.
        """
        raise NotImplementedError

    def clean_status(self):
        raise NotImplementedError


# TODO: SomeFields and strings maybe in EN_US with i18n support i guess.
class MontyPython(object):
    """
        Programa para Mestres de Tormenta RPG, que consiste em uma serie de
        ferramentas para ajudar nos combates.
    """

    def __init__(self, janela):
        # variaveis utilizadas em todo o programa
        self.turno = 0
        self.turno1 = 0
        self.comba = {
            'Indice': ['NOME', 'PV', 'NIVEL', 'INICI', 'ORDEM DA INICIATIVA',
                       ['DESCRIÇÂOSTATUS', 'TURNO DURAÇÂO STATUS'], 'TAMANHO',
                       'TIPO DE PERSONAGEM', 'MUNIÇÃO']
        }
        self.ordem = {}
        self.tagtext = {}
        self.janela = janela
        self.chars = None
        # Opçõs de janela
        self.janela.title('Controle de Combate - Beta 0.3')
        self.janela.resizable(width=False, height=False)

        # Menu Superior
        principal = t.Menu(janela)
        arquivo = t.Menu(principal)
        arquivo.add_command(label="Abrir", command=self.open)
        arquivo.add_command(label="Salvar", command=self.save)
        arquivo.add_command(label="Sair", command=self.quit)
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
        self.frame2_2_1_2_1 = t.Frame(self.frame2_2_1_2, borderwidth=3,
                                      relief=t.RAISED)
        self.frame2_2_1_2_1.pack(side=t.LEFT, pady=5, padx=5)
        self.frame2_2_1_2_1_1 = t.Frame(self.frame2_2_1_2_1)
        self.frame2_2_1_2_1_1.pack()
        self.frame2_2_1_2_1_2 = t.Frame(self.frame2_2_1_2_1)
        self.frame2_2_1_2_1_2.pack()
        self.frame2_2_1_2_1_3 = t.Frame(self.frame2_2_1_2_1)
        self.frame2_2_1_2_1_3.pack()
        self.frame2_2_1_2_2 = t.Frame(self.frame2_2_1_2, borderwidth=3,
                                      relief=t.GROOVE)
        self.frame2_2_1_2_2.pack(side=t.LEFT, fill=t.X, expand=True, pady=5,
                                 padx=5)
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

        self.vez_text = t.StringVar()
        self.vez1_text = t.StringVar()
        self.vez2_text = t.StringVar()

        self.vez_text.set('Turno: 1', )
        self.vez1_text.set('Not Selected')
        self.vez2_text.set('Not Selected')

        self.vez = t.Label(self.frame2_2_1_2_2_2,
                           textvariable=self.vez_text,
                           fg='darkblue')
        self.vez.pack()
        self.vez1 = t.Label(self.frame2_2_1_2_2_2,
                            textvariable=self.vez1_text,
                            fg='darkblue',
                            font=('Verdana', '12', 'bold'))
        self.vez1.pack()
        self.vez2 = t.Label(self.frame2_2_1_2_2_2,
                            textvariable=self.vez2_text,
                            fg='darkblue')
        self.vez2.pack()
        #Fontes
        fonte1 = ('Arial', '9', 'bold')
        fonte2 = ('Arial', '10', 'bold')

        #Titulo
        self.titulo = t.Label(self.frame1, text='Controle de Combate - Beta',
                              fg='darkblue', font=('Verdana', '14', 'bold'))
        self.titulo.pack()
        self.titulob = t.Label(self.frame1,
                               text='Acessem dadosedesventuras.blogspot.com',
                               font=('Verdana', '9'))
        self.titulob.pack()

        #Campo Adicionar Combatente (contido no frame2_1_1)
        self.t_add_com = t.Label(self.frame2_1_1_1, text='Adicionar Combatente',
                                 font=fonte2, height=2)
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
        self.iniciativa = t.Label(self.frame2_1_1_2_1_1_4, text='Iniciativa',
                                  font=fonte1)
        self.iniciativa.pack()
        self.campo_iniciativa = t.Entry(self.frame2_1_1_2_1_1_4, width=10)
        self.campo_iniciativa.pack()
        self.municao = t.Label(self.frame2_1_1_2_1_1_5, text='Munição',
                               font=fonte1)
        self.municao.pack()
        self.campo_municao = t.Entry(self.frame2_1_1_2_1_1_5, width=10)
        self.campo_municao.pack()
        self.tamanho = t.StringVar(self.frame2_1_1_2_1_2)
        self.tamanho.set(0)
        for txt, val in (
                ('Medio ou menor', '0'), ('Grande', '1'), ('Enorme', '2'),
                ('Descomunal', '3'), ('Colossal', '4')):
            a = t.Radiobutton(self.frame2_1_1_2_1_2, text=txt, value=val,
                              variable=self.tamanho)
            a.pack(side=t.LEFT)
        self.botaopersonagem = t.Button(self.frame2_1_1_2_2, text='Personagem',
                                        width=10,
                                        command=lambda: self.add_char(0))
        self.botaopersonagem.pack(pady=5, padx=10)
        self.botaomonstro = t.Button(self.frame2_1_1_2_2, text='NPC', width=10,
                                     command=lambda: self.add_char(1))
        self.botaomonstro.pack(pady=5, padx=10)

        #Campo Controle de Status(contido no frame2_1_2)
        self.t_con_sta = t.Label(self.frame2_1_2_1, text='Controle de Status',
                                 font=fonte2, height=2)
        self.t_con_sta.pack()
        self.t_con_sta1 = t.Label(self.frame2_1_2_2_1_1, text='Pontos de Vida',
                                  font=fonte2)
        self.t_con_sta1.pack()
        self.botaocura = t.Button(self.frame2_1_2_2_1_2_1, width=14,
                                  text='Curar', command=self.add_hitpoints)
        self.botaocura.pack(side=t.LEFT)
        self.campo_recuperacao = t.Entry(self.frame2_1_2_2_1_2_1, width=10)
        self.campo_recuperacao.pack(side=t.LEFT)
        self.botaodano = t.Button(self.frame2_1_2_2_1_2_2, width=14,
                                  text='Causar Dano',
                                  command=self.subtract_hitpoints)
        self.botaodano.pack(side=t.LEFT)
        self.campo_dano = t.Entry(self.frame2_1_2_2_1_2_2, width=10)
        self.campo_dano.pack(side=t.LEFT)
        self.t_con_sta2 = t.Label(self.frame2_1_2_2_2_1, text='Outros',
                                  font=fonte2)
        self.t_con_sta2.pack()
        self.botaoaltini = t.Button(self.frame2_1_2_2_2_2_1, width=14,
                                    text='Alterar Iniciativa',
                                    command=self.change_initiative)
        self.botaoaltini.pack(side=t.LEFT)
        self.campo_altini = t.Entry(self.frame2_1_2_2_2_2_1, width=10)
        self.campo_altini.pack(side=t.LEFT)
        self.botaomonstro = t.Button(self.frame2_1_2_2_2_2_2,
                                     text='Passar Dias', width=14,
                                     command=self.passar_dias)
        self.botaomonstro.pack(side=t.LEFT)
        self.campo_dias = t.Entry(self.frame2_1_2_2_2_2_2, width=10)
        self.campo_dias.pack(side=t.LEFT)
        self.botaoaddsta = t.Button(self.frame2_1_2_3, text='ADD Outros Status',
                                    command=self._create_add_status_window)
        self.botaoaddsta.pack(pady=5, padx=5)

        #Campo Controle de Turno(contido no frame2_1_3)
        self.t_con_turn = t.Label(self.frame2_1_3_1, text='Controle de Turnos',
                                  font=fonte2, height=2)
        self.t_con_turn.pack()
        self.botaoordcomb = t.Button(self.frame2_1_3_2, text='Ordenar',
                                     command=self.sort)
        self.botaoordcomb.pack(side=t.LEFT, pady=5, padx=5)
        self.botaopassturn = t.Button(self.frame2_1_3_2, text='Passar Turno',
                                      command=self.shift_turn)
        self.botaopassturn.pack(side=t.LEFT, pady=5, padx=5)

        #Campo Combate(contido no frame2_2_1)
        self.t_con = t.Label(self.frame2_2_1_1, text='Combate', font=fonte2)
        self.t_con.pack()
        self.controlecom = t.Label(self.frame2_2_1_2_1_1,
                                   text='Lista de Combate', font=fonte1)
        self.controlecom.pack()
        self.explitabp = t.Label(self.frame2_2_1_2_1_1, text='Nome - PV ')
        self.explitabp.pack()
        self.scrollbarp = t.Scrollbar(self.frame2_2_1_2_1_2)
        self.scrollbarp.pack(side=t.RIGHT)
        self.listboxp = t.Listbox(self.frame2_2_1_2_1_2, exportselection=0)
        self.listboxp.pack()
        self.listboxp.config(yscrollcommand=self.scrollbarp.set)
        self.scrollbarp.config(command=self.listboxp.yview)
        self.botaoremover = t.Button(self.frame2_2_1_2_1_3, text='Remover',
                                     font=fonte1, command=self.delete_char)
        self.botaoremover.pack()
        self.vez = t.Label(self.frame2_2_1_2_2_1, text='Turno do combatente:',
                           font=fonte1)
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
        self.t_out = t.Label(self.frame2_2_3_1, text='Outros', font=fonte2,
                             width=10)
        self.t_out.pack()
        self.botaoxp = t.Button(self.frame2_2_3_2, text='Calcular XP',
                                font=fonte1, command=self.calculate_xp)
        self.botaoxp.pack(side=t.LEFT, pady=5, padx=5)
        self.botaocritico = t.Button(self.frame2_2_3_2, text='Acerto Critico',
                                     font=fonte1, command=self.critico)
        self.botaocritico.pack(side=t.LEFT, pady=5, padx=5)


    # TODO: Rewrite
    def critico(self):
        self.janelacr = t.Tk()
        self.janelacr.title('Critico')
        self.janelacr.resizable(width=False, height=False)
        self.framejanelacrd1 = t.Frame(self.janelacr, borderwidth=3,
                                       relief=t.GROOVE)
        self.framejanelacrd1.pack(fill=t.X, pady=5, padx=5)
        self.framejanelacr1 = t.Frame(self.framejanelacrd1)
        self.framejanelacr1.pack()
        self.framejanelacr1e = t.Frame(self.framejanelacrd1)
        self.framejanelacr1e.pack()
        self.framejanelacrd2 = t.Frame(self.janelacr, borderwidth=3,
                                       relief=t.GROOVE)
        self.framejanelacrd2.pack(fill=t.X, pady=5, padx=5)
        self.framejanelacr2 = t.Frame(self.framejanelacrd2)
        self.framejanelacr2.pack()
        self.framejanelacr2e = t.Frame(self.framejanelacrd2)
        self.framejanelacr2e.pack()
        self.framejanelacrd3 = t.Frame(self.janelacr, borderwidth=3,
                                       relief=t.GROOVE)
        self.framejanelacrd3.pack(fill=t.X, pady=5, padx=5)
        self.framejanelacr3 = t.Frame(self.framejanelacrd3)
        self.framejanelacr3.pack()
        self.framejanelacr3e = t.Frame(self.framejanelacrd3)
        self.framejanelacr3e.pack()
        self.framejanelacrd4 = t.Frame(self.janelacr, borderwidth=3,
                                       relief=t.GROOVE)
        self.framejanelacrd4.pack(fill=t.X, pady=5, padx=5)
        self.framejanelacr4 = t.Frame(self.framejanelacrd4)
        self.framejanelacr4.pack()
        self.framejanelacr4e = t.Frame(self.framejanelacrd4)
        self.framejanelacr4e.pack()
        self.framejanelacrd5 = t.Frame(self.janelacr, borderwidth=3,
                                       relief=t.GROOVE)
        self.framejanelacrd5.pack(fill=t.X, pady=5, padx=5)
        self.framejanelacr5 = t.Frame(self.framejanelacrd5)
        self.framejanelacr5.pack()
        self.framejanelacr5e = t.Frame(self.framejanelacrd5)
        self.framejanelacr5e.pack()
        self.framejanelacr6 = t.Frame(self.janelacr)
        self.framejanelacr6.pack()

        armaa = t.Label(self.framejanelacr1, text=_('weapon_dmg_type'))
        armaa.pack()
        self.arma = t.StringVar(self.framejanelacr1e)
        self.arma.set(0)
        for txt1, val1 in ((_('Corte'), '0'), (_('Esmagamento'), '1'),
                           (_('Perfuração'), '2'),
                           (_('Energia'), '3')):
            arma = t.Radiobutton(self.framejanelacr1e, text=txt1, value=val1,
                                 variable=self.arma)
            arma.pack(side=t.LEFT)
        multic = t.Label(self.framejanelacr2, text=_('weapon_multiplier'))
        multic.pack()
        self.multi = t.StringVar(self.framejanelacr2e)
        self.multi.set(0)
        for txt2, val2 in (('x2', '0'), ('x3', '1'), ('x4', '2')):
            multi = t.Radiobutton(self.framejanelacr2e, text=txt2, value=val2,
                                  variable=self.multi)
            multi.pack(side=t.LEFT)
        tam = t.Label(self.framejanelacr3, text=_('atker_size'))
        tam.pack()
        self.taman = t.StringVar(self.framejanelacr3e)
        self.taman.set(0)
        for txt3, val3 in (
                (_('Mínimo ou menor'), '0'), (_('Pequeno'), '1'),
                (_('Média'), '2'), (_('Grande'), '3'),
                (_('Enorme ou Maior'), '4')):
            taman = t.Radiobutton(self.framejanelacr3e, text=txt3, value=val3,
                                  variable=self.taman)
            taman.pack(side=t.LEFT)
        arm = t.Label(self.framejanelacr4, text=_('def_height'))
        arm.pack()
        self.armad = t.StringVar(self.framejanelacr4e)
        self.armad.set(0)
        for txt4, val4 in ((_('Nenhuma'), '0'), (_('Leve'), '1'),
                           (_('Média'), '2'), (_('Pesada'), '3')):
            armad = t.Radiobutton(self.framejanelacr4e, text=txt4, value=val4,
                                  variable=self.armad)
            armad.pack(side=t.LEFT)
        esc = t.Label(self.framejanelacr5, text=_('def_shield'))
        esc.pack()
        self.escu = t.StringVar(self.framejanelacr5e)
        self.escu.set(0)
        for txt5, val5 in ((_('Nenhum'), '0'), (_('Escudo Braço Direito'), '1'),
                           (_('Escudo Braço esquerdo'), '2')):
            escu = t.Radiobutton(self.framejanelacr5e, text=txt5, value=val5,
                                 variable=self.escu)
            escu.pack(side=t.LEFT)

        self.gerarcri = t.Button(self.framejanelacr6, text=_('Gerar Critico'),
                                 command=self.gecritico)
        self.gerarcri.pack(side=t.LEFT, pady=5, padx=5)

    #TODO: Rewrite
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

        legr = _("Critico na perna direita")
        legl = _("Critico na perna esquerda")
        body = _("Critico no Tronco")
        head = _("Critico na Cabeça")
        armr = _("Critico no braço direito")
        arml = _("Critico na braço esquerdo")

        if ARMA == '0':
            if local == 1:
                if 1 <= severidade <= 3:
                    tkMessageBox.showinfo(legr, _("0_1_1_sev_3"))
                elif 4 <= severidade <= 6:
                    tkMessageBox.showinfo(legr, _("0_1_4_sev_6"))
                elif 7 <= severidade <= 8:
                    tkMessageBox.showinfo(legr, _("0_1_7_sev_8"))
                elif 9 <= severidade <= 10:
                    tkMessageBox.showinfo(legr, _("0_1_9_sev_10"))
                elif 11 <= severidade <= 12:
                    tkMessageBox.showinfo(legr, _("0_1_11_sev_12"))
                elif severidade >= 13:
                    tkMessageBox.showinfo(legr, _("0_1_sev_13"))
            elif local == 2:
                if 1 <= severidade <= 3:
                    tkMessageBox.showinfo(legl, _("0_2_1_sev_3"))
                elif 4 <= severidade <= 6:
                    tkMessageBox.showinfo(legl, _("0_2_4_sev_6"))
                elif 7 <= severidade <= 8:
                    tkMessageBox.showinfo(legl, _("0_2_7_sev_8"))
                elif 9 <= severidade <= 10:
                    tkMessageBox.showinfo(legl, _("0_2_9_sev_10"))
                elif 11 <= severidade <= 12:
                    tkMessageBox.showinfo(legl, _("0_2_11_sev_12"))
                elif severidade >= 13:
                    tkMessageBox.showinfo(legl, _("0_2__sev_13"))
            elif 3 <= local <= 7:
                if 1 <= severidade <= 3:
                    tkMessageBox.showinfo(body, _("0_37_1_sev_3"))
                elif 4 <= severidade <= 6:
                    tkMessageBox.showinfo(body, _("0_37_4_sev_6"))
                elif 7 <= severidade <= 8:
                    tkMessageBox.showinfo(body, _("0_37_7_sev_8"))
                elif 9 <= severidade <= 10:
                    tkMessageBox.showinfo(body, _("0_37_9_sev_10"))
                elif 11 <= severidade <= 12:
                    tkMessageBox.showinfo(body, _("0_37_11_sev_12"))
                elif severidade >= 13:
                    tkMessageBox.showinfo(body, _("0_37__sev_13"))
            elif local == 8:
                if des == 1:
                    if 1 <= severidade <= 3:
                        tkMessageBox.showinfo(armr, _("0_8_1_1_sev_3"))
                    elif 4 <= severidade <= 6:
                        tkMessageBox.showinfo(armr, _("0_8_1_4_sev_6"))
                    elif 7 <= severidade <= 8:
                        tkMessageBox.showinfo(armr, _("0_8_1_7_sev_8"))
                    elif 9 <= severidade <= 10:
                        tkMessageBox.showinfo(armr, _("0_8_1_9_sev_10"))
                    elif 11 <= severidade <= 12:
                        tkMessageBox.showinfo(armr, _("0_8_1_11_sev_12"))
                    elif severidade >= 13:
                        tkMessageBox.showinfo(armr, _("0_8_1__sev_13"))
                else:
                    if 1 <= severidade <= 3:
                        tkMessageBox.showinfo(armr, _("0_8__1_sev_3"))
                    elif 4 <= severidade <= 6:
                        tkMessageBox.showinfo(armr, _("0_8__4_sev_6"))
                    elif 7 <= severidade <= 8:
                        tkMessageBox.showinfo(armr, _("0_8__7_sev_8"))
                    elif 9 <= severidade <= 10:
                        tkMessageBox.showinfo(armr, _("0_8__9_sev_10"))
                    elif 11 <= severidade <= 12:
                        tkMessageBox.showinfo(armr, _("0_8__11_sev_12"))
                    elif severidade >= 13:
                        tkMessageBox.showinfo(armr, _("0_8____sev_13"))
            elif local == 9:
                if des == 1:
                    if 1 <= severidade <= 3:
                        tkMessageBox.showinfo(armr, _("0_9_1_1_sev_3"))
                    elif 4 <= severidade <= 6:
                        tkMessageBox.showinfo(armr, _("0_9_1_4_sev_6"))
                    elif 7 <= severidade <= 8:
                        tkMessageBox.showinfo(armr, _("0_9_1_7_sev_8"))
                    elif 9 <= severidade <= 10:
                        tkMessageBox.showinfo(armr, _("0_9_1_9_sev_10"))
                    elif 11 <= severidade <= 12:
                        tkMessageBox.showinfo(armr, _("0_9_1_11_sev_12"))
                    elif severidade >= 13:
                        tkMessageBox.showinfo(armr, _("0_9_1___sev_13"))
                else:
                    if 1 <= severidade <= 3:
                        tkMessageBox.showinfo(arml, _("0_9__1_sev_3"))
                    elif 4 <= severidade <= 6:
                        tkMessageBox.showinfo(arml, _("0_9__4_sev_6"))
                    elif 7 <= severidade <= 8:
                        tkMessageBox.showinfo(arml, _("0_9__7_sev_8"))
                    elif 9 <= severidade <= 10:
                        tkMessageBox.showinfo(arml, _("0_9__9_sev_10"))
                    elif 11 <= severidade <= 12:
                        tkMessageBox.showinfo(arml, _("0_9__11_sev_12"))
                    elif severidade >= 13:
                        tkMessageBox.showinfo(arml, _("0_9_____sev_13"))
            elif local == 10:
                if 1 <= severidade <= 3:
                    tkMessageBox.showinfo(head, _("0_10___1_sev_3"))
                elif 4 <= severidade <= 6:
                    tkMessageBox.showinfo(head, _("0_10___4_sev_6"))
                elif 7 <= severidade <= 8:
                    tkMessageBox.showinfo(head, _("0_10___7_sev_8"))
                elif 9 <= severidade <= 10:
                    tkMessageBox.showinfo(head, _("0_10___9_sev_10"))
                elif 11 <= severidade <= 12:
                    tkMessageBox.showinfo(head, _("0_10___11_sev_12"))
                elif severidade >= 13:
                    tkMessageBox.showinfo(head, _("0_10_____sev_13"))
        if ARMA == '1':
            if local == 1:
                if 1 <= severidade <= 3:
                    tkMessageBox.showinfo(legr, _("1_1__1_sev_3"))
                elif 4 <= severidade <= 6:
                    tkMessageBox.showinfo(legr, _("1_1__4_sev_6"))
                elif 7 <= severidade <= 8:
                    tkMessageBox.showinfo(legr, _("1_1__7_sev_8"))
                elif 9 <= severidade <= 10:
                    tkMessageBox.showinfo(legr, _("1_1__9_sev_10"))
                elif 11 <= severidade <= 12:
                    tkMessageBox.showinfo(legr, _("1_1__11_sev_12"))
                elif severidade >= 13:
                    tkMessageBox.showinfo(legr, _("1_1____sev_13"))
            elif local == 2:
                if 1 <= severidade <= 3:
                    tkMessageBox.showinfo(legl, _("1_2__1_sev_3"))
                elif 4 <= severidade <= 6:
                    tkMessageBox.showinfo(legl, _("1_2__4_sev_6"))
                elif 7 <= severidade <= 8:
                    tkMessageBox.showinfo(legl, _("1_2__7_sev_8"))
                elif 9 <= severidade <= 10:
                    tkMessageBox.showinfo(legl, _("1_2__9_sev_10"))
                elif 11 <= severidade <= 12:
                    tkMessageBox.showinfo(legl, _("1_2__11_sev_12"))
                elif severidade >= 13:
                    tkMessageBox.showinfo(legl, _("1_2____sev_13"))
            elif 3 <= local <= 7:
                if 1 <= severidade <= 3:
                    tkMessageBox.showinfo(body, _("1_37__1_sev_3"))
                elif 4 <= severidade <= 6:
                    tkMessageBox.showinfo(body, _("1_37__4_sev_6"))
                elif 7 <= severidade <= 8:
                    tkMessageBox.showinfo(body, _("1_37__7_sev_8"))
                elif 9 <= severidade <= 10:
                    tkMessageBox.showinfo(body, _("1_37__9_sev_10"))
                elif 11 <= severidade <= 12:
                    tkMessageBox.showinfo(body, _("1_37__11_sev_12"))
                elif severidade >= 13:
                    tkMessageBox.showinfo(body, _("1_37____sev_13"))
            elif local == 8:
                if des == 1:
                    if 1 <= severidade <= 3:
                        tkMessageBox.showinfo(armr, _("1_8_1_1_sev_3"))
                    elif 4 <= severidade <= 6:
                        tkMessageBox.showinfo(armr, _("1_8_1_4_sev_6"))
                    elif 7 <= severidade <= 8:
                        tkMessageBox.showinfo(armr, _("1_8_1_7_sev_8"))
                    elif 9 <= severidade <= 10:
                        tkMessageBox.showinfo(armr, _("1_8_1_9_sev_10"))
                    elif 11 <= severidade <= 12:
                        tkMessageBox.showinfo(armr, _("1_8_1_11_sev_12"))
                    elif severidade >= 13:
                        tkMessageBox.showinfo(armr, _("1_8_1___sev_13"))
                else:
                    if 1 <= severidade <= 3:
                        tkMessageBox.showinfo(armr, _("1_8___1_sev_3"))
                    elif 4 <= severidade <= 6:
                        tkMessageBox.showinfo(armr, _("1_8___4_sev_6"))
                    elif 7 <= severidade <= 8:
                        tkMessageBox.showinfo(armr, _("1_8___7_sev_8"))
                    elif 9 <= severidade <= 10:
                        tkMessageBox.showinfo(armr, _("1_8___9_sev_10"))
                    elif 11 <= severidade <= 12:
                        tkMessageBox.showinfo(armr, _("1_8___11_sev_12"))
                    elif severidade >= 13:
                        tkMessageBox.showinfo(armr, _("1_8_____sev_13"))
            elif local == 9:
                if des == 1:
                    if 1 <= severidade <= 3:
                        tkMessageBox.showinfo(arml, _("1_9_1_1_sev_3"))
                    elif 4 <= severidade <= 6:
                        tkMessageBox.showinfo(arml, _("1_9_1_4_sev_6"))
                    elif 7 <= severidade <= 8:
                        tkMessageBox.showinfo(arml, _("1_9_1_7_sev_8"))
                    elif 9 <= severidade <= 10:
                        tkMessageBox.showinfo(arml, _("1_9_1_9_sev_10"))
                    elif 11 <= severidade <= 12:
                        tkMessageBox.showinfo(arml, _("1_9_1_11_sev_12"))
                    elif severidade >= 13:
                        tkMessageBox.showinfo(arml, _("1_9_1___sev_13"))
                else:
                    if 1 <= severidade <= 3:
                        tkMessageBox.showinfo(arml, _("1_9___1_sev_3"))
                    elif 4 <= severidade <= 6:
                        tkMessageBox.showinfo(arml, _("1_9___4_sev_6"))
                    elif 7 <= severidade <= 8:
                        tkMessageBox.showinfo(arml, _("1_9___7_sev_8"))
                    elif 9 <= severidade <= 10:
                        tkMessageBox.showinfo(arml, _("1_9___9_sev_10"))
                    elif 11 <= severidade <= 12:
                        tkMessageBox.showinfo(arml, _("1_9___11_sev_12"))
                    elif severidade >= 13:
                        tkMessageBox.showinfo(arml, _("1_9_____sev_13"))
            elif local == 10:
                if 1 <= severidade <= 3:
                    tkMessageBox.showinfo(head, _("1_10___1_sev_3"))
                elif 4 <= severidade <= 6:
                    tkMessageBox.showinfo(head, _("1_10___4_sev_6"))
                elif 7 <= severidade <= 8:
                    tkMessageBox.showinfo(head, _("1_10___7_sev_8"))
                elif 9 <= severidade <= 10:
                    tkMessageBox.showinfo(head, _("1_10___9_sev_10"))
                elif 11 <= severidade <= 12:
                    tkMessageBox.showinfo(head, _("1_10___11_sev_12"))
                elif severidade >= 13:
                    tkMessageBox.showinfo(head, _("1_10_____sev_13"))

    def _retrieve_char_instance_from_listbox(self, lbox_char):
        """
        Compare and get the character instance that is relative for the
        listbox selected entry and return that Character.

        Keyword arguments:
        lbox_char -- The string that came from the listbox and will be used
        for search/comparison with the list of character objects. (NoDefault)

        """
        lchar = [char for char in self.chars if str(char) == lbox_char]
        if lchar:
            return lchar[0]

    def change_initiative(self):
        """
        Change the initiative_value of the selected object into the specified
        value.
        """
        new_init = self.campo_altini.get()
        lbox_char, lbox_pos = self._get_or_select_listbox_item()
        if lbox_char is not None:
            char = self._retrieve_char_instance_from_listbox(lbox_char)
            char.init_value = new_init
            self.listboxp.delete(lbox_pos)
            self.listboxp.insert(t.END, char)

    def add_char(self, char_type):
        """
        Add character instances into the list of chars.

        KeyWord arguments:
        char_type -- The type of the char: 0 for Player, 1 for NPC.
        """
        char = Character()
        char.name = self.campo_nome.get()
        char.hp = self.campo_pv.get()
        char.level = self.campo_nivel.get()
        char.init_value = self.campo_iniciativa.get()
        char.size = self.tamanho.get()
        char.char_type = char_type
        if char.cleaned_data:
            if not str(char) in self.listboxp.get(0, t.END):
                self.listboxp.insert(t.END, char)
                if not self.chars:
                    self.chars = [char]
                else:
                    self.chars.append(char)
            else:
                tkMessageBox.showerror(_("Char Already Exists"),
                                       _("name_repeat_error"))

    def delete_char(self):
        """
        Delete a character from the listbox and chars list.
        """
        lbox_char, lbox_pos = self._get_or_select_listbox_item()
        if lbox_char is not None:
            char = self._retrieve_char_instance_from_listbox(lbox_char)
            self.chars.remove(char)
            self.listboxp.delete(lbox_pos)

    def add_hitpoints(self):
        """
        Add the specified int value to the target HitPoints
        """
        extra_hp = self.campo_recuperacao.get()
        lbox_char, lbox_pos = self._get_or_select_listbox_item()
        if lbox_char is not None:
            char = self._retrieve_char_instance_from_listbox(lbox_char)
            valid_hp = char.clean_int_fields(extra_hp)
            if valid_hp:
                char.hp = char.hp + valid_hp
                self.listboxp.delete(lbox_pos)
                self.listboxp.insert(t.END, char)

    def subtract_hitpoints(self):
        """
        Subtracts the specified int value from the target's hitpoints.
        """
        sub_hp = self.campo_dano.get()
        lbox_char, lbox_pos = self._get_or_select_listbox_item()
        if lbox_char is not None:
            char = self._retrieve_char_instance_from_listbox(lbox_char)
            valid_hp = char.clean_int_fields(sub_hp)
            print(char, lbox_pos)
            if valid_hp:
                char.hp = char.hp - valid_hp
                self.listboxp.delete(lbox_pos)
                self.listboxp.insert(t.END, char)

    def sort(self):
        """
        Sort the Results and reinsert into theListBox.
        This is the method fired by the button 'ordenar'
        """
        self.listboxp.delete(0, t.END)
        char_sorted = sorted(self.chars, key=attrgetter('init_value'),
                             reverse=True)

        for char in char_sorted:
            self.listboxp.insert(t.END, char)

    def _get_or_select_listbox_item(self, next_pos=None, autoselect=None):
        """
        Get an item or select the first of the listbox if the autoselect is
        True.

        Returns the string and position in the list box.
        """
        try:
            lbox_selection = self.listboxp.curselection()
            next_lchar = self.listboxp.get(lbox_selection[0] + 1)
            if next_lchar == '' and next_pos is True:
                next_lchar = None
                lbox_selection = None
        except IndexError:
            lbox_selection = None
            next_lchar = None

        if not lbox_selection:
            if not autoselect:
                tkMessageBox.showerror(_("Char Error"),
                                       _("Char Error"))
                return None, None

            self.listboxp.selection_clear(0, t.END)
            self.listboxp.activate(0)
            self.listboxp.selection_set(0)
            lchar = self.listboxp.get(0)
            lbox_selection = self.listboxp.curselection()
            return lchar, lbox_selection[0]
        elif not next_pos:
            lchar = self.listboxp.get(lbox_selection[0])
            return lchar, lbox_selection[0]
        elif next_pos and next_lchar:
            self.listboxp.selection_clear(0, t.END)
            self.listboxp.activate(lbox_selection[0] + 1)
            self.listboxp.selection_set(lbox_selection[0] + 1)
            return next_lchar, lbox_selection[0] + 1

    #TODO: Reimplement status support with a new way.
    def shift_turn(self):
        """Shift the turn of the selected player or NPC."""
        next_lchar, char_pos = self._get_or_select_listbox_item(next_pos=True,
                                                                autoselect=True)
        char = self._retrieve_char_instance_from_listbox(next_lchar)

        self.turno1 += 1
        self.vez_text.set(self.turno1)
        self.vez1_text.set(char.name)

        if char.status:
            self.vez2_text.set(char.status)

    def _create_add_status_window(self):
        """
        Create the Add Status window and call the add_Status method
        with the values written into the fields
        """
        window_status = t.Toplevel()
        window_status.title('Status or Condition')
        window_status.resizable(width=False, height=False)

        frame1 = t.Frame(window_status)
        frame1.pack()
        title = t.Label(frame1, text=_("Fill the status"), width=70, height=2)
        title.pack()

        frame2 = t.Frame(window_status)
        frame2.pack()

        frame2_1 = t.Frame(frame2)
        frame2_1.pack(side=t.LEFT)
        status_title = t.Label(frame2_1, text=_("Status Name"), width=20,
                               height=1)
        status_value = t.Entry(frame2_1, width=20)
        status_title.pack()
        status_value.pack()

        frame2_2 = t.Frame(frame2)
        frame2_2.pack(side=t.RIGHT)
        status_type_title = t.Label(frame2_2, text=_("Status Type"), width=20,
                                    height=1)
        status_type_title.pack()

        stat_type = t.StringVar()
        stat_type.set('Static')

        stat_choice1 = t.Radiobutton(frame2_2, text=_('Static'),
                                     variable=stat_type, value=_('Static'),
                                     command=lambda: status_turn.configure(
                                         state='normal')).pack()

        stat_choice2 = t.Radiobutton(frame2_2, text=_('Resistance Test'),
                                     variable=stat_type, value=_('Continuous'),
                                     command=lambda: status_turn.configure(
                                         state='disabled')).pack()

        frame3 = t.Frame(window_status)
        frame3.pack()

        frame3_1 = t.Frame(frame3)
        frame3_1.pack(side=t.LEFT)
        status_turn_title = t.Label(frame3_1, text=_("Number of Turns"),
                                    width=20, height=1)
        status_turn_title.pack()
        status_turn = t.Entry(frame3, width=20)
        status_turn.pack()

        frame4 = t.Frame(window_status)
        frame4.pack()

        status_submit = t.Button(frame4, width=14, text=_("Add Status"),
                                 command=lambda: self.add_status(
                                     (status_value.get(),
                                      stat_type.get(),
                                      status_turn.get())
                                 ))
        status_submit.pack()

    def add_status(self, status_value):
        """
        Add a new status for a specific character.
        """
        lchar, lchar_pos = self._get_or_select_listbox_item()
        char = self._retrieve_char_instance_from_listbox(lchar)

        char.status.add(status_value)

    #TODO: Rewrite.
    #Botão Passar Dias    
    def passar_dias(self):
        try:
            DIASPASS = self.campo_dias.get()
            DIASPASS = int(DIASPASS)
            self.listboxp.delete(0, t.END)
            for i in self.comba:
                self.comba[i][1] = self.comba[i][1] + (
                    int(self.comba[i][2]) * DIASPASS)
                self.listboxp.insert(t.END, str(self.comba[i][0]) + ' - ' +
                                     str(self.comba[i][1]))
        except:
            tkMessageBox.showerror(_("Faltou Informações"), _("days_error"))

    def calculate_xp(self, xp_table=None):
        """
        Calculate the experience gained using a xp_table and the level of the
        NPC's (character type == 1) dividing the second value of xp_table tuple
        by the number of players (character type == 0).

        Default: if no xp_table is provided, the default is to use the
        PathFinder experience table per level.
        """
        npcs = [char for char in self.chars if char.char_type == 1]
        pcs = len([char for char in self.chars if char.char_type == 0])
        xp = 0
        if not xp_table:
            xp_table = [
                (1, 400),
                (2, 600),
                (3, 800),
                (4, 1200),
                (5, 1600),
                (6, 2400),
                (7, 3200),
                (8, 4800),
                (9, 6400),
                (10, 9600),
                (11, 12800),
                (12, 19200),
                (13, 25600),
                (14, 38400),
                (15, 51200),
                (16, 76800),
                (17, 102400),
                (18, 153600),
                (19, 204800),
                (20, 307200),
                (21, 409600),
                (22, 615000),
                (23, 82000),
                (24, 1230000),
                (25, 1640000),
            ]

        for npc in npcs:
                xp += [value[1] for value in xp_table if value[0] == npc.level][
                    0]

        if pcs:
            tkMessageBox.showinfo(_("XP ganho"),
                                  "Esse combate da um total de %i XP \n cada "
                                  "jogador que sobreviveu "
                                  "recebe %i XP" % (xp, xp / pcs))
        else:
            tkMessageBox.showinfo(_("XP ganho"),
                                  "Não foram adicionados Personagens Jogadores."
                                  "Sem Experiência."
            )

    def open(self):
        """
        Open previously saved files.
        """
        window = t.Tk()
        window.withdraw()
        filename = tkFileDialog.askopenfilename(parent=window,
                                                title=_('Open saved CDC file'))

        if filename:
            with open(filename, 'rb') as savefile:
                saved_game = pickle.load(savefile)

        window.destroy()

        self.chars = saved_game[0]
        self.listboxp.delete(0, t.END)

        for char in saved_game[1]:
            self.listboxp.insert(t.END, char)

        self.turno = saved_game[2]
        self.turno1 = saved_game[3]

    def save(self):
        """
        Persist all combat information into a file that can be opened later.
        """
        content = [self.chars,
                   self.listboxp.get(0, t.END),
                   self.turno,
                   self.turno1,
                   self.tagtext
        ]
        window = t.Tk()
        window.withdraw()
        filename = tkFileDialog.asksaveasfilename(parent=window,
                                                  title=_("Save combat info"))

        if filename:
            with open(filename, 'wb') as savefile:
                pickle.dump(content, savefile, protocol=2)

        window.destroy()

    def quit(self):
        """ Destroy the main window. """
        self.janela.destroy()

    def ajuda(self):
        webbrowser.open(
            'http://dadosedesventuras.blogspot.com.br/p/ajuda-controle-de-combate.html')

    def sobre(self):
        tkMessageBox.showinfo(_("Sobre"),
                              _("about"))


if __name__ == '__main__':
    swallow = t.Tk()
    MontyPython(swallow)
    swallow.mainloop()
