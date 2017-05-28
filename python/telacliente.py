# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'telacliente.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!




    




from PyQt4 import QtCore, QtGui
from telafinalizar import Ui_telafinalizar
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

class Ui_telacliente(object):
    def __init__ (self,x):
        self.T=0
        self.P=0
        self.pedidotemp=[]
        self.c=''
        self.x=x  #cliente logado




    def bairro(self): ##obter os restaurantes que estao no mesmo bairro do cliente
        self.pedidotemp=[]
        r=[]
        ww=[]

        with open('dict.json','r') as cf:
            d=json.load(cf)


        b=d['clientes'][self.x]['bairro']
        for i in d['cozinheiro']:
            if b==d['cozinheiro'][i]['bairro'] and d['cozinheiro'][i]['status']=='online':
                ww.append((i,d['cozinheiro'][i]['restaurante']))
                r.append(d['cozinheiro'][i]['restaurante'])
        return ww

        ##mostrar r na lista de restaurantes proximos
        




    def khara(self,item): ##definir o nome do dicionario do dicionario escolhido
            for name in d['cozinheiro']:
                if d['cozinheiro'][name]['restaurante'] == item:
                    nm = name
                    self.c=nm
                    return nm

    def retirar(self): #quando o botao retirar for acionado



        v=self.nquantidade.value() ##valor do seletor da quantidade de pratos

        it=self.scomidas.currentText() ##retorna o texto atual do seletor de comida

        index=self.scomidas.currentIndex() ##retorna o indice na lista da comida selecionada

        lc=d['cozinheiro'][nm]['cardapio'][:]

        df=lc[index][:] ## df= lista da comida a ser retirada

        dt=df[:]

        if v!=0:

            self.T=0
            self.P=0

            self.carrinhoww.setText('')

            for i in self.pedidotemp: 
                itemp=i
                if it in itemp:
                    itemp[3]-=v #retirando a quantidade
                    if itemp[3]<=0:
                        self.pedidotemp.remove(itemp) #se a quantidade final for menor que 0 o item e retirado do carrinho
                    itemp[0]-=df[0]*v #retirando do preco
                    itemp[1]-=df[1]*v #retirando do tempo

            for i in self.pedidotemp:
                objeto = i
                nn=objeto[2] #nome
                pp=objeto[0] #preco
                tt=objeto[1] #tempo de preparo
                qq=objeto[3] #quantidade
                self.T+=tt #tempo total
                self.P+=pp #preco total
                
                self.carrinhoww.append('{0}     x{3} \n Preço: R${1:.2f} \n Tempo: {2} minutos \n' .format(nn,pp,tt,qq)) ##printar os dados de cada lista de comidas no box do carrinho


        self.TEMPOW.setText('{0}' .format(self.T))




    def add(self): ##quando o botao adicionar for acionado


        

 

        v=self.nquantidade.value() ##valor do seletor da quantidade de pratos

        it=self.scomidas.currentText() ##retorna o texto atual do seletor de comida

        index=self.scomidas.currentIndex() ##retorna o indice na lista da comida selecionada

        lc=d['cozinheiro'][nm]['cardapio'][:]

        df=lc[index][:] ## df= lista da comida adicionada ao carrinho

        dt=df[:]

        if v!=0:
            self.carrinhoww.setText('')
            xtemp=0

            self.T=0
            self.P=0

            for i in self.pedidotemp:
                itemp=i
                if it in itemp:
                    itemp[3]+=v #adicionado a quantidade
                    itemp[0]+=df[0]*v #adicionando ao preco
                    itemp[1]+=df[1]*v #adicionando ao tempo
                    xtemp=1


            if xtemp==0:
                dt[0]*=v #mudando o preco total
                dt[1]*=v #mudando o tempo total
                dt.append(v) #adicionando a quantidade
                self.pedidotemp.append(dt) #adicionando a lista da comida ao pedido temporario


            for i in self.pedidotemp:
                objeto = i
                nn=objeto[2] #nome
                pp=objeto[0] #preco
                tt=objeto[1] #tempo de preparo
                qq=objeto[3] #quantidade
                self.T+=tt #tempo total
                self.P+=pp #preco total
                
                self.carrinhoww.append('{0}     x{3} \n Preço: R${1:.2f} \n Tempo: {2} minutos \n' .format(nn,pp,tt,qq)) ##printar os dados de cada lista de comidas no box do carrinho


        self.TEMPOW.setText('{0}' .format(self.T))

            





    def getitem(self):
        self.pedidotemp=[]
        self.carrinhoww.setText('')
        item=self.srestaurante.currentText()
        global nm
        nm = self.khara(item)



        
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Trebuchet MS"))
        font.setPointSize(12)
        self.NOMERESTAURANTE.setFont(font)
        self.NOMERESTAURANTE.setText(item)

        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Trebuchet MS"))
        font.setPointSize(11)
        self.descricaowrest.setFont(font)
        self.descricaowrest.setText(d['cozinheiro'][nm]['descricao']) #printar descricao do restaurante no box de descricao


        self.cardapioww.setFont(font)
        lc=d['cozinheiro'][nm]['cardapio']
        self.cardapioww.setText('')

        for i in lc:
            objeto = i

            
            nn=objeto[2] #nome
            pp=objeto[0] #preco
            tt=objeto[1] #tempo de preparo

            self.scomidas.addItem(nn)  #adicionando as comidas na lista de selecao de comidas
            
           
            self.cardapioww.append('{0} \n Preço: R${1:.2f} \n Tempo: {2} minutos \n' .format(nn,pp,tt)) ##printar os dados de cada lista de comidas no box do cardapio

        self.nquantidade.setMinimum(0)

        self.nquantidade.setMaximum(10)



    def finalizar(self):


        d['clientes'][self.x]['temp'] = self.pedidotemp

        with open('dict.json','w') as file:
            json.dump(d, file, indent=1)

        self.final = QtGui.QMainWindow()
        self.ui= Ui_telafinalizar(self.x,self.c)
        self.ui.setupUi(self.final)
        self.final.show()

    def setupUi(self, telacliente):

        telacliente.setObjectName(_fromUtf8("telacliente"))
        telacliente.resize(1366, 870)
        telacliente.setMinimumSize(QtCore.QSize(1366, 870))
        telacliente.setMaximumSize(QtCore.QSize(1366, 870))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("minilogo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        telacliente.setWindowIcon(icon)
        telacliente.setDocumentMode(True)
        telacliente.setDockNestingEnabled(False)
        telacliente.setUnifiedTitleAndToolBarOnMac(True)
        self.centralwidget = QtGui.QWidget(telacliente)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 170, 391, 131))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Trebuchet MS"))
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.srestaurante = QtGui.QComboBox(self.centralwidget)
        self.srestaurante.setGeometry(QtCore.QRect(80, 280, 231, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Trebuchet MS"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.srestaurante.setFont(font)
        self.srestaurante.setObjectName(_fromUtf8("srestaurante"))
        self.combo = QtGui.QLabel('')
        self.bselecionar = QtGui.QPushButton(self.centralwidget)
        self.bselecionar.setGeometry(QtCore.QRect(80, 340, 93, 28))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Trebuchet MS"))
        font.setPointSize(9)
        self.bselecionar.setFont(font)
        self.bselecionar.setObjectName(_fromUtf8("bselecionar"))
        self.descricaowrest = QtGui.QTextBrowser(self.centralwidget)
        self.descricaowrest.setGeometry(QtCore.QRect(80, 470, 301, 321))
        self.descricaowrest.setObjectName(_fromUtf8("descricaowrest"))
        self.NOMERESTAURANTE = QtGui.QLabel(self.centralwidget)
        self.NOMERESTAURANTE.setGeometry(QtCore.QRect(80, 430, 211, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Trebuchet MS"))
        font.setPointSize(9)
        self.NOMERESTAURANTE.setFont(font)
        self.NOMERESTAURANTE.setObjectName(_fromUtf8("NOMERESTAURANTE"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(170, 60, 391, 131))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Trebuchet MS"))
        font.setPointSize(13)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.cardapioww = QtGui.QTextBrowser(self.centralwidget)
        self.cardapioww.setGeometry(QtCore.QRect(510, 300, 311, 321))
        self.cardapioww.setObjectName(_fromUtf8("cardapioww"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(590, 20, 161, 151))
        self.label.setText(_fromUtf8(""))
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("pylogo.png")))
        self.label.setScaledContents(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.nquantidade = QtGui.QSpinBox(self.centralwidget)
        self.nquantidade.setGeometry(QtCore.QRect(1210, 300, 46, 22))
        self.nquantidade.setObjectName(_fromUtf8("nquantidade"))
        self.scomidas = QtGui.QComboBox(self.centralwidget)
        self.scomidas.setGeometry(QtCore.QRect(960, 300, 201, 21))
        self.scomidas.setObjectName(_fromUtf8("scomidas"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(960, 220, 391, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Trebuchet MS"))
        font.setPointSize(13)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.carrinhoww = QtGui.QTextBrowser(self.centralwidget)
        self.carrinhoww.setGeometry(QtCore.QRect(960, 420, 301, 361))
        self.carrinhoww.setObjectName(_fromUtf8("carrinhoww"))
        self.badicionar = QtGui.QPushButton(self.centralwidget)
        self.badicionar.setGeometry(QtCore.QRect(1020, 350, 93, 28))
        self.badicionar.setObjectName(_fromUtf8("badicionar"))
        self.bfinalizar = QtGui.QPushButton(self.centralwidget)
        self.bfinalizar.setGeometry(QtCore.QRect(1170, 790, 93, 28))
        self.bfinalizar.setObjectName(_fromUtf8("bfinalizar"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(970, 800, 53, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.TEMPOW = QtGui.QLabel(self.centralwidget)
        self.TEMPOW.setGeometry(QtCore.QRect(1020, 800, 53, 16))
        self.TEMPOW.setObjectName(_fromUtf8("TEMPOW"))
        self.badicionar_2 = QtGui.QPushButton(self.centralwidget)
        self.badicionar_2.setGeometry(QtCore.QRect(1130, 350, 93, 28))
        self.badicionar_2.setObjectName(_fromUtf8("badicionar_2"))
        telacliente.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(telacliente)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1366, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuOp_es = QtGui.QMenu(self.menubar)
        self.menuOp_es.setObjectName(_fromUtf8("menuOp_es"))
        telacliente.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(telacliente)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        telacliente.setStatusBar(self.statusbar)
        self.blogout = QtGui.QAction(telacliente)
        self.blogout.setObjectName(_fromUtf8("blogout"))
        self.bsair = QtGui.QAction(telacliente)
        self.bsair.setObjectName(_fromUtf8("bsair"))
        self.menuOp_es.addAction(self.bsair)
        self.menubar.addAction(self.menuOp_es.menuAction())
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Trebuchet MS"))
        font.setPointSize(11)
        self.carrinhoww.setFont(font)

        self.retranslateUi(telacliente)
        QtCore.QObject.connect(self.bsair, QtCore.SIGNAL(_fromUtf8("triggered()")), telacliente.close)
        QtCore.QMetaObject.connectSlotsByName(telacliente)

        self.bfinalizar.clicked.connect(self.finalizar)

        self.bselecionar.clicked.connect(self.getitem)

        self.badicionar.clicked.connect(self.add)

        self.badicionar_2.clicked.connect(self.retirar)

        lista = self.bairro()
        print(lista)


        for item in lista:
            self.srestaurante.addItem(item[1])

    def retranslateUi(self, telacliente):
        telacliente.setWindowTitle(_translate("telacliente", "PyFood", None))
        self.label_2.setText(_translate("telacliente", "Restaurantes", None))
        self.bselecionar.setText(_translate("telacliente", "Selecionar", None))
        
        self.NOMERESTAURANTE.setText(_translate("telacliente", "NOME DO RESTAURANTE", None))
        self.label_4.setText(_translate("telacliente", "Cardápio", None))
        
        self.scomidas.setItemText(0, _translate("telacliente", "COMIDAAA", None))
        self.scomidas.setItemText(1, _translate("telacliente", "cocoooc", None))
        self.label_5.setText(_translate("telacliente", "Carrinho", None))

        self.badicionar.setText(_translate("telacliente", "Adicionar", None))
        self.bfinalizar.setText(_translate("telacliente", "Finalizar", None))
        self.label_3.setText(_translate("telacliente", "Tempo: ", None))
        self.TEMPOW.setText(_translate("telacliente", "", None))
        self.badicionar_2.setText(_translate("telacliente", "Retirar", None))
        self.menuOp_es.setTitle(_translate("telacliente", "Opções", None))
        self.blogout.setText(_translate("telacliente", "Logout", None))
        self.bsair.setText(_translate("telacliente", "Sair", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    telacliente = QtGui.QMainWindow()
    ui = Ui_telacliente()
    ui.setupUi(telacliente)
    telacliente.show()
    sys.exit(app.exec_())

