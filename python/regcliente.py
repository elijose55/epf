# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'regcliente.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
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

class Ui_regcliente(object):


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
            if x not in d['clientes'] and x not in d['cozinheiro']:
                d['clientes'][x]={}

                temp = self.tnome.text()
                temp = str(temp)
                d['clientes'][x]['nome']=temp

                temp = self.temail.text()
                temp = str(temp)
                d['clientes'][x]['email']=temp

                temp = self.tsenha.text()
                temp = str(temp)
                d['clientes'][x]['senha']=temp

                temp = self.tbairro.text()
                temp = str(temp)
                temp = temp.lstrip()
                temp = temp.lower()
                temp = temp.title()
                d['clientes'][x]['bairro']=temp

                temp = self.tcelular.text()
                temp = str(temp)
                d['clientes'][x]['celular']=temp

                with open('dict.json','w') as file:
                    json.dump(d, file, indent=1)

                msg=QtGui.QMessageBox()
                msg.setIcon(QtGui.QMessageBox.Information)
                msg.setWindowTitle('Aviso')
                msg.setText('Registro Bem-Sucedido')
                msg.setStandardButtons(QtGui.QMessageBox.Ok)
                msg.exec_()

                self.telalog = QtGui.QMainWindow()
                self.ui= Ui_tlogin()
                self.ui.setupUi(self.telalog)
                self.telalog.show()
                self.telareg.close()

            else:
                self.erro()



    def setupUi(self, regcliente):
        regcliente.setObjectName(_fromUtf8("regcliente"))
        regcliente.resize(973, 652)
        regcliente.setMinimumSize(QtCore.QSize(973, 652))
        regcliente.setMaximumSize(QtCore.QSize(973, 652))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("minilogo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        regcliente.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(regcliente)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.bregistar = QtGui.QPushButton(self.centralwidget)
        self.bregistar.setGeometry(QtCore.QRect(420, 470, 111, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Trebuchet MS"))
        font.setPointSize(10)
        self.bregistar.setFont(font)
        self.bregistar.setObjectName(_fromUtf8("bregistar"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(430, 60, 161, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Trebuchet MS"))
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 160, 379, 26))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Trebuchet MS"))
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.tlogin = QtGui.QLineEdit(self.centralwidget)
        self.tlogin.setGeometry(QtCore.QRect(70, 190, 379, 22))
        self.tlogin.setObjectName(_fromUtf8("tlogin"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 220, 377, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Trebuchet MS"))
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(540, 150, 375, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Trebuchet MS"))
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
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
        self.tsenha = QtGui.QLineEdit(self.centralwidget)
        self.tsenha.setGeometry(QtCore.QRect(70, 260, 381, 22))
        self.tsenha.setObjectName(_fromUtf8("tsenha"))
        self.temail = QtGui.QLineEdit(self.centralwidget)
        self.temail.setGeometry(QtCore.QRect(70, 330, 381, 22))
        self.temail.setInputMethodHints(QtCore.Qt.ImhNone)
        self.temail.setObjectName(_fromUtf8("temail"))
        self.tcelular = QtGui.QLineEdit(self.centralwidget)
        self.tcelular.setGeometry(QtCore.QRect(70, 400, 379, 22))
        self.tcelular.setObjectName(_fromUtf8("tcelular"))
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(70, 360, 379, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Trebuchet MS"))
        font.setPointSize(9)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(540, 230, 377, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Trebuchet MS"))
        font.setPointSize(9)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.tbairro = QtGui.QLineEdit(self.centralwidget)
        self.tbairro.setGeometry(QtCore.QRect(540, 260, 377, 22))
        self.tbairro.setObjectName(_fromUtf8("tbairro"))
        regcliente.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(regcliente)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 973, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuOpcoes = QtGui.QMenu(self.menubar)
        self.menuOpcoes.setObjectName(_fromUtf8("menuOpcoes"))
        regcliente.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(regcliente)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        regcliente.setStatusBar(self.statusbar)
        self.actionVoltar = QtGui.QAction(regcliente)
        self.actionVoltar.setObjectName(_fromUtf8("actionVoltar"))
        self.menuOpcoes.addAction(self.actionVoltar)
        self.menubar.addAction(self.menuOpcoes.menuAction())

        self.retranslateUi(regcliente)
        QtCore.QObject.connect(self.actionVoltar, QtCore.SIGNAL(_fromUtf8("triggered()")), regcliente.close)
        QtCore.QMetaObject.connectSlotsByName(regcliente)

        self.bregistar.clicked.connect(self.registro)

    def retranslateUi(self, regcliente):
        regcliente.setWindowTitle(_translate("regcliente", "Registro", None))
        self.bregistar.setText(_translate("regcliente", "Registrar", None))
        self.label.setText(_translate("regcliente", "Registro", None))
        self.label_2.setText(_translate("regcliente", "  Login", None))
        self.label_3.setText(_translate("regcliente", "  Senha", None))
        self.label_4.setText(_translate("regcliente", "  Nome Completo", None))
        self.label_5.setText(_translate("regcliente", "  Email", None))
        self.label_7.setText(_translate("regcliente", "  Celular", None))
        self.label_6.setText(_translate("regcliente", "  Bairro", None))
        self.menuOpcoes.setTitle(_translate("regcliente", "Opções", None))
        self.actionVoltar.setText(_translate("regcliente", "Voltar", None))



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    regcliente = QtGui.QMainWindow()
    ui = Ui_regcliente()
    ui.setupUi(regcliente)
    regcliente.show()
    sys.exit(app.exec_())

