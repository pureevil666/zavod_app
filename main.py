from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
import sys
import calculation

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 800


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("Завод")
        self.setGeometry(650, 150, WINDOW_WIDTH, WINDOW_HEIGHT)
        self.setStyleSheet("Window {background-color: #191919;}")

        self.input_area = QtWidgets.QPlainTextEdit(self)
        self.input_area.setFixedWidth(WINDOW_WIDTH)
        self.input_area.setFixedHeight(WINDOW_HEIGHT - 70)
        self.input_area.setFont(QFont('Times', 10))
        self.input_area.setStyleSheet("QPlainTextEdit { color: White; background-color: #191919; "
                                      "padding: 5px 0px 5px 10px;}")

        self.button_width = WINDOW_WIDTH
        self.button_height = 70
        self.button = QtWidgets.QPushButton(self)
        self.button.setText("Посчитать")
        self.button.setFixedWidth(self.button_width)
        self.button.setFixedHeight(self.button_height)
        self.button.setStyleSheet("QPushButton {font-size: 25px; font-weight: bold; "
                                  "color: White; background-color: #404040;}")
        self.button.move(WINDOW_WIDTH - self.button_width, WINDOW_HEIGHT - self.button_height)
        self.button.clicked.connect(self.press_button)

    def press_button(self):
        calculation.give_data(window.input_area.toPlainText())
        self.show_result()

    def show_result(self):
        self.result = Result()
        self.result.show()

    def disable_window(self, value):
        self.input_area.setReadOnly(value)
        self.button.setDisabled(value)


class Result(QWidget):
    def __init__(self):
        super(Result, self).__init__()

        window.disable_window(True)
        self.result_width = round(WINDOW_WIDTH * 0.7)
        self.result_height = round(WINDOW_HEIGHT * 0.4)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setMinimumWidth(self.result_width)
        self.move(WINDOW_WIDTH + round(self.result_width * 0.35), WINDOW_HEIGHT - round(self.result_height * 1.4))
        self.setMinimumHeight(self.result_height)

        self.label = QtWidgets.QLabel(self)
        self.label.setText('Результат')
        self.label.setMinimumWidth(self.result_width - 5)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.move(0, 10)
        self.label.setFont(QFont('Arial', 16))

        self.result_label = QtWidgets.QLabel(self)
        self.result_label.setText(calculation.label)
        self.result_label.setMinimumWidth(self.result_width - 5)
        self.result_label.setMargin(120)
        self.result_label.move(0, -75)
        self.result_label.setFont(QFont('Arial', 12))

        self.overall_score_label = QtWidgets.QLabel(self)
        self.overall_score_label.setText(f'Общее: {calculation.overall_score}')
        self.overall_score_label.setAlignment(Qt.AlignCenter)
        self.overall_score_label.setMinimumWidth(self.result_width - 5)
        self.overall_score_label.move(0, self.result_height - 75)
        self.overall_score_label.setFont(QFont('Arial', 16))

        self.close_button_width = self.result_width - 10
        self.close_button_height = 40
        self.close_button = QtWidgets.QPushButton(self)
        self.close_button.setText("Закрыть")
        self.close_button.clicked.connect(self.close_result)
        self.close_button.setFixedWidth(self.close_button_width)
        self.close_button.setFixedHeight(self.close_button_height)
        self.close_button.setFont(QFont('Arial', 12))
        self.close_button.move(self.result_width - self.close_button_width - 5,
                               self.result_height - self.close_button_height - 5)

    def close_result(self):
        global window
        self.close()
        window.disable_window(False)


def application():
    global window
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()
