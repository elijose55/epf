# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'telafinalizar.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import json

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

class Ui_telafinalizar(object):

    def __init__ (self,x,c):
        self.x=x
        self.T=0
        self.P=0
        self.c=c


    def fim(self):
        d['clientes'][self.x]['pedido']=lc
        d['cozinheiro'][self.c]['pedido']=lc
        


    def setupUi(self, telafinalizar):
        telafinalizar.setObjectName(_fromUtf8("telafinalizar"))
        telafinalizar.resize(676, 668)
        telafinalizar.setMinimumSize(QtCore.QSize(676, 668))
        telafinalizar.setMaximumSize(QtCore.QSize(676, 668))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("minilogo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        telafinalizar.setWindowIcon(icon)
        self.carrinhoww = QtGui.QTextBrowser(telafinalizar)
        self.carrinhoww.setGeometry(QtCore.QRect(100, 170, 301, 361))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Trebuchet MS"))
        font.setPointSize(10)
        self.carrinhoww.setFont(font)
        self.carrinhoww.setObjectName(_fromUtf8("carrinhoww"))
        self.bvoltar = QtGui.QPushButton(telafinalizar)
        self.bvoltar.setGeometry(QtCore.QRect(80, 600, 93, 28))
        self.bvoltar.setObjectName(_fromUtf8("bvoltar"))
        self.bpedir = QtGui.QPushButton(telafinalizar)
        self.bpedir.setGeometry(QtCore.QRect(510, 600, 93, 28))
        self.bpedir.setObjectName(_fromUtf8("bpedir"))
        self.label_5 = QtGui.QLabel(telafinalizar)
        self.label_5.setGeometry(QtCore.QRect(250, 50, 391, 51))
        self.label_5.setMinimumSize(QtCore.QSize(391, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Trebuchet MS"))
        font.setPointSize(13)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.ltempo = QtGui.QLabel(telafinalizar)
        self.ltempo.setGeometry(QtCore.QRect(460, 250, 180, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Trebuchet MS"))
        font.setPointSize(10)
        self.ltempo.setFont(font)
        self.ltempo.setObjectName(_fromUtf8("ltempo"))
        self.lpreco = QtGui.QLabel(telafinalizar)
        self.lpreco.setGeometry(QtCore.QRect(460, 190, 180, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Trebuchet MS"))
        font.setPointSize(10)
        self.lpreco.setFont(font)
        self.lpreco.setObjectName(_fromUtf8("lpreco"))
        self.line = QtGui.QFrame(telafinalizar)
        self.line.setGeometry(QtCore.QRect(460, 220, 191, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.line_2 = QtGui.QFrame(telafinalizar)
        self.line_2.setGeometry(QtCore.QRect(460, 290, 191, 16))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.label = QtGui.QLabel(telafinalizar)
        self.label.setGeometry(QtCore.QRect(550, 190, 53, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(telafinalizar)
        self.label_2.setGeometry(QtCore.QRect(550, 250, 53, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))


############

        #self.carrinhoww.setText('')

        with open('dict.json','r') as cf:
            d=json.load(cf)

        lc = d['clientes'][self.x]['temp']



        for i in lc:
            objeto = i
            nn=objeto[2] #nome
            pp=objeto[0] #preco
            tt=objeto[1] #tempo de preparo
            qq=objeto[3] #quantidade
            self.T+=tt #tempo total
            self.P+=pp #preco total
                
            self.carrinhoww.append('{0}     x{3} \n Preço: R${1:.2f} \n Tempo: {2} minutos \n' .format(nn,pp,tt,qq))

        self.lpreco.setText('Preço :   R${0:.2f}' .format(self.P))
        self.ltempo.setText('Tempo :   {0} minutos' .format(self.T))


        self.bpedir.clicked.connect(self.fim)

##############

        self.retranslateUi(telafinalizar)
        QtCore.QObject.connect(self.bvoltar, QtCore.SIGNAL(_fromUtf8("clicked()")), telafinalizar.close)
        QtCore.QMetaObject.connectSlotsByName(telafinalizar)

    def retranslateUi(self, telafinalizar):
        telafinalizar.setWindowTitle(_translate("telafinalizar", "PyFood", None))
        self.bvoltar.setText(_translate("telafinalizar", "Voltar", None))
        self.bpedir.setText(_translate("telafinalizar", "Pedir", None))
        self.label_5.setText(_translate("telafinalizar", "Finalizar Pedido", None))



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    telafinalizar = QtGui.QDialog()
    ui = Ui_telafinalizar()
    ui.setupUi(telafinalizar)
    telafinalizar.show()
    sys.exit(app.exec_())

