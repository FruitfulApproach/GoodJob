from PyQt5.QtWidgets import QDialog
from ui.ui_account_create_dialog import Ui_AccountCreateDialog
from core.auto_task_runner import AutoTaskRunner
from task.create_gmail_account import CreateGmailAccount

class AccountCreateDialog(QDialog, Ui_AccountCreateDialog):
    def __init__(self, pickled=False, parent=None):
        super(QDialog, self).__init__(parent)
        super(Ui_AccountCreateDialog, self).__init__()
        self.setupUi(self)
        
        if not pickled:            
            self.finish_setup()
            
    def finish_setup(self):
        self.createGmailAccountButton.clicked.connect(self.create_gmail_account)
        self.gmailGenderCombo.currentTextChanged.connect(self.gender_selection_changed)
        
    def gender_selection_changed(self):
        gender = self.gmailGenderCombo.currentText()
        self.customGenderGroup.setEnabled(gender == "Custom")            
    
    def delete_latest_account(self):
        raise NotImplementedError
    
    def create_gmail_account(self):
        runner = AutoTaskRunner()        
        first_name = self.gmailFirstNameLine.text()
        last_name = self.gmailLastNameLine.text()
        birthday = self.gmailBirthdayEdit.date()
        gender = self.gmailGenderCombo.currentText()
        password = self.gmailPasswordLine.text()
        create_gmail = CreateGmailAccount(
            runner.driver, first_name, last_name, birthday, gender, password)
        create_gmail.status.connect(self.status_message)
        create_gmail.error.connect(self.status_message)
        runner.push_thread(create_gmail)
        
    def status_message(self, msg):
        self.gmailStatusText.appendPlainText(f'{msg}\n')
    
    