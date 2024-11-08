from PyQt5.QtCore import QThread, QMutex, QWaitCondition, pyqtSignal, QObject

class PauseableThread(QThread):
    paused = pyqtSignal()
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self._pauseMutex = QMutex()
        self._pauseCond = QWaitCondition()
        self._paused = False
    
    @property
    def is_paused(self):
        return self._paused

    def pause(self):
        if not self._paused:
            self._pauseMutex.lock()
            self._paused = True
            self._pauseMutex.unlock()
            self.paused.emit()
    
    def resume(self):
        if self.is_paused:
            self._pauseMutex.lock()
            self._paused = False
            self._pauseMutex.unlock()
            self._pauseCond.wakeAll()
    
    def check_pause(self):
        self._pauseMutex.lock()
        if self.is_paused:
            self._pauseCond.wait(self._pauseMutex)
        self._pauseMutex.unlock()    