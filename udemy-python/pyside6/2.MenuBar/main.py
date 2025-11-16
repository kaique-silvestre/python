from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QTextEdit


class Menu(QMainWindow):
    def __init__(self):
        super().__init__()

        # Criando uma Menu Bar
        menuBar = self.menuBar()

        # Criando os Menus da Menu Bar
        fileMenu = menuBar.addMenu("File")
        editMenu = menuBar.addMenu("Edit")
        helpFile = menuBar.addMenu("Help")

        # Criando um submenu
        aboutMenu = helpFile.addMenu("About")

        # Criando ações dentro dos menus 
        aboutAction = aboutMenu.addAction("?")
        exitAction = fileMenu.addAction("Exit")

        # Criando signals que se coenctam as ações e fazem algo
        aboutAction.triggered.connect(lambda: print("Text"))
        exitAction.triggered.connect(self.close)
    

app = QApplication()
wi = Menu()
wi.show()
app.exec()