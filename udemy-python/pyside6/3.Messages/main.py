from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox, QGridLayout, QPushButton

class MyMessageBoxApp(QMainWindow):
    def __init__(self):
        super().__init__()
    
        MyCentralWidget = QWidget()
        MyLayout = QGridLayout()
        MyCentralWidget.setLayout(MyLayout)

        self.setCentralWidget(MyCentralWidget)

        CButton = QPushButton("Critical")
        IButton = QPushButton("Information")
        AButton = QPushButton("About")
        WButton = QPushButton("Warning")

        MyLayout.addWidget(CButton, 0, 0)
        MyLayout.addWidget(IButton, 0, 1)
        MyLayout.addWidget(WButton, 1, 0)
        MyLayout.addWidget(AButton, 1, 1)

        CButton.clicked.connect(self.critical)
        IButton.clicked.connect(self.information)
        AButton.clicked.connect(self.about)
        WButton.clicked.connect(self.warning)




    def critical(self):
        ret = QMessageBox().critical(self, "Warning", "This is a warning", QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel, QMessageBox.StandardButton.Ok)
        if ret == QMessageBox.StandardButton.Ok:
            print("Ok")
        else:
            print("Cancel")

    def information(self):
        ret = QMessageBox().information(self, "Warning", "This is a warning", QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel, QMessageBox.StandardButton.Ok)
        if ret == QMessageBox.StandardButton.Ok:
            print("Ok")
        else:
            print("Cancel")
    def about(self):
        ret = QMessageBox().about(self, "Warning", "This is a warning")
        if ret == QMessageBox.StandardButton.Ok:
            print("Ok")
        else:
            print("Cancel")
        
    def warning(self):
        ret = QMessageBox().warning(self, "Warning", "This is a warning", QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel, QMessageBox.StandardButton.Ok)
        if ret == QMessageBox.StandardButton.Ok:
            print("Ok")
        else:
            print("Cancel")


app = QApplication()
widget = MyMessageBoxApp()
widget.show()
app.exec()