# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'telareg.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

d={
    'clientes': {
    'eli':{
    'nome': 'elijose',
    'email': 'elijose55',
    'senha': 'elizao',
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
    'restaurante': 'asterix',
    'descricao': 'Comida boa e caseira focada em massas e paes',
    'cardapio': ''
    }
      }
      }
    

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
            if x not in d['cozinheiro']:
                d['cozinheiro'][x]={}

                username = self.tnome.text()
                username = str(username)
                d['cozinheiro'][x]['nome']=username

                username = self.temail.text()
                username = str(username)
                d['cozinheiro'][x]['email']=username

                username = self.tsenha.text()
                username = str(username)
                d['cozinheiro'][x]['senha']=username

                username = self.tbairro.text()
                username = str(username)
                username = username.lstrip()
                username = username.lower()
                username = username.title()
                d['cozinheiro'][x]['bairro']=username

                username = self.tcelular.text()
                username = str(username)
                d['cozinheiro'][x]['celular']=username

                username = self.tnomerest.text()
                username = str(username)
                d['cozinheiro'][x]['restaurante']=username

                username = self.tdescricao.text()
                username = str(username)
                d['cozinheiro'][x]['descricao']=username

                print (d)



            else:
                self.erro()

            self.telalog = QtGui.QMainWindow()
            self.ui= Ui_tlogin()
            self.ui.setupUi(self.telalog)
            self.telalog.show()
            self.telareg.close
            print(d)



    def setupUi(self, telareg):
        telareg.setObjectName(_fromUtf8("telareg"))
        telareg.resize(976, 652)
        telareg.setMinimumSize(QtCore.QSize(976, 652))
        telareg.setMaximumSize(QtCore.QSize(976, 652))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("minilogo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        telareg.setWindowIcon(icon)
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
        self.bregistar.setGeometry(QtCore.QRect(440, 520, 111, 41))
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
        self.label.raise_()
        self.label_3.raise_()
        self.bregistar.raise_()
        self.label_2.raise_()
        self.tlogin.raise_()
        self.label_3.raise_()
        self.tsenha.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.temail.raise_()
        self.tnome.raise_()
        self.label_7.raise_()
        self.label_6.raise_()
        self.tdescricao.raise_()
        self.label_8.raise_()
        self.tcelular.raise_()
        self.label_4.raise_()
        self.tcelular.raise_()
        self.label_3.raise_()
        self.label_2.raise_()
        self.tnome.raise_()
        self.label_5.raise_()
        self.label_7.raise_()
        self.tbairro.raise_()
        self.tsenha.raise_()
        self.label_6.raise_()
        self.tlogin.raise_()
        self.label_8.raise_()
        self.temail.raise_()
        self.tdescricao.raise_()
        self.label_9.raise_()
        self.tnomerest.raise_()
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

        self.retranslateUi(telareg)
        QtCore.QObject.connect(self.bvoltar, QtCore.SIGNAL(_fromUtf8("triggered()")), telareg.close)
        QtCore.QMetaObject.connectSlotsByName(telareg)

        self.bregistar.clicked.connect(self.registro)

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

