# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'telalog.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

"""
d={
 "clientes": {
  "": {
   "nome": "elijose",
   "senha": "",
   "email": "elijose55",
   "celular": "976678686",
   "bairro": "juruce"
  }
 },
 "cozinheiro": {
  "a": {
   "nome": "elijose",
   "senha": "",
   "email": "elijose55",
   "celular": "976678686",
   "restaurante": "asterix",
   "cardapio": {
   'bolo':[15,20,'Bolo de Cenoura'],
   'arroz':[7,25,'Arroz Branco'],
   'feijao':[8,24, 'Feijao Caseiro']
   }
   "bairro": "juruce",
   "descricao": "Comida boa e caseira focada em massas e paes"
  }
 }
}

"""


d={
    'clientes': {
    '':{
    'nome': 'elijose',
    'email': 'elijose55',
    'senha': '',
    'bairro': 'juruce',
    'celular': '976678686',
    }

    },

    'cozinheiro': {
    'a':{
    'nome': 'elijose',
    'email': 'elijose55',
    'senha': '',
    'bairro': 'juruce',
    'celular': '976678686',
    'status': 'online',
    'restaurante': 'asterix',
    'descricao': 'Comida boa e caseira focada em massas e paes',
    'cardapio': [[15,20,'Bolo de Cenoura'],[7,25,'Arroz Branco'],[8,24, 'Feijao Caseiro']],
    }
      }
      }

from PyQt4 import QtCore, QtGui
from escolhalogin import Ui_escolhalogin
from regcliente import Ui_regcliente
from telareg import Ui_telareg
from telacliente import Ui_telacliente
from telafinalizar import Ui_telafinalizar
from telacardapio import Ui_telacardapio
import json







with open('dict.json','r') as cf:
    d=json.load(cf)


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_tlogin(object):

    def __init__ (self):
        with open('dict.json','r') as cf:
            d=json.load(cf)



    def lerro(self): ##aviso de login invalido
        msg=QtGui.QMessageBox()
        msg.setIcon(QtGui.QMessageBox.Warning)
        msg.setWindowTitle('Aviso')
        msg.setText('Login ou Senha Inválidos')
        msg.setStandardButtons(QtGui.QMessageBox.Ok)
        msg.exec_()

    def registrocheck(self):
        ##aparecer janela de escolha de registro depois de clicar no botao de registar
        self.escolhareg = QtGui.QMainWindow()
        self.ui= Ui_escolhalogin()
        self.ui.setupUi(self.escolhareg)
        self.escolhareg.show()





    def logincheck(self): ##checar o login e senha no dicionario

        with open('dict.json','r') as cf:
            d=json.load(cf)
        username = self.llogin.text()
        username = str(username)
        password = self.lsenha.text()
        password = str(password)

        if username in d['cozinheiro']: ##login de um cozinheiro
            if d['cozinheiro'][username]['senha']==password:

                    ##abrir tela de cardapio do cozinheiro depois do login do cozinheiro
                self.cardapio = QtGui.QMainWindow()
                self.ui= Ui_telacardapio(username)
                self.ui.setupUi(self.cardapio)
                self.cardapio.show()
                QtGui.QMainWindow.close(self.tlogin)

        elif username in d['clientes']: ##login do cliente
            if d['clientes'][username]['senha']==password:

                d['clientes'][username]['pedido'] = []

                with open('dict.json','w') as file:
                    json.dump(d, file, indent=1)

                    #abrir tela de espera do cliente
                self.cliente = QtGui.QMainWindow()
                self.ui= Ui_telacliente(username)
                self.ui.setupUi(self.cliente)
                self.cliente.show()
                QtGui.QMainWindow.close(self.tlogin)
            else:
                self.lerro() ##funcao que mostra mensagem de login errado
        else:
            self.lerro()
        
        


    def setupUi(self, tlogin):

        def __init__(self):
            with open('arquivo.json','r') as cf:
                dict=json.load(cf)

        tlogin.setObjectName(_fromUtf8("tlogin"))
        tlogin.resize(666, 506)
        tlogin.setMinimumSize(QtCore.QSize(666, 506))
        tlogin.setMaximumSize(QtCore.QSize(666, 506))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        tlogin.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("minilogo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        tlogin.setWindowIcon(icon)
        tlogin.setAutoFillBackground(True)
        tlogin.setStyleSheet(_fromUtf8(""))
        tlogin.setUnifiedTitleAndToolBarOnMac(True)
        self.tlogin = tlogin
        self.centralwidget = QtGui.QWidget(tlogin)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(230, 110, 173, 230))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Trebuchet MS"))
        font.setPointSize(9)
        self.widget.setFont(font)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.label = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Trebuchet MS"))
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_4.addWidget(self.label)
        self.llogin = QtGui.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Trebuchet MS"))
        font.setPointSize(9)
        self.llogin.setFont(font)
        self.llogin.setObjectName(_fromUtf8("llogin"))
        self.verticalLayout_4.addWidget(self.llogin)
        self.label_2 = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Trebuchet MS"))
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_4.addWidget(self.label_2)
        self.lsenha = QtGui.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Trebuchet MS"))
        font.setPointSize(9)
        self.lsenha.setFont(font)
        self.lsenha.setEchoMode(QtGui.QLineEdit.Password)
        self.lsenha.setObjectName(_fromUtf8("lsenha"))
        self.verticalLayout_4.addWidget(self.lsenha)
        self.blogin = QtGui.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Trebuchet MS"))
        font.setPointSize(9)
        self.blogin.setFont(font)
        self.blogin.setObjectName(_fromUtf8("blogin"))
        self.verticalLayout_4.addWidget(self.blogin)
        self.bregistrar = QtGui.QPushButton(self.widget)
        
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Trebuchet MS"))
        font.setPointSize(9)
        self.bregistrar.setFont(font)
        self.bregistrar.setObjectName(_fromUtf8("bregistrar"))
        self.verticalLayout_4.addWidget(self.bregistrar)
        self.label.raise_()
        self.label_2.raise_()
        self.llogin.raise_()
        self.lsenha.raise_()
        self.blogin.raise_()
        self.bregistrar.raise_()
        self.label.raise_()
        tlogin.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(tlogin)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        tlogin.setStatusBar(self.statusbar)
        self.menubar = QtGui.QMenuBar(tlogin)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 666, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuOp_es = QtGui.QMenu(self.menubar)
        self.menuOp_es.setObjectName(_fromUtf8("menuOp_es"))
        tlogin.setMenuBar(self.menubar)
        self.bsair = QtGui.QAction(tlogin)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Trebuchet MS"))
        self.bsair.setFont(font)
        self.bsair.setObjectName(_fromUtf8("bsair"))
        self.menuOp_es.addAction(self.bsair)
        self.menubar.addAction(self.menuOp_es.menuAction())

        self.retranslateUi(tlogin)
        QtCore.QObject.connect(self.bsair, QtCore.SIGNAL(_fromUtf8("triggered()")), tlogin.close)
        QtCore.QMetaObject.connectSlotsByName(tlogin)


        self.bregistrar.clicked.connect(self.registrocheck) ##conectar botao de registro com a funcao de abrir tela de escolha de registro

        self.blogin.clicked.connect(self.logincheck) ##conectar botao de login com a funcao de checar login

    def retranslateUi(self, tlogin):
        tlogin.setWindowTitle(_translate("tlogin", "PyFood", None))
        self.label.setText(_translate("tlogin", "Login", None))
        self.label_2.setText(_translate("tlogin", "Senha", None))
        self.blogin.setText(_translate("tlogin", "Login", None))
        self.bregistrar.setText(_translate("tlogin", "Registrar", None))
        self.menuOp_es.setTitle(_translate("tlogin", "Opções", None))
        self.bsair.setText(_translate("tlogin", "Sair", None))



if __name__ == "__main__":
    import sys


    app = QtGui.QApplication(sys.argv)
    tlogin = QtGui.QMainWindow()
    ui = Ui_tlogin()
    ui.setupUi(tlogin)
    tlogin.show()
    sys.exit(app.exec_())

