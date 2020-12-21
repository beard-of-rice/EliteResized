from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, QThreadPool
from EliteResizedUI import Ui_MainWindow
import Settings, Worker, CThread, orjson, sys, os, math, time, traceback
from PIL import Image

class MainWindowUIClass(Ui_MainWindow):
    userprofile = os.environ['USERPROFILE']
    journalDir = f'{userprofile}\Saved Games\Frontier Developments\Elite Dangerous'
    screenshotDir = f'{userprofile}\Pictures\Frontier Developments\Elite Dangerous'
    saveDir = f'{userprofile}\EliteResized'
    windowClosed = 0
    fileType = 'png'
    
    
    def __init__(self, *args, **kwargs):
        super(MainWindowUIClass, self).__init__(*args, **kwargs)
        self.threadpool = QThreadPool()
        self.fill_thread = None
        Settings.init()

        
    def setupUI(self, MW):
        super().setupUI(MW)


    def progressPrint( self, msg ):
        self.textBrowser.append( msg )

        self.textBrowser.verticalScrollBar().setValue(
            self.textBrowser.verticalScrollBar().maximum()
        )

        
    def browseSlot(self, lineType):
        if lineType == "journal":
            directory = QtWidgets.QFileDialog.getExistingDirectory(
                        None,
                        "Select Elite Dangerous Journal directory",
                        self.journalDir)
            self.lineEdit.setText(directory)
        elif lineType == "screenshots":
            directory = QtWidgets.QFileDialog.getExistingDirectory(
                        None,
                        "Select Elite Dangerous Screenshots directory",
                        self.screenshotDir)
            self.lineEdit_2.setText(directory)
        elif lineType == "save":
            directory = QtWidgets.QFileDialog.getExistingDirectory(
                        None,
                        "Select Elite Resized save directory",
                        self.saveDir)
            self.lineEdit_3.setText(directory)

      
    def returnPressedSlot(self, lineType):
        if lineType == "journal":
            directory =  self.lineEdit.text()
            self.journalDir = self.setDirectory(directory)
            self.lineEdit.setText(self.journalDir)
        elif lineType == "screenshots":
            directory =  self.lineEdit_2.text()
            self.screenshotDir = self.setDirectory(directory)
            self.lineEdit_2.setText(self.screenshotDir)
        elif lineType == "save":
            directory =  self.lineEdit_3.text()
            self.saveDir = self.setDirectory(directory)
            self.lineEdit_3.setText(self.saveDir)


    def setAllDirs(self):
        self.setDirectory(self.journalDir)
        self.setDirectory(self.screenshotDir)
        self.setDirectory(self.saveDir)


    def convert(self):
        self.setAllDirs()
        worker = Worker.Worker(self.processScreenshots)
        worker.signals.result.connect(self.progressPrint)
        worker.signals.finished.connect(lambda: self.progressPrint('Conversion complete'))

        self.threadpool.start(worker)

    def onClicked(self, imageType):
        self.fileType = imageType

    def processScreenshots(self):        
        i = 0
        data = self.generate_screenshot_dictionary()
        lengthOfDataDict = len(data)
        if lengthOfDataDict < 1:
            self.progressPrint(f'No screenshots found')
            return
        Settings.percentPerItem = 100 / lengthOfDataDict

        for item in data:
            if self.windowClosed == 1:
                #ie tidy up and go home
                self.endCThread()
                break
            if 'timestamp' in item:
                originalfile = item['Filename'].replace("\\ED_Pictures", self.screenshotDir)
                if (os.path.isfile(originalfile)):
                    img = Image.open(originalfile)
                    newfilename =  f'{self.build_file_name(item)}.{self.fileType}'
                    savefilefull = f'{self.saveDir}\\{newfilename}'
                    time.sleep(0.02)

                    if not (os.path.isfile(savefilefull)):
                        if self.fileType == "jpeg":
                            img.save(savefilefull, self.fileType, dpi=(300, 300))
                        elif self.fileType == "webp":
                            img.save(savefilefull, self.fileType, dpi=(300, 300))
                        elif self.fileType == "png":
                            img.save(savefilefull, self.fileType, dpi=(300, 300), compress_level=4)
                        i += 1
                        self.progressPrint(f'{newfilename} saved. {str(i)} files saved so far')
                    else:
                        self.progressPrint(f'{newfilename} already exists')
                else:
                    time.sleep(0.01)
                    self.progressPrint(f'{originalfile} not found')

            self.fill_thread = CThread.CThread(Settings.completed)
            self.fill_thread.valueChanged.connect(self.progressBar.setValue)
            self.fill_thread.start()

        self.endCThread()      
        self.progressPrint(f'Number of entries converted: {str(i)}')
        

    def endCThread(self):
        if self.fill_thread != None:
                self.fill_thread.disconnect() # event unbind
                self.fill_thread.stop_fill = True
                self.fill_thread.wait()
                self.fill_thread.quit()


    # convert invalid characters for Windows filenames 
    def convert_disallowed_chars(self, text):
        for ch in ['<', '>', ':', '"', '/', '\\', '|', '?']:
            if ch in text:
                text = text.replace(ch,"_")

        text = text.replace('*', '_Star')
        return text


    # create file name from available elements in subdictionary
    def build_file_name(self, item):
        filename = []
        filename.append(self.convert_disallowed_chars(item['timestamp']))
        if 'System' in item:
            filename.append(self.convert_disallowed_chars(item['System']))
        if 'Body' in item:
            filename.append(self.convert_disallowed_chars(item['Body']))
        return '_'.join(filename)


    # return a dictionary containing all Screenshot events
    def generate_screenshot_dictionary(self):
        data = []
        for filename in os.listdir(self.journalDir):
            if filename.endswith(".log"):
                filepath = f'{self.journalDir}\\{filename}'
                for line in open(filepath, 'r', errors='replace'):
                    currentline = orjson.loads(line)
                    if currentline['event'] == 'Screenshot':
                        self.progressPrint(f'Screenshot found in {filename}')
                        time.sleep(0.01) # need to add these in or Windows has a fit
                        data.append(currentline)
            else:
                continue

        return data


    def setDirectory( self, directory ):
        if not os.path.exists(directory):
            os.makedirs(directory)
        return directory

    
    def onLastClosed(self):
        self.windowClosed = 1 #var to inform workers window has been closed
        sys.exit(0)


def exception_hook(exctype, value, traceback):
    print(exctype, value, traceback)
    sys._excepthook(exctype, value, traceback) 
    sys.exit(1)


# main function
def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MainWindowUIClass()
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.setQuitOnLastWindowClosed(False)
    app.lastWindowClosed.connect(ui.onLastClosed)
    sys._excepthook = sys.excepthook 
    sys.excepthook = exception_hook 
    sys.exit(app.exec_())

# run the main function
if __name__ == "__main__":
    main()
