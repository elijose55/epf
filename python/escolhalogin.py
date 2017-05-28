# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'escolhalogin.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!


from PyQt4 import QtCore, QtGui
from regcliente import Ui_regcliente 
from telareg import Ui_telareg

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

class Ui_escolhalogin(object):




    def cliente(self):
        self.regcliente = QtGui.QMainWindow()
        self.ui= Ui_regcliente(d)
        self.ui.setupUi(self.regcliente)
        
        self.regcliente.show()
        self.escolhalogin.close()

    def cozinheiro(self):
        self.regcoz = QtGui.QMainWindow()
        self.ui= Ui_telareg()
        self.ui.setupUi(self.regcoz)
        self.regcoz.show()


    def setupUi(self, escolhalogin):
        escolhalogin.setObjectName(_fromUtf8("escolhalogin"))
        escolhalogin.resize(663, 505)
        escolhalogin.setMinimumSize(QtCore.QSize(663, 505))
        escolhalogin.setMaximumSize(QtCore.QSize(663, 505))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../minilogo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        escolhalogin.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(escolhalogin)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.bcliente = QtGui.QPushButton(self.centralwidget)
        self.bcliente.setGeometry(QtCore.QRect(350, 270, 93, 28))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Trebuchet MS"))
        font.setPointSize(9)
        self.bcliente.setFont(font)
        self.bcliente.setObjectName(_fromUtf8("bcliente"))

        self.bcliente.clicked.connect(self.cliente)

        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 140, 301, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Trebuchet MS"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.bcozinheiro = QtGui.QPushButton(self.centralwidget)
        self.bcozinheiro.setGeometry(QtCore.QRect(200, 270, 93, 28))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Trebuchet MS"))
        font.setPointSize(9)
        self.bcozinheiro.setFont(font)
        self.bcozinheiro.setObjectName(_fromUtf8("bcozinheiro"))

        self.bcozinheiro.clicked.connect(self.cozinheiro)

        escolhalogin.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(escolhalogin)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 663, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuOpcoes = QtGui.QMenu(self.menubar)
        self.menuOpcoes.setObjectName(_fromUtf8("menuOpcoes"))
        escolhalogin.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(escolhalogin)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        escolhalogin.setStatusBar(self.statusbar)
        self.bvoltar = QtGui.QAction(escolhalogin)
        self.bvoltar.setObjectName(_fromUtf8("bvoltar"))
        self.menuOpcoes.addAction(self.bvoltar)
        self.menubar.addAction(self.menuOpcoes.menuAction())

        self.retranslateUi(escolhalogin)
        QtCore.QObject.connect(self.bvoltar, QtCore.SIGNAL(_fromUtf8("triggered()")), escolhalogin.close)
        QtCore.QMetaObject.connectSlotsByName(escolhalogin)

    def retranslateUi(self, escolhalogin):
        escolhalogin.setWindowTitle(_translate("escolhalogin", "PyFood", None))
        self.bcliente.setText(_translate("escolhalogin", "Cliente", None))
        self.label.setText(_translate("escolhalogin", "Você gostaria de se registrar como:", None))
        self.bcozinheiro.setText(_translate("escolhalogin", "Cozinheiro", None))
        self.menuOpcoes.setTitle(_translate("escolhalogin", "Opções", None))
        self.bvoltar.setText(_translate("escolhalogin", "Voltar", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    escolhalogin = QtGui.QMainWindow()
    ui = Ui_escolhalogin(d)
    ui.setupUi(escolhalogin)
    escolhalogin.show()
    sys.exit(app.exec_())

