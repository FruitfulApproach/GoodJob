from PyQt5.QtWidgets import QMainWindow
from ui.ui_main_window import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)
        

        
        
        
        