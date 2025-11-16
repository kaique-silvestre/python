from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel
import sys 
from main_window import MainWindow

if __name__ == "__main__":

    app = QApplication(sys.argv)


    window = MainWindow()
    label1 = QLabel("Texto")
    window.v_layout.addWidget(label1)
    window.setWindowTitle("Calculator" )




    window.show()
    app.exec()