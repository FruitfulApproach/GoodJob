from PyQt5.QtWidgets import QMainWindow
from ui.ui_main_window import Ui_MainWindow
from dialog.account_create_dialog import AccountCreateDialog

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, pickled=False, parent=None):
        super(QMainWindow, self).__init__(parent)
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)
        
        if not pickled:
            self.account_create_dialog = AccountCreateDialog(parent=self)
            self.finish_setup()
            
    def finish_setup(self):
        self.actionCreateAccount.triggered.connect(self.show_account_create_dialog)
        
    def show_account_create_dialog(self):
        result = self.account_create_dialog.exec_()
        
        if result == self.account_create_dialog.Rejected:
            self.account_create_dialog.delete_latest_account()
        
        

        
        
        
        