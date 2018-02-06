import sys
from PyQt4 import QtCore, QtGui, uic

form_class = uic.loadUiType("Project.ui")[0]

class MyWindowClass(QtGui.QMainWindow, form_class):
    def __init__(self, parent = None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        #
        self.Play.clicked.connect(self.button_clicked)
        #
        self.media_obj = Phonon.MediaObject(self)
        self.actionOpen.triggered.connect(self.open)

    def button_clicked(self):
        if(self.Play.text() == "Play"):
            self.Play.setText("Pause")
        else:
            self.Play.setText("Play")

    def open(self):
        dialog = QFileDialog()
        dialog.setViewMode(QFileDialog.Detail)
        filename = dialog.getOpenFileName(self,
             'Open audio file', '/home',
             "Audio Files (*.mp3 *.wav *.ogg)")[0]
        self.audio_output = Phonon.AudioOutput(Phonon.MusicCategory, self)
        Phonon.createPath(self.media_obj, self.audio_output)
        self.media_obj.setCurrentSource(Phonon.MediaSource(filename))
        self.media_obj.tick.connect(self.time_change)
        self.media_obj.totalTimeChanged.connect(self.total_time_change)
        self.media_obj.play()
        self.button.setEnabled(True)
        self.button.setText("Pause")
        self.horizontalSlider.setEnabled(True)

app = QtGui.QApplication(sys.argv)
myWindow = MyWindowClass()
myWindow.show()
app.exec_()
