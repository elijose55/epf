# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'telapedidos.ui'
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

class Ui_telapedidos(object):

    def __init__ (self,c):
        self.c = c
        self.listaclientes = []

    def pronto (self):

        ##### mostrar os pedidos no box de pedidos
        lc = d['cozinheiro'][self.c]['pedido']
        self.pedidospend.setText('\n')
        self.listaclientes = []


        for i in lc:
            
              
            for o in lc[i]:
                objeto = o
                nn = objeto[2] #nome
                pp = objeto[0] #preco
                tt = objeto[1] #tempo de preparo
                qq = objeto[3] #quantidade
                cc = objeto[4] #cliente
                self.listaclientes.append(objeto[4]) #lista de clientes que fizeram um pedido com esse cozinheiro
                self.pedidospend.append('  {0}       x{3} \n Preço: R${1:.2f} \n Tempo: {2} minutos \n' .format(nn,pp,tt,qq))##printar os dados de cada lista de comidas no box do cardapio
                self.pedidospend.append(' Celular: {0}' .format(d['clientes'][cc]['celular']))
            #self.pedidospend.append('Cliente: {0} \n \n \n ' .format(cc))
            #self.scomidapronta.clear()
        #for i in self.listaclientes:
            #self.scomidapronta.addItem(cc)  #adicionando os clientes na lista de selecao de pedido pronto

        #index = self.scomidapronta.currentIndex()
        #clientepronto = self.listaclientes[index]
        #print(clientepronto)



        for i in lc:
            
              
            for o in lc[i]:
                objeto = o
                nn = objeto[2] #nome
                pp = objeto[0] #preco
                tt = objeto[1] #tempo de preparo
                qq = objeto[3] #quantidade
                cc = objeto[4] #cliente
                self.listaclientes.append(objeto[4]) #lista de clientes que fizeram um pedido com esse cozinheiro
                self.pedidospend.append('  {0}       x{3} \n Preço: R${1:.2f} \n Tempo: {2} minutos \n' .format(nn,pp,tt,qq))##printar os dados de cada lista de comidas no box do cardapio
                
            self.pedidospend.append('Cliente: {0} \n \n \n ' .format(cc))





        with open('dict.json','w') as file:
            json.dump(d, file, indent=1)








            
    def cancel(self): #funcao para cancelar os pedidos, assim ela tira o status de pendente do cozinheiro e de qualquer cliente que tenha feito pedidos para ele
        for i in d['clientes']:
            if i in self.listaclientes:
                d['clientes'][i]['pedido'] = []
                d['clientes'][i]['pentente'] = 'nao'
                del d['cozinheiro'][self.c]['pedido'][i]

        with open('dict.json','w') as file:
            json.dump(d, file, indent=1)

        msg=QtGui.QMessageBox()
        msg.setIcon(QtGui.QMessageBox.Information)
        msg.setWindowTitle('Aviso')
        msg.setText('Sessão Encerrada')
        msg.setStandardButtons(QtGui.QMessageBox.Ok)
        msg.exec_()
        QtGui.QMainWindow.close(self.telapedidos)

        
    def setupUi(self, telapedidos):
        telapedidos.setObjectName(_fromUtf8("telapedidos"))
        telapedidos.resize(481, 631)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../.designer/backup/minilogo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        telapedidos.setWindowIcon(icon)
        self.telapedidos = telapedidos
        self.centralwidget = QtGui.QWidget(telapedidos)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, -40, 391, 131))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Trebuchet MS"))
        font.setPointSize(17)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.caixacardapio_2 = QtGui.QTextBrowser(self.centralwidget)
        self.caixacardapio_2.setGeometry(QtCore.QRect(610, 990, 411, 401))
        self.caixacardapio_2.setObjectName(_fromUtf8("caixacardapio_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(630, 920, 101, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Trebuchet MS"))
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.bcancelar = QtGui.QPushButton(self.centralwidget)
        self.bcancelar.setGeometry(QtCore.QRect(310, 550, 93, 28))
        self.bcancelar.setObjectName(_fromUtf8("bcancelar"))
        self.bpronta = QtGui.QPushButton(self.centralwidget)
        self.bpronta.setGeometry(QtCore.QRect(90, 550, 93, 28))
        self.bpronta.setObjectName(_fromUtf8("bpronta"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(180, -60, 121, 111))
        self.label_4.setText(_fromUtf8(""))
        self.label_4.setPixmap(QtGui.QPixmap(_fromUtf8("../../.designer/backup/pylogo.png")))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.pedidospend = QtGui.QTextBrowser(self.centralwidget)
        self.pedidospend.setGeometry(QtCore.QRect(80, 90, 331, 381))
        self.pedidospend.setObjectName(_fromUtf8("pedidospend"))
        telapedidos.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(telapedidos)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 481, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuOp_es = QtGui.QMenu(self.menubar)
        self.menuOp_es.setObjectName(_fromUtf8("menuOp_es"))
        telapedidos.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(telapedidos)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        telapedidos.setStatusBar(self.statusbar)
        self.bsair = QtGui.QAction(telapedidos)
        self.bsair.setObjectName(_fromUtf8("bsair"))
        self.menuOp_es.addAction(self.bsair)
        self.menubar.addAction(self.menuOp_es.menuAction())

        self.bpronta.clicked.connect(self.pronto)

        self.bcancelar.clicked.connect(self.cancel)

        ##### mostrar os pedidos no box de pedidos
        lc = d['cozinheiro'][self.c]['pedido']
        self.pedidospend.setText('\n')
        self.listaclientes = []


        for i in lc:
            
              
            for o in lc[i]:
                objeto = o
                nn = objeto[2] #nome
                pp = objeto[0] #preco
                tt = objeto[1] #tempo de preparo
                qq = objeto[3] #quantidade
                cc = objeto[4] #cliente
                self.listaclientes.append(objeto[4]) #lista de clientes que fizeram um pedido com esse cozinheiro
                self.pedidospend.append('  {0}       x{3} \n Preço: R${1:.2f} \n Tempo: {2} minutos \n' .format(nn,pp,tt,qq))##printar os dados de cada lista de comidas no box do cardapio
                


        self.retranslateUi(telapedidos)
        QtCore.QObject.connect(self.bsair, QtCore.SIGNAL(_fromUtf8("triggered()")), telapedidos.close)
        QtCore.QMetaObject.connectSlotsByName(telapedidos)

    def retranslateUi(self, telapedidos):
        telapedidos.setWindowTitle(_translate("telapedidos", "PyFood", None))
        self.label_2.setText(_translate("telapedidos", "Pedidos", None))
        self.label_3.setText(_translate("telapedidos", "Pendentes", None))
        self.bcancelar.setText(_translate("telapedidos", "Encerrar", None))
        self.bpronta.setText(_translate("telapedidos", "Atualizar", None))
        self.menuOp_es.setTitle(_translate("telapedidos", "Opções", None))
        self.bsair.setText(_translate("telapedidos", "Sair", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    telapedidos = QtGui.QMainWindow()
    ui = Ui_telapedidos()
    ui.setupUi(telapedidos)
    telapedidos.show()
    sys.exit(app.exec_())

