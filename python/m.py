import requests

address = "1600 Amphitheatre Parkway, Mountain View, CA"
api_key = "AIzaSyBzeQVOmI0Sdb3ZilDFASetZaSudW6RAkU"
api_response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address={0}&key={1}'.format(address, api_key))
api_response_dict = api_response.json()

if api_response_dict['status'] == 'OK':
    latitude = api_response_dict['results'][0]['geometry']['location']['lat']
    longitude = api_response_dict['results'][0]['geometry']['location']['lng']
    print ('Latitude:', latitude)
    print ('Longitude:', longitude)









def localizacion(lat, lon):
    latitud=str(lat)
    longitud=str(lon)
    html= \
"""
<!DOCTYPE html>
<html>
  <head>
    <meta name="viewport" content="initial-scale=1.0, user-scalable=no">
    <meta charset="utf-8">
    <title>Simple markers</title>
    <style>
      html, body {
        height: 100%;
        margin: 0;
        padding: 0;
      }
      #map {
        height: 100%;
      }
    </style>
  </head>
  <body>
    <div id="map"></div>
    <script>

function initMap() {
  var myLatLng = {lat: """+latitud+""" , lng: """+longitud+"""};

  var map = new google.maps.Map(document.getElementById('map'), {
    zoom: 10,
    center: myLatLng
  });

  var marker = new google.maps.Marker({
    position: myLatLng,
    map: map,
    title: 'Mapa Prueba!'
  });
}

    </script>
    <script async defer
        src="https://maps.googleapis.com/maps/api/js?key=AIzaSyBzeQVOmI0Sdb3ZilDFASetZaSudW6RAkU&signed_in=true&callback=initMap"></script>
  </body>
</html>
"""
    return html







# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mapa.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(596, 342)
        self.webView = QtWebKit.QWebView(Dialog)
        self.webView.setGeometry(QtCore.QRect(170, 10, 421, 291))
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.webView.setObjectName(_fromUtf8("webView"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(30, 120, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(10, 30, 151, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 80, 151, 20))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(15, 10, 71, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 61, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButton_2 = QtGui.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(510, 310, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(430, 310, 75, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.pushButton.setText(_translate("Dialog", "ENCONTRAR", None))
        self.label.setText(_translate("Dialog", "LATITUD:", None))
        self.label_2.setText(_translate("Dialog", "LONGITUD:", None))
        self.pushButton_2.setText(_translate("Dialog", "SALIR", None))
        self.pushButton_3.setText(_translate("Dialog", "REGRESAR", None))

from PyQt4 import QtWebKit








#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Código creado por: Gibson Sneyder Ramírez Moreno
correo: sramirez.udea@gmail.com
http://pythoninicios.blogspot.com.co/
'''
import sys
from PyQt4.QtGui import QApplication
from PyQt4.QtCore import QUrl
from PyQt4.QtWebKit import QWebView

class showmap(QtGui.QDialog):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        QWebView.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
              
        QtCore.QObject.connect(self.ui.pushButton, QtCore.SIGNAL('clicked()'),self.calcular)
        QtCore.QObject.connect(self.ui.pushButton_3, QtCore.SIGNAL('clicked()'),self.regresar)
        QtCore.QObject.connect(self.ui.pushButton_2, QtCore.SIGNAL('clicked()'),self.salir)

    def calcular(self):
        latitud=self.ui.lineEdit.text()
        longitud=self.ui.lineEdit_2.text()
        html=localizacion(latitude,longitude)
        self.ui.webView.setHtml(html)
        
    def regresar(self):
        self.close()
        
    def salir(self):
        self.close()
        
if __name__== "__main__":
    app=QtGui.QApplication(sys.argv)
    myapp = showmap()
    myapp.show()
    sys.exit(app.exec_())