from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 800


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("Завод")
        self.setGeometry(650, 150, WINDOW_WIDTH, WINDOW_HEIGHT)

        self.input_area = QtWidgets.QPlainTextEdit(self)
        self.input_area.setFixedWidth(WINDOW_WIDTH)
        self.input_area.setFixedHeight(WINDOW_HEIGHT)
        self.input_area.setStyleSheet("QPlainTextEdit { color: White; background-color: #191919;}")

        self.button_width = WINDOW_WIDTH - 30
        self.button_height = 50
        self.button = QtWidgets.QPushButton(self)
        self.button.setText("Посчитать")
        self.button.setFixedWidth(self.button_width)
        self.button.setFixedHeight(self.button_height)
        self.button.setStyleSheet("QPushButton {font-size: 25px; font-weight: bold; "
                                  "color: White; background-color: #404040;}")
        self.button.move(WINDOW_WIDTH - self.button_width - 15, WINDOW_HEIGHT - self.button_height - 15)
        self.button.clicked.connect(self.press_button)

    def press_button(self):
        input_text = self.input_area.toPlainText()

        print(input_text)


def application():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()
