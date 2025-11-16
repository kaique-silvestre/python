from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QVBoxLayout, QPushButton


# Criação da classe "MyInterface" que é (herda) uma "QMainWindow" 
class MyInterface(QMainWindow):
    # Chamamos o construtor da classe "QMainWindow"
    def __init__(self):
        super().__init__()

        # Criamos um Widget
        MyCentralWidget = QWidget()
        # Criamos um Layout
        MyVLayout = QVBoxLayout()
        # Definimos que o Widget "MyCentralWidget" terá o Layout "MyLayout"
        MyCentralWidget.setLayout(MyVLayout)

        # Definimos que o Central Widget do "QMainWindow" será o objeto "MyCentralWidget" que é da Classe "Widget"
        self.setCentralWidget(MyCentralWidget)  

        # Criamos um objeto botão
        button01 = QPushButton("Click Me!")

        # Adicionamos o Objeto botão no Layout
        MyVLayout.addWidget(button01)

app = QApplication()
wi = MyInterface()
wi.show()

app.exec()
