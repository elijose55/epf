# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'telacardapio.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
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
    'restaurante': 'asterix',
    'descricao': 'Comida boa e caseira focada em massas e paes',
    'cardapio': []
    }
      }
      }

x='a'  ##colocar aqui o nome do usuario que entrou

class comida:
        def __init__(self,preco,tempo,nome):
            self.p=preco
            self.t=tempo
            self.n=nome

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


class Ui_telacardapio(object):

    def criar(self):
        pt = self.tprato.text()
        pt = str(pt)
        pr = self.tpreco.text()
        pr = float(pr)
        tt = self.ttempo.text()
        tt = int(tt)
        food = comida(pr,tt,pt)
        (d['cozinheiro'][x]['cardapio']).append(food)
        print(d['cozinheiro'][x]['cardapio'])

        self.textBrowser.setText('')

        self.textBrowser.append('{0} \n Preço: R${1} \n Tempo: {2} minutos \n' .format(pt,pr,tt))




    def setupUi(self, telacardapio):
        telacardapio.setObjectName(_fromUtf8("telacardapio"))
        telacardapio.setEnabled(True)
        telacardapio.resize(1322, 866)
        telacardapio.setMinimumSize(QtCore.QSize(1322, 866))
        telacardapio.setMaximumSize(QtCore.QSize(1322, 866))
        telacardapio.setFocusPolicy(QtCore.Qt.TabFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("minilogo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        telacardapio.setWindowIcon(icon)
        telacardapio.setInputMethodHints(QtCore.Qt.ImhNone)
        self.centralwidget = QtGui.QWidget(telacardapio)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.bcardapio = QtGui.QPushButton(self.centralwidget)
        self.bcardapio.setGeometry(QtCore.QRect(350, 520, 111, 31))
        self.bcardapio.setObjectName(_fromUtf8("bcardapio"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(840, 200, 101, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Trebuchet MS"))
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(170, 210, 141, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Trebuchet MS"))
        font.setPointSize(11)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.birpedidos = QtGui.QPushButton(self.centralwidget)
        self.birpedidos.setEnabled(True)
        self.birpedidos.setGeometry(QtCore.QRect(1060, 730, 111, 31))
        self.birpedidos.setInputMethodHints(QtCore.Qt.ImhNone)
        self.birpedidos.setCheckable(False)
        self.birpedidos.setProperty("ol", False)
        self.birpedidos.setObjectName(_fromUtf8("birpedidos"))
        self.blimpar = QtGui.QPushButton(self.centralwidget)
        self.blimpar.setGeometry(QtCore.QRect(840, 660, 93, 28))
        self.blimpar.setObjectName(_fromUtf8("blimpar"))
        self.blimpar_2 = QtGui.QPushButton(self.centralwidget)
        self.blimpar_2.setGeometry(QtCore.QRect(1070, 660, 93, 28))
        self.blimpar_2.setObjectName(_fromUtf8("blimpar_2"))
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(580, 20, 121, 111))
        self.label_7.setText(_fromUtf8(""))
        self.label_7.setPixmap(QtGui.QPixmap(_fromUtf8("pylogo.png")))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.textBrowser = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(830, 250, 341, 391))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.ttempo = QtGui.QLineEdit(self.centralwidget)
        self.ttempo.setGeometry(QtCore.QRect(170, 460, 485, 22))
        self.ttempo.setObjectName(_fromUtf8("ttempo"))
        self.label_10 = QtGui.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(170, 420, 485, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Trebuchet MS"))
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.tpreco = QtGui.QLineEdit(self.centralwidget)
        self.tpreco.setGeometry(QtCore.QRect(170, 370, 487, 22))
        self.tpreco.setObjectName(_fromUtf8("tpreco"))
        self.label_11 = QtGui.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(170, 330, 487, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Trebuchet MS"))
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.tprato = QtGui.QLineEdit(self.centralwidget)
        self.tprato.setGeometry(QtCore.QRect(170, 290, 489, 22))
        self.tprato.setObjectName(_fromUtf8("tprato"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(170, 260, 489, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Trebuchet MS"))
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        telacardapio.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(telacardapio)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1322, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuOpcoes = QtGui.QMenu(self.menubar)
        self.menuOpcoes.setObjectName(_fromUtf8("menuOpcoes"))
        telacardapio.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(telacardapio)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        telacardapio.setStatusBar(self.statusbar)
        self.busuario = QtGui.QAction(telacardapio)
        self.busuario.setObjectName(_fromUtf8("busuario"))
        self.bsair = QtGui.QAction(telacardapio)
        self.bsair.setObjectName(_fromUtf8("bsair"))
        self.menuOpcoes.addAction(self.busuario)
        self.menuOpcoes.addAction(self.bsair)
        self.menubar.addAction(self.menuOpcoes.menuAction())
        
        font.setFamily(_fromUtf8("Trebuchet MS"))
        font.setPointSize(11)
        self.textBrowser.setFont(font)

        self.bcardapio.clicked.connect(self.criar)

        self.retranslateUi(telacardapio)
        QtCore.QObject.connect(self.bsair, QtCore.SIGNAL(_fromUtf8("triggered()")), telacardapio.close)
        QtCore.QObject.connect(self.blimpar, QtCore.SIGNAL(_fromUtf8("clicked()")), self.textBrowser.clear)
        QtCore.QMetaObject.connectSlotsByName(telacardapio)

    def retranslateUi(self, telacardapio):
        telacardapio.setWindowTitle(_translate("telacardapio", "PyFood", None))
        self.bcardapio.setText(_translate("telacardapio", "ADICIONAR OU CRIAR", None))
        self.label.setText(_translate("telacardapio", "Cardápio", None))
        self.label_8.setText(_translate("telacardapio", "Editar Cardápio", None))
        self.birpedidos.setText(_translate("telacardapio", "Pedidos", None))
        self.blimpar.setText(_translate("telacardapio", "Limpar", None))
        self.blimpar_2.setText(_translate("telacardapio", "ATIVAR OU DESATIVAR", None))
        self.textBrowser.setHtml(_translate("telacardapio", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">frango a milanesa   R$15,00   20 min</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p></body></html>", None))
        self.label_10.setText(_translate("telacardapio", "Tempo (min)", None))
        self.label_11.setText(_translate("telacardapio", " Preço (R$)", None))
        self.label_3.setText(_translate("telacardapio", " Prato", None))
        self.menuOpcoes.setTitle(_translate("telacardapio", "Opções", None))
        self.busuario.setText(_translate("telacardapio", "Usuario", None))
        self.bsair.setText(_translate("telacardapio", "Sair", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    telacardapio = QtGui.QMainWindow()
    ui = Ui_telacardapio()
    ui.setupUi(telacardapio)
    telacardapio.show()
    sys.exit(app.exec_())

