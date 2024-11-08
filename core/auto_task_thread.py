from core.pauseable_thread import PauseableThread
from core.auto_task_runner import AutoTaskRunner
from PyQt5.QtCore import pyqtSignal

class AutoTaskThread(PauseableThread):
    status = pyqtSignal(str)
    error = pyqtSignal(str)
    
    def __init__(self, driver, parent=None):
        super().__init__(parent)
        self._driver = driver
        
    @property
    def driver(self):
        return self._driver
    
    def run(self):
        try:
            self._run()
            
        except Exception as e:
            self.error.emit(str(e))
            
            if __debug__:
                raise e
            
    def _run(self):
        raise NotImplementedError