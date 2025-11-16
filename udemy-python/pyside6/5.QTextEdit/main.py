from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QTextEdit, QVBoxLayout, QMessageBox
import json
import pathlib


class NotepadApplication(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("notepad")


        # Creating a Central Widget and VLayout 
        CentralWidget = QWidget()
        vLayout = QVBoxLayout()

        # Setting CW and Layout 
        self.setCentralWidget(CentralWidget)
        CentralWidget.setLayout(vLayout)

        # Creating the notepad
        self.TextEdit = QTextEdit()

        self.TextEdit.setPlaceholderText("Your Text Here")

        # Creating menubar 
        menubar = self.menuBar()

        # File 
        file = menubar.addMenu("File")

        # File Actions
        savefile = file.addAction("Save File")
        exitfile = file.addAction("Exit")

        # edit menu
        edit = menubar.addMenu("Edit")

        # edit menu actions
        copy = edit.addAction("Copy")
        paste = edit.addAction("Paste")
        delete = edit.addAction("Delete")




        #slots
        # edit 
        copy.triggered.connect(self.TextEdit.copy)
        paste.triggered.connect(self.TextEdit.paste)
        delete.triggered.connect(self.TextEdit.clear)

        # file
        savefile.triggered.connect(self.savefile)
        exitfile.triggered.connect(self.exitmessage) 

        # adding to the layout 
        vLayout.addWidget(self.TextEdit)

    def savefile(self):
        path = pathlib.Path(__file__).parent / "text.txt"
        with open(path, 'w+', encoding='utf8') as file:
            note = self.TextEdit.toPlainText()
            file.writelines(note)
    
    def exitmessage(self):
        qsb = QMessageBox.StandardButton
        warning = QMessageBox.warning \
        (
            self, "Exit without Saving", "Exiting the program without saving your files will make you lost all your work, are you sure?", qsb.Ok | qsb.Cancel, qsb.Cancel 
        )
        if warning == qsb.Ok:
            exit()


app = QApplication()
widget = NotepadApplication()
widget.show()
app.exec()