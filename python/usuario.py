# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'usuario.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import json

c='a'

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

class Ui_usuario(object):

    def __init__(self,c):
        self.c = c

    def trocarcel(self):
        cel = self.tcelular.text()
        d['cozinheiro'][self.c]['celular'] = cel
        with open('dict.json','w') as file:
            json.dump(d, file, indent=1)
        self.tcelular.clear()
        self.CELULAR.setText(d['cozinheiro'][self.c]['celular'])

    def trocaremail(self):
        email = self.temail.text()
        d['cozinheiro'][self.c]['email'] = email
        with open('dict.json','w') as file:
            json.dump(d, file, indent=1)
        self.EMAIL.setText(d['cozinheiro'][self.c]['email'])
        self.temail.clear()

    def trocarbairro(self):
        temp = self.tbairro.text()
        temp = str(temp)
        temp = temp.lstrip()
        temp = temp.lower()
        temp = temp.title()
        temp=temp.split()
        temp=' '.join(temp)
        d['cozinheiro'][self.c]['bairro'] = temp
        with open('dict.json','w') as file:
            json.dump(d, file, indent=1)
        self.LBAIRRO.setText(d['cozinheiro'][self.c]['bairro'])
        self.tbairro.clear()

    def trocarrest(self):
        rest = self.tnomerest.text()
        d['cozinheiro'][self.c]['restaurante'] = rest
        with open('dict.json','w') as file:
            json.dump(d, file, indent=1)
        self.tnomerest.clear()
        self.NOMEREST.setText(d['cozinheiro'][self.c]['restaurante'])

    def trocardes(self):
        des = self.tdescricao.text()
        d['cozinheiro'][self.c]['descricao'] = des
        with open('dict.json','w') as file:
            json.dump(d, file, indent=1)
        self.tdescricao.clear()
        self.LDESCRICAOWW.setText(d['cozinheiro'][self.c]['descricao'])

    def trocarend(self):
        temp = self.tendereco.text()
        temp = str(temp)
        temp = temp.lower()
        temp = temp.lstrip()
        temp=temp.title()
        temp=temp.split()
        temp=' '.join(temp)
        d['cozinheiro'][self.c]['endereco'] = temp
        with open('dict.json','w') as file:
            json.dump(d, file, indent=1)
        self.tendereco.clear()
        self.ENDERECO.setText(d['cozinheiro'][self.c]['endereco'])
    def setupUi(self, usuario):
        usuario.setObjectName(_fromUtf8("usuario"))
        usuario.resize(897, 648)
        usuario.setMinimumSize(QtCore.QSize(897, 648))
        usuario.setMaximumSize(QtCore.QSize(897, 648))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("minilogo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        usuario.setWindowIcon(icon)
        self.label = QtGui.QLabel(usuario)
        self.label.setGeometry(QtCore.QRect(400, 10, 161, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Trebuchet MS"))
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_5 = QtGui.QLabel(usuario)
        self.label_5.setGeometry(QtCore.QRect(50, 100, 61, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Trebuchet MS"))
        font.setPointSize(9)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.temail = QtGui.QLineEdit(usuario)
        self.temail.setGeometry(QtCore.QRect(60, 170, 373, 22))
        self.temail.setObjectName(_fromUtf8("temail"))
        self.EMAIL = QtGui.QLabel(usuario)
        self.EMAIL.setGeometry(QtCore.QRect(60, 130, 331, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Trebuchet MS"))
        font.setPointSize(9)
        self.EMAIL.setFont(font)
        self.EMAIL.setObjectName(_fromUtf8("EMAIL"))
        self.btrocaremail = QtGui.QPushButton(usuario)
        self.btrocaremail.setGeometry(QtCore.QRect(60, 200, 93, 28))
        self.btrocaremail.setObjectName(_fromUtf8("btrocaremail"))
        self.tcelular = QtGui.QLineEdit(usuario)
        self.tcelular.setGeometry(QtCore.QRect(60, 310, 373, 22))
        self.tcelular.setObjectName(_fromUtf8("tcelular"))
        self.label_10 = QtGui.QLabel(usuario)
        self.label_10.setGeometry(QtCore.QRect(60, 240, 61, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Trebuchet MS"))
        font.setPointSize(9)
        self.label_10.setFont(font)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.btrocarcelular = QtGui.QPushButton(usuario)
        self.btrocarcelular.setGeometry(QtCore.QRect(60, 340, 93, 28))
        self.btrocarcelular.setObjectName(_fromUtf8("btrocarcelular"))
        self.CELULAR = QtGui.QLabel(usuario)
        self.CELULAR.setGeometry(QtCore.QRect(60, 270, 351, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Trebuchet MS"))
        font.setPointSize(9)
        self.CELULAR.setFont(font)
        self.CELULAR.setObjectName(_fromUtf8("CELULAR"))
        self.tendereco = QtGui.QLineEdit(usuario)
        self.tendereco.setGeometry(QtCore.QRect(480, 170, 373, 22))
        self.tendereco.setObjectName(_fromUtf8("tendereco"))
        self.label_7 = QtGui.QLabel(usuario)
        self.label_7.setGeometry(QtCore.QRect(480, 100, 61, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Trebuchet MS"))
        font.setPointSize(9)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.btrocarende = QtGui.QPushButton(usuario)
        self.btrocarende.setGeometry(QtCore.QRect(480, 200, 93, 28))
        self.btrocarende.setObjectName(_fromUtf8("btrocarende"))
        self.ENDERECO = QtGui.QLabel(usuario)
        self.ENDERECO.setGeometry(QtCore.QRect(480, 130, 311, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Trebuchet MS"))
        font.setPointSize(9)
        self.ENDERECO.setFont(font)
        self.ENDERECO.setObjectName(_fromUtf8("ENDERECO"))
        self.tnomerest = QtGui.QLineEdit(usuario)
        self.tnomerest.setGeometry(QtCore.QRect(480, 310, 373, 22))
        self.tnomerest.setObjectName(_fromUtf8("tnomerest"))
        self.label_6 = QtGui.QLabel(usuario)
        self.label_6.setGeometry(QtCore.QRect(480, 240, 211, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Trebuchet MS"))
        font.setPointSize(9)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.btrocarnome = QtGui.QPushButton(usuario)
        self.btrocarnome.setGeometry(QtCore.QRect(480, 340, 93, 28))
        self.btrocarnome.setObjectName(_fromUtf8("btrocarnome"))
        self.NOMEREST = QtGui.QLabel(usuario)
        self.NOMEREST.setGeometry(QtCore.QRect(480, 270, 321, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Trebuchet MS"))
        font.setPointSize(9)
        self.NOMEREST.setFont(font)
        self.NOMEREST.setObjectName(_fromUtf8("NOMEREST"))
        self.tdescricao = QtGui.QLineEdit(usuario)
        self.tdescricao.setGeometry(QtCore.QRect(60, 500, 373, 61))
        self.tdescricao.setObjectName(_fromUtf8("tdescricao"))
        self.label_8 = QtGui.QLabel(usuario)
        self.label_8.setGeometry(QtCore.QRect(60, 390, 71, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Trebuchet MS"))
        font.setPointSize(9)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.bdescricao = QtGui.QPushButton(usuario)
        self.bdescricao.setGeometry(QtCore.QRect(60, 570, 93, 28))
        self.bdescricao.setObjectName(_fromUtf8("bdescricao"))
        self.LDESCRICAOWW = QtGui.QLabel(usuario)
        self.LDESCRICAOWW.setGeometry(QtCore.QRect(60, 430, 381, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Trebuchet MS"))
        font.setPointSize(9)
        self.LDESCRICAOWW.setFont(font)
        self.LDESCRICAOWW.setObjectName(_fromUtf8("LDESCRICAOWW"))
        self.tbairro = QtGui.QLineEdit(usuario)
        self.tbairro.setGeometry(QtCore.QRect(480, 460, 373, 22))
        self.tbairro.setObjectName(_fromUtf8("tbairro"))
        self.label_9 = QtGui.QLabel(usuario)
        self.label_9.setGeometry(QtCore.QRect(480, 390, 61, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Trebuchet MS"))
        font.setPointSize(9)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.btrocarbairro = QtGui.QPushButton(usuario)
        self.btrocarbairro.setGeometry(QtCore.QRect(480, 490, 93, 28))
        self.btrocarbairro.setObjectName(_fromUtf8("btrocarbairro"))
        self.LBAIRRO = QtGui.QLabel(usuario)
        self.LBAIRRO.setGeometry(QtCore.QRect(480, 420, 311, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Trebuchet MS"))
        font.setPointSize(9)
        self.LBAIRRO.setFont(font)
        self.LBAIRRO.setObjectName(_fromUtf8("LBAIRRO"))


############################################## mostrar os dados do usuario na tela
        self.EMAIL.setText(d['cozinheiro'][self.c]['email'])
        self.LBAIRRO.setText(d['cozinheiro'][self.c]['bairro'])
        self.CELULAR.setText(d['cozinheiro'][self.c]['celular'])
        self.NOMEREST.setText(d['cozinheiro'][self.c]['restaurante'])
        self.ENDERECO.setText(d['cozinheiro'][self.c]['endereco'])
        self.LDESCRICAOWW.setText(d['cozinheiro'][self.c]['descricao'])


        self.btrocarbairro.clicked.connect(self.trocarbairro)

        self.btrocarcelular.clicked.connect(self.trocarcel)

        self.btrocaremail.clicked.connect(self.trocaremail)

        self.btrocarnome.clicked.connect(self.trocarrest)

        self.btrocarende.clicked.connect(self.trocarend)

        self.bdescricao.clicked.connect(self.trocardes)

        self.retranslateUi(usuario)
        QtCore.QMetaObject.connectSlotsByName(usuario)


    def retranslateUi(self, usuario):
        usuario.setWindowTitle(_translate("usuario", "Usuário", None))
        self.label.setText(_translate("usuario", "Usuário", None))
        self.label_5.setText(_translate("usuario", "  Email", None))
        self.btrocaremail.setText(_translate("usuario", "Trocar", None))
        self.label_10.setText(_translate("usuario", "Celular", None))
        self.btrocarcelular.setText(_translate("usuario", "Trocar", None))
        self.label_7.setText(_translate("usuario", "Endereço", None))
        self.btrocarende.setText(_translate("usuario", "Trocar", None))
        self.label_6.setText(_translate("usuario", "Nome do Restaurante", None))
        self.btrocarnome.setText(_translate("usuario", "Trocar", None))
        self.label_8.setText(_translate("usuario", "Descrição", None))
        self.bdescricao.setText(_translate("usuario", "Trocar", None))
        self.label_9.setText(_translate("usuario", "Bairro", None))
        self.btrocarbairro.setText(_translate("usuario", "Trocar", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    usuario = QtGui.QDialog()
    ui = Ui_usuario(c)
    ui.setupUi(usuario)
    usuario.show()
    sys.exit(app.exec_())

