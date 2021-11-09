import sys, sqlite3, hashlib
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog, QApplication, QStackedWidget, QWidget, QFileDialog
import mp3_scrapper

class WelcomeScreen(QDialog):       #some OOP knowledge needed here
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        loadUi('5ndgui.ui', self)
        self.directory = None
        self.browsebutton.clicked.connect(self.browseDirectory)
        self.downloadbutton.clicked.connect(self.downloadfile)

    def browseDirectory(self):
        directory_name = QFileDialog.getExistingDirectory(self,'Select a download Folder', 'C:')  #selects a download folder
        self.directory = directory_name

    def downloadfile(self):
        print(self.directory)
        _link = self.linkField.text()
        self.error_label.setText('')
        self.successfull_label.setText('')
        if len(_link) > 0:
            if self.directory != None:
                result = mp3_scrapper.scrap(_link, self.directory)
                if result == 0:
                    self.error_label.setText('Invalid Link!')
                elif result == 1:
                    self.error_label.setText('')
                    self.successfull_label.setText('Download Successfull!')
            else:
                self.error_label.setText('Please select a download folder!')
        else:
            self.error_label.setText('Please put a link!')
    
#main app
app = QApplication(sys.argv)
wel = WelcomeScreen()
widget = QStackedWidget()
widget.addWidget(wel)
widget.setGeometry(200, 100, 822, 537)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print('Some Error Occured!')