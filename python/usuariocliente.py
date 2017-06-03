# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'usuariocliente.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import json


x=''

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

class Ui_usuariocliente(object):
	def __init__(self,x):
		self.x = x
		with open('dict.json','r') as cf:
			d=json.load(cf)

	def trocarcel(self):
		cel = self.tcelular.text()
		d['clientes'][self.x]['celular'] = cel
		with open('dict.json','w') as file:
			json.dump(d, file, indent=1)
		self.tcelular.clear()
		self.CELULAR.setText(d['clientes'][self.x]['celular'])

	def trocaremail(self):
		email = self.temail.text()
		d['clientes'][self.x]['email'] = email
		with open('dict.json','w') as file:
			json.dump(d, file, indent=1)
		self.EMAIL.setText(d['clientes'][self.x]['email'])
		self.temail.clear()

	def trocarbairro(self):
		temp = self.tbairro.text()
		temp = str(temp)
		temp = temp.lstrip()
		temp = temp.lower()
		temp = temp.title()
		d['clientes'][self.x]['bairro'] = temp
		with open('dict.json','w') as file:
			json.dump(d, file, indent=1)
		self.BAIRRO.setText(d['clientes'][self.x]['bairro'])
		self.tbairro.clear()

	def setupUi(self, usuariocliente):
		usuariocliente.setObjectName(_fromUtf8("usuariocliente"))
		usuariocliente.resize(892, 647)
		usuariocliente.setMinimumSize(QtCore.QSize(892, 647))
		usuariocliente.setMaximumSize(QtCore.QSize(892, 647))
		self.EMAIL = QtGui.QLabel(usuariocliente)
		self.EMAIL.setGeometry(QtCore.QRect(60, 140, 331, 31))
		font = QtGui.QFont()
		font.setFamily(_fromUtf8("Trebuchet MS"))
		font.setPointSize(9)
		self.EMAIL.setFont(font)
		self.EMAIL.setObjectName(_fromUtf8("EMAIL"))
		self.label = QtGui.QLabel(usuariocliente)
		self.label.setGeometry(QtCore.QRect(400, 20, 161, 61))
		font = QtGui.QFont()
		font.setFamily(_fromUtf8("Trebuchet MS"))
		font.setPointSize(15)
		self.label.setFont(font)
		self.label.setObjectName(_fromUtf8("label"))
		self.CELULAR = QtGui.QLabel(usuariocliente)
		self.CELULAR.setGeometry(QtCore.QRect(60, 280, 351, 31))
		font = QtGui.QFont()
		font.setFamily(_fromUtf8("Trebuchet MS"))
		font.setPointSize(9)
		self.CELULAR.setFont(font)
		self.CELULAR.setObjectName(_fromUtf8("CELULAR"))
		self.label_7 = QtGui.QLabel(usuariocliente)
		self.label_7.setGeometry(QtCore.QRect(480, 110, 61, 31))
		font = QtGui.QFont()
		font.setFamily(_fromUtf8("Trebuchet MS"))
		font.setPointSize(9)
		self.label_7.setFont(font)
		self.label_7.setObjectName(_fromUtf8("label_7"))
		self.btrocaremail = QtGui.QPushButton(usuariocliente)
		self.btrocaremail.setGeometry(QtCore.QRect(60, 210, 93, 28))
		self.btrocaremail.setObjectName(_fromUtf8("btrocaremail"))
		self.label_10 = QtGui.QLabel(usuariocliente)
		self.label_10.setGeometry(QtCore.QRect(60, 250, 61, 31))
		font = QtGui.QFont()
		font.setFamily(_fromUtf8("Trebuchet MS"))
		font.setPointSize(9)
		self.label_10.setFont(font)
		self.label_10.setObjectName(_fromUtf8("label_10"))
		self.tbairro = QtGui.QLineEdit(usuariocliente)
		self.tbairro.setGeometry(QtCore.QRect(480, 180, 373, 22))
		self.tbairro.setObjectName(_fromUtf8("tbairro"))
		self.temail = QtGui.QLineEdit(usuariocliente)
		self.temail.setGeometry(QtCore.QRect(60, 180, 373, 22))
		self.temail.setObjectName(_fromUtf8("temail"))
		self.label_5 = QtGui.QLabel(usuariocliente)
		self.label_5.setGeometry(QtCore.QRect(50, 110, 61, 31))
		font = QtGui.QFont()
		font.setFamily(_fromUtf8("Trebuchet MS"))
		font.setPointSize(9)
		self.label_5.setFont(font)
		self.label_5.setObjectName(_fromUtf8("label_5"))
		self.BAIRRO = QtGui.QLabel(usuariocliente)
		self.BAIRRO.setGeometry(QtCore.QRect(480, 140, 311, 31))
		font = QtGui.QFont()
		font.setFamily(_fromUtf8("Trebuchet MS"))
		font.setPointSize(9)
		self.BAIRRO.setFont(font)
		self.BAIRRO.setObjectName(_fromUtf8("BAIRRO"))
		self.btrocarcelular = QtGui.QPushButton(usuariocliente)
		self.btrocarcelular.setGeometry(QtCore.QRect(60, 350, 93, 28))
		self.btrocarcelular.setObjectName(_fromUtf8("btrocarcelular"))
		self.tcelular = QtGui.QLineEdit(usuariocliente)
		self.tcelular.setGeometry(QtCore.QRect(60, 320, 373, 22))
		self.tcelular.setObjectName(_fromUtf8("tcelular"))
		self.btrocarbairro = QtGui.QPushButton(usuariocliente)
		self.btrocarbairro.setGeometry(QtCore.QRect(480, 210, 93, 28))
		self.btrocarbairro.setObjectName(_fromUtf8("btrocarbairro"))

############################################## mostrar os dados do usuario na tela
		self.EMAIL.setText(d['clientes'][self.x]['email'])
		self.BAIRRO.setText(d['clientes'][self.x]['bairro'])
		self.CELULAR.setText(d['clientes'][self.x]['celular'])

		self.btrocarbairro.clicked.connect(self.trocarbairro)

		self.btrocarcelular.clicked.connect(self.trocarcel)

		self.btrocaremail.clicked.connect(self.trocaremail)











		self.retranslateUi(usuariocliente)
		QtCore.QMetaObject.connectSlotsByName(usuariocliente)

	def retranslateUi(self, usuariocliente):
		usuariocliente.setWindowTitle(_translate("usuariocliente", "Dialog", None))
		self.label.setText(_translate("usuariocliente", "Usuário", None))
		self.label_7.setText(_translate("usuariocliente", "Bairro", None))
		self.btrocaremail.setText(_translate("usuariocliente", "Trocar", None))
		self.label_10.setText(_translate("usuariocliente", "Celular", None))
		self.label_5.setText(_translate("usuariocliente", "  Email", None))
		self.btrocarcelular.setText(_translate("usuariocliente", "Trocar", None))
		self.btrocarbairro.setText(_translate("usuariocliente", "Trocar", None))


if __name__ == "__main__":
	import sys
	app = QtGui.QApplication(sys.argv)
	usuariocliente = QtGui.QDialog()
	ui = Ui_usuariocliente(x)
	ui.setupUi(usuariocliente)
	usuariocliente.show()
	sys.exit(app.exec_())

