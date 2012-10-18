#!/usr/bin/env python



from PyQt4 import QtCore, QtGui, QtNetwork, QtWebKit
import settings


class MainWindow(QtGui.QMainWindow):
    def __init__(self, url):
        super(MainWindow, self).__init__()

        self.progress = 0

        
        QtNetwork.QNetworkProxyFactory.setUseSystemConfiguration(True)

        self.view = QtWebKit.QWebView(self)
        self.view.load(url)
        self.view.loadFinished.connect(self.adjustLocation)
        self.view.titleChanged.connect(self.adjustTitle)
        self.view.loadProgress.connect(self.setProgress)

        self.locationEdit = QtGui.QLineEdit(self)
        self.locationEdit.setSizePolicy(QtGui.QSizePolicy.Expanding,
                self.locationEdit.sizePolicy().verticalPolicy())
        self.locationEdit.returnPressed.connect(self.changeLocation)

        toolBar = self.addToolBar("Navigation")
        toolBar.addWidget(self.locationEdit)


        
        self.setCentralWidget(self.view)
        self.setUnifiedTitleAndToolBarOnMac(True)

    def viewSource(self):
        accessManager = self.view.page().networkAccessManager()
        request = QtNetwork.QNetworkRequest(self.view.url())
        reply = accessManager.get(request)
        reply.finished.connect(self.slotSourceDownloaded)

    def slotSourceDownloaded(self):
        reply = self.sender()
        self.textEdit = QtGui.QTextEdit(None)
        self.textEdit.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.textEdit.show()
        self.textEdit.setPlainText(QtCore.QTextStream(reply).readAll())
        self.textEdit.resize(600, 400)
        reply.deleteLater()
        
    def adjustLocation(self):
        self.locationEdit.setText(self.view.url().toString())

    def changeLocation(self):
        url = QtCore.QUrl.fromUserInput(self.locationEdit.text())
        self.view.load(url)
        self.view.setFocus()

    def adjustTitle(self):
        if 0 < self.progress < 100:
            self.setWindowTitle("%s (%s%%)" % (self.view.title(), self.progress))
        else:
            self.setWindowTitle(self.view.title())

    def setProgress(self, p):
        self.progress = p
        self.adjustTitle()




if __name__ == '__main__':

    import sys

    app = QtGui.QApplication(sys.argv)

    url = QtCore.QUrl(settings.APP_AUTH_URL)
        

    browser = MainWindow(url)
    browser.show()
    

    sys.exit(app.exec_())
