# AUTHOR - HIMANK JESHWAR
# DATE - 13/08/21

import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class Main_Screen(QMainWindow):
    def __init__(self):
        super(Main_Screen,self).__init__()
        self.browser=QWebEngineView()
        self.browser.setUrl(QUrl("https://bing.com"))
        self.setCentralWidget(self.browser)
        self.show()

        # Navigation Bar
        navbar=QToolBar()
        self.addToolBar(navbar)

        # Back Button
        back_button=QAction("Back",self)
        back_button.triggered.connect(self.browser.back)
        navbar.addAction(back_button)

        # Forward Button
        forward_button=QAction("    Forward",self)
        forward_button.triggered.connect(self.browser.forward)
        navbar.addAction(forward_button)

        # Reload Button
        reload_button=QAction("    Reload",self)
        reload_button.triggered.connect(self.browser.reload)
        navbar.addAction(reload_button)

        # Home Button
        home_button=QAction("   Home",self)
        home_button.triggered.connect(self.navigate_home)
        navbar.addAction(home_button)
        self.urlBar=QLineEdit()
        self.urlBar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.urlBar)

        self.browser.urlChanged.connect(self.update_url)
    def navigate_home(self):
        self.browser.setUrl(QUrl("https://bing.com")) 
    def navigate_to_url(self):
        url=self.urlBar.text()
        self.browser.setUrl(QUrl(url))    
    def update_url(self,url):
        self.urlBar.setText(url.toString())    


app=QApplication(sys.argv)
QApplication.setApplicationName("Butterfly Browser")
screen=Main_Screen()
app.exec_()