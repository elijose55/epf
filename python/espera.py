# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'espera.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import json

with open('dict.json','r') as cf:
    d=json.load(cf)

###################### codigo do API do google para criar o mapa com a rota #######################
def localizacao (o, d):
    origem = o 
    dest = d 
    
    html_head = \
"""
<!DOCTYPE html>
<html>
  <head>
    <meta name="viewport" content="initial-scale=1.0, user-scalable=no">
    <meta charset="utf-8">
    <title>Directions service</title>
    <style>
      /* Always set the map height explicitly to define the size of the div
       * element that contains the map. */
      #map {
        height: 100%;
      }
      /* Optional: Makes the sample page fill the window. */
      html, body {
        height: 100%;
        margin: 0;
        padding: 0;
      }
      #floating-panel {
        position: absolute;
        top: 10px;
        left: 25%;
        z-index: 5;
        background-color: #fff;
        padding: 5px;
        border: 1px solid #999;
        text-align: center;
        font-family: 'Roboto','sans-serif';
        line-height: 30px;
        padding-left: 10px;
      }
    </style>
  </head>
  <body>
    <div id="map"></div>
    <script>
      function initMap() {
        var directionsService = new google.maps.DirectionsService;
        var directionsDisplay = new google.maps.DirectionsRenderer;
        var map = new google.maps.Map(document.getElementById('map'), {
          zoom: 14,
          center: {lat: -23.59, lng: -46.67}
        });
        calculateAndDisplayRoute(directionsService, directionsDisplay);
        directionsDisplay.setMap(map);

        var onChangeHandler = function() {
          calculateAndDisplayRoute(directionsService, directionsDisplay);
        };
        document.getElementById('start').addEventListener('change', onChangeHandler);
        document.getElementById('end').addEventListener('change', onChangeHandler);
      }

      function calculateAndDisplayRoute(directionsService, directionsDisplay) {
        directionsService.route({
"""
    fmt = "\n          origin: \"{0}\"," + \
          "\n          destination: \"{1}\","  
    
    html_fromto = fmt.format (origem, dest)
    
    html_trailer = \
"""
          travelMode: 'DRIVING'
        }, function(response, status) {
          if (status === 'OK') {
            directionsDisplay.setDirections(response);
          } else {
            window.alert('Directions request failed due to ' + status);
          }
        });
      }
    </script>
    <script async defer
    src="https://maps.googleapis.com/maps/api/js?key=AIzaSyBzeQVOmI0Sdb3ZilDFASetZaSudW6RAkU&callback=initMap">
    </script>
  </body>
</html>
"""
    html = html_head + html_fromto + html_trailer
    
    return html

#############################################################################


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

class Ui_MainWindow(object):

    def __init__ (self,x,c):
        with open('dict.json','r') as cf:
            d=json.load(cf)
            self.x = x
            self.c = c
            self.opcao = d['cozinheiro'][self.c]['endereco'] #variavel para que o mapa continue a aparecer mesmo sem endereco de origem

    def cancel(self):
        d['clientes'][self.x]['pedido'] = []

        with open('dict.json','w') as file:
            json.dump(d, file, indent=1)

        msg=QtGui.QMessageBox()
        msg.setIcon(QtGui.QMessageBox.Information)
        msg.setWindowTitle('Aviso')
        msg.setText('Pedido Cancelado')
        msg.setStandardButtons(QtGui.QMessageBox.Ok)
        msg.exec_()
        QtGui.QMainWindow.close(self.MainWindow)

    def mapa(self):
        self.opcao = self.tendereco.text()
        self.origem = self.opcao
        self.dest = d['cozinheiro'][self.c]['endereco']
        html = localizacao(self.origem,self.dest)
        self.webView.setHtml(html)


    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(810, 780)
        MainWindow.setMinimumSize(QtCore.QSize(810, 780))
        MainWindow.setMaximumSize(QtCore.QSize(810, 780))
        self.MainWindow = MainWindow
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.webView = QtWebKit.QWebView(self.centralwidget)
        self.webView.setGeometry(QtCore.QRect(20, 20, 771, 571))
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.webView.setObjectName(_fromUtf8("webView"))
        self.lstatus = QtGui.QLabel(self.centralwidget)
        self.lstatus.setGeometry(QtCore.QRect(230, 680, 500, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lstatus.setFont(font)
        self.lstatus.setObjectName(_fromUtf8("lstatus"))
        self.brota = QtGui.QPushButton(self.centralwidget)
        self.brota.setGeometry(QtCore.QRect(690, 600, 93, 31))
        self.brota.setObjectName(_fromUtf8("brota"))
        self.tendereco = QtGui.QLineEdit(self.centralwidget)
        self.tendereco.setGeometry(QtCore.QRect(300, 600, 381, 31))
        self.tendereco.setObjectName(_fromUtf8("tendereco"))
        self.bcancelar = QtGui.QPushButton(self.centralwidget)
        self.bcancelar.setGeometry(QtCore.QRect(670, 690, 111, 31))
        self.bcancelar.setObjectName(_fromUtf8("bcancelar"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 810, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.origem = self.opcao
        self.dest = d['cozinheiro'][self.c]['endereco']

        html = localizacao(self.origem,self.dest)
        self.webView.setHtml(html)
        self.lstatus.setText('Status do Pedido : Em Andamento')

        d['clientes'][self.x]['pedido'] = []



        self.bcancelar.clicked.connect(self.cancel)
        self.brota.clicked.connect(self.mapa)






        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.brota.setText(_translate("MainWindow", "Mostrar Rota", None))
        self.tendereco.setPlaceholderText(_translate("MainWindow", "Digite seu Endereço", None))
        self.bcancelar.setText(_translate("MainWindow", "Cancelar Pedido", None))

from PyQt4 import QtWebKit

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

