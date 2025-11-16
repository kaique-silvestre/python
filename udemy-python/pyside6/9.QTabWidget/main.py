from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTabWidget, QMainWindow, QPushButton

class Tabs(QWidget):
    def __init__(self):
        super().__init__()

        tab = QTabWidget(self)

        # Widget 01
        wi01 = QWidget()
        b01 = QPushButton("Click Me")
        vlay01 = QVBoxLayout()
        vlay01.addWidget(b01)
        wi01.setLayout(vlay01)

        # Widget 02
        wi02 = QWidget()
        b02 = QPushButton("Click Me 2")
        vlay02 = QVBoxLayout()
        vlay02.addWidget(b02)
        wi02.setLayout(vlay02)

        # Addinf Widgets to TAB widget
        tab.addTab(wi01, "First tab")
        tab.addTab(wi02, "Second tab")

        # Addinf tab Widget to the Widget
        total_layout = QVBoxLayout()
        total_layout.addWidget(tab)
        self.setLayout(total_layout)

app = QApplication()
wi = Tabs()
wi.show()
app.exec()