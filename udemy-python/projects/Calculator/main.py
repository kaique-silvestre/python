from PySide6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QGridLayout, QVBoxLayout



class MainCalculator(QWidget):
    def __init__(self):
        super().__init__()

        self.string = ""

        # Creating Objects

        BUTTONS_LIST = \
            [
            "7", "8", "9", "/", 
            "4", "5", "6", "-" ,
            "1", "2", "3", "+",
            "0", ".", "=", "*"
            ]
        
        self.calc_view = QLineEdit()
        

        # Layout
        app_layout = QVBoxLayout()
        self.setLayout(app_layout)
        buttons_grid = QGridLayout()

        # Adding to the layout
        app_layout.addWidget(self.calc_view) 

        app_layout.addLayout(buttons_grid)

        column = row = 0
        for item in BUTTONS_LIST:
            button = QPushButton(item)
            button.clicked.connect(self.button_clicked)
            buttons_grid.addWidget(button, row, column)
            if column < 3:
                column += 1
            else:
                row += 1
                column = 0
    def button_clicked(self):
        button = self.sender()
        print(button)
        self.string += button.text()
        self.calc_view.setText(self.string)

app = QApplication()
widget = MainCalculator()
widget.show()
app.exec()

        
        
