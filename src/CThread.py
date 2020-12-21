from PyQt5.QtCore import QThread, pyqtSignal
import time, math, Settings

class CThread(QThread):
    valueChanged = pyqtSignal([int])
    def __init__(self,value):
        super().__init__()
        self.stop_fill = False
        Settings.completed = value


    def run(self):
        if Settings.completed < 100:
            time.sleep(0.1)
            Settings.completed += Settings.percentPerItem
            self.valueChanged.emit(int(math.ceil(Settings.completed)))
