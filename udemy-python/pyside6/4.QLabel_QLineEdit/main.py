from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout


class MyLine(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Lines and Labels")

        MyCentralWidget = QWidget()
        v_layout = QVBoxLayout()
        MyCentralWidget.setLayout(v_layout)
        self.setCentralWidget(MyCentralWidget)

        h_layout = QHBoxLayout()
        label = QLabel("Fullname: ")
        self.edit = QLineEdit()

        h_layout.addWidget(label)
        h_layout.addWidget(self.edit)

        v_layout.addLayout(h_layout)
        
        bu = QPushButton("grab me!")
        
        v_layout.addWidget(bu)

        self.la2 = QLabel("text")

        v_layout.addWidget(self.la2)

        bu.clicked.connect(self.teste)
    
    def teste(self):
        self.la2.setText(self.edit.text())



app = QApplication()
myline = MyLine()
myline.show()
app.exec()
