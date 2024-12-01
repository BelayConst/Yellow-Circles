from PyQt6 import uic, QtWidgets, QtCore
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtWidgets import QPushButton
from PyQt6.QtGui import QPainter, QColor, QPolygon
import sys
import random


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.flag = False
        uic.loadUi('UI.ui', self)


        self.drawButton.clicked.connect(self.draw)
        self.coords = []

    def draw(self):
        self.figure = 'circle'
        self.size = random.randint(10, 100)
        self.color = (255, 255, 0)  # 'yellow'
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            qp.setPen(QColor(*self.color))
            qp.setBrush(QColor(*self.color))
            self.x, self.y = random.randint(10, 540), random.randint(10, 380)
            if self.figure == 'circle':
                qp.drawEllipse(self.x, self.y, self.size, self.size)
            qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
