from PyQt5.QtWidgets import QDialog
from ui.ui_account_create_dialog import Ui_AccountCreateDialog
from core.auto_browser import AutoBrowser

class AccountCreateDialog(QDialog, Ui_AccountCreateDialog):
    def __init__(self, pickled=False, parent=None):
        super(QDialog, self).__init__(parent)
        super(Ui_AccountCreateDialog, self).__init__()
        self.setupUi(self)
        
        if not pickled:            
            self.finish_setup()
            
    def finish_setup(self):
        pass
    
    def delete_latest_account(self):
        raise NotImplementedError