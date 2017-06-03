# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'telareg.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from mapa2 import imail
import requests
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

class Ui_telareg(object):
    def __init__(self):
        with open('dict.json','r') as cf:
            d=json.load(cf)

    def erro(self):
        msg=QtGui.QMessageBox()
        msg.setIcon(QtGui.QMessageBox.Warning)
        msg.setWindowTitle('Aviso')
        msg.setText('Usuario Indisponivel')
        msg.setStandardButtons(QtGui.QMessageBox.Ok)
        msg.exec_()

    def registro(self):
            x = self.tlogin.text()
            x = str(x)
            if x not in d['cozinheiro'] and x not in d['clientes']:
                d['cozinheiro'][x]={}

                d['cozinheiro'][x]['login']=x

                temp = self.tnome.text()
                temp = str(temp)
                d['cozinheiro'][x]['nome']=temp

                temp = self.temail.text()
                temp = str(temp)
                d['cozinheiro'][x]['email']=temp

                temp = self.tendereco.text()
                temp = str(temp)
                temp = temp.lower()
                temp = temp.lstrip()
                temp=temp.title()
                temp=temp.split()
                temp=' '.join(temp)
                d['cozinheiro'][x]['endereco']=temp

                temp = self.tsenha.text()
                temp = str(temp)
                temp = temp.lower()
                temp = temp.lstrip()
                temp=temp.title()
                temp=temp.split()
                temp=' '.join(temp)
                temp = str(temp)
                d['cozinheiro'][x]['senha']=temp

                temp = self.tbairro.text()
                temp = str(temp)
                temp = temp.lstrip()
                temp = temp.lower()
                temp = temp.title()
                temp=temp.split()
                temp=' '.join(temp)
                d['cozinheiro'][x]['bairro']=temp

                temp = self.tcelular.text()
                temp = str(temp)
                d['cozinheiro'][x]['celular']=temp

                temp = self.tnomerest.text()
                temp = str(temp)
                d['cozinheiro'][x]['restaurante']=temp

                temp = self.tdescricao.text()
                temp = str(temp)
                d['cozinheiro'][x]['descricao']=temp

                d['cozinheiro'][x]['status']='offline'

                d['cozinheiro'][x]['cardapio'] = []

                d['cozinheiro'][x]['pedido'] = {}

                with open('dict.json','w') as file:
                    json.dump(d, file, indent=1)


                msg=QtGui.QMessageBox()
                msg.setIcon(QtGui.QMessageBox.Information)
                msg.setWindowTitle('Aviso')
                msg.setText('Registro Realizado. Aguarde o Email de Confirmação')
                msg.setStandardButtons(QtGui.QMessageBox.Ok)
                msg.exec_()

                imail(d['cozinheiro'][x]['email'])



                QtGui.QMainWindow.close(self.telareg)




            else:
                self.erro()

    def setupUi(self, telareg):
        telareg.setObjectName(_fromUtf8("telareg"))
        telareg.resize(976, 652)
        telareg.setMinimumSize(QtCore.QSize(976, 652))
        telareg.setMaximumSize(QtCore.QSize(976, 652))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("minilogo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        telareg.setWindowIcon(icon)
        self.telareg = telareg
        self.centralwidget = QtGui.QWidget(telareg)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(430, 50, 161, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Trebuchet MS"))
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.bregistar = QtGui.QPushButton(self.centralwidget)
        self.bregistar.setGeometry(QtCore.QRect(440, 540, 111, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Trebuchet MS"))
        font.setPointSize(10)
        self.bregistar.setFont(font)
        self.bregistar.setObjectName(_fromUtf8("bregistar"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(540, 150, 375, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Trebuchet MS"))
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.tcelular = QtGui.QLineEdit(self.centralwidget)
        self.tcelular.setGeometry(QtCore.QRect(70, 400, 379, 22))
        self.tcelular.setObjectName(_fromUtf8("tcelular"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 220, 377, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Trebuchet MS"))
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 160, 379, 26))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Trebuchet MS"))
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.tnome = QtGui.QLineEdit(self.centralwidget)
        self.tnome.setGeometry(QtCore.QRect(540, 190, 375, 22))
        self.tnome.setObjectName(_fromUtf8("tnome"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(70, 290, 373, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Trebuchet MS"))
        font.setPointSize(9)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(70, 360, 379, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Trebuchet MS"))
        font.setPointSize(9)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.tbairro = QtGui.QLineEdit(self.centralwidget)
        self.tbairro.setGeometry(QtCore.QRect(540, 260, 377, 22))
        self.tbairro.setObjectName(_fromUtf8("tbairro"))
        self.tsenha = QtGui.QLineEdit(self.centralwidget)
        self.tsenha.setGeometry(QtCore.QRect(70, 260, 381, 22))
        self.tsenha.setObjectName(_fromUtf8("tsenha"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(540, 230, 377, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Trebuchet MS"))
        font.setPointSize(9)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.tlogin = QtGui.QLineEdit(self.centralwidget)
        self.tlogin.setGeometry(QtCore.QRect(70, 190, 379, 22))
        self.tlogin.setObjectName(_fromUtf8("tlogin"))
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(550, 300, 377, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Trebuchet MS"))
        font.setPointSize(9)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.temail = QtGui.QLineEdit(self.centralwidget)
        self.temail.setGeometry(QtCore.QRect(70, 330, 381, 20))
        self.temail.setObjectName(_fromUtf8("temail"))
        self.tdescricao = QtGui.QLineEdit(self.centralwidget)
        self.tdescricao.setGeometry(QtCore.QRect(540, 400, 377, 91))
        self.tdescricao.setObjectName(_fromUtf8("tdescricao"))
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(550, 370, 377, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Trebuchet MS"))
        font.setPointSize(9)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.tnomerest = QtGui.QLineEdit(self.centralwidget)
        self.tnomerest.setGeometry(QtCore.QRect(540, 340, 377, 22))
        self.tnomerest.setObjectName(_fromUtf8("tnomerest"))
        self.tendereco = QtGui.QLineEdit(self.centralwidget)
        self.tendereco.setGeometry(QtCore.QRect(70, 470, 379, 22))
        self.tendereco.setText(_fromUtf8(""))
        self.tendereco.setObjectName(_fromUtf8("tendereco"))
        self.label_10 = QtGui.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(70, 430, 379, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Trebuchet MS"))
        font.setPointSize(9)
        self.label_10.setFont(font)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        telareg.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(telareg)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 976, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuOpcoes = QtGui.QMenu(self.menubar)
        self.menuOpcoes.setObjectName(_fromUtf8("menuOpcoes"))
        telareg.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(telareg)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        telareg.setStatusBar(self.statusbar)
        self.bvoltar = QtGui.QAction(telareg)
        self.bvoltar.setObjectName(_fromUtf8("bvoltar"))
        self.menuOpcoes.addAction(self.bvoltar)
        self.menubar.addAction(self.menuOpcoes.menuAction())

        self.bregistar.clicked.connect(self.registro)
        #botao de registrar pressionado
        
        self.retranslateUi(telareg)
        QtCore.QObject.connect(self.bvoltar, QtCore.SIGNAL(_fromUtf8("triggered()")), telareg.close)
        QtCore.QMetaObject.connectSlotsByName(telareg)

    def retranslateUi(self, telareg):
        telareg.setWindowTitle(_translate("telareg", "Registro", None))
        self.label.setText(_translate("telareg", "Registro", None))
        self.bregistar.setText(_translate("telareg", "Registrar", None))
        self.label_4.setText(_translate("telareg", "  Nome Completo", None))
        self.label_3.setText(_translate("telareg", "  Senha", None))
        self.label_2.setText(_translate("telareg", "  Login", None))
        self.label_5.setText(_translate("telareg", "  Email", None))
        self.label_7.setText(_translate("telareg", "  Celular", None))
        self.label_6.setText(_translate("telareg", "  Bairro", None))
        self.label_8.setText(_translate("telareg", "Nome do Restaurante", None))
        self.label_9.setText(_translate("telareg", "Descrição do Restaurante", None))
        self.label_10.setText(_translate("telareg", "  Endereço", None))
        self.menuOpcoes.setTitle(_translate("telareg", "Opções", None))
        self.bvoltar.setText(_translate("telareg", "Voltar", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    telareg = QtGui.QMainWindow()
    ui = Ui_telareg()
    ui.setupUi(telareg)
    telareg.show()
    sys.exit(app.exec_())

