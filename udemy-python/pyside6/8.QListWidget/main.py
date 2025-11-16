from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QListWidget, QAbstractItemView


class MyList(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("List")

        # Self explicita que o item faz pafrte da classe
        MyList = QListWidget(self)
        
        MyList.addItem("One")
        
        MyList.addItems(["Two", "Three"])

        self.setCentralWidget(MyList)

app = QApplication()
wi = MyList()
wi.show()
app.exec()

