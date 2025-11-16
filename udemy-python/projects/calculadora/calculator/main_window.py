from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel
import sys 

class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        self.central_widget = QWidget()

        self.setCentralWidget(self.central_widget)

        self.v_layout = QVBoxLayout()
        self.central_widget.setLayout(self.v_layout)
        



if __name__ == "__main__":
    ...