import sys
from PyQt5.QtWidgets import QWidget,QApplication,QVBoxLayout,QLabel
from PyQt5.QtCore import Qt

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Main Window")
#set title of window
        self.setGeometry(500,300,500,300)
#setGeometry (alignLeft, alignTop, width, height)
        
        self.mainLayout = QVBoxLayout(self)
#create mainLayout with vertical box means all the wiidgets addes in the mainLayout isin vertical
        self.setLayout(self.mainLayout)
#here mainWindow Layout in the window
        
        self.LabelUI()
#function call in the MainWindow constructor for add the label in the mainWindow layout
        
    def LabelUI(self):
#function for creating the label and set in the main Layout
        
        self.label = QLabel("Hello Core2Web")
#here create the label with parameter "hello core2web"
        self.mainLayout.addWidget(self.label,0,Qt.AlignmentFlag.AlignCenter)
#set the label in the main Layout Window
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_Window = MainWindow()
    main_Window.show()
    sys.exit(app.exec_())