import sys
import math
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QPushButton, QInputDialog, QSlider
from PyQt5.QtGui import QPixmap, QPainter, QColor, QBrush, QPen, QPaintEvent
from PyQt5.QtCore import Qt, QPoint


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.initUI()

    def initUI(self):
        self.setFixedSize(400, 300)
        self.setWindowTitle('Чёрно-белый Мандельброт')
        self.qp = QPainter(self)
        self.max_iteration = 255
        self.palette = [
            (
                int(255 * math.sin(i / 30.0 + 0.5) ** 2),
                int(255 * math.sin(i / 30.0 + 1.0) ** 2),
                int(255 * math.sin(i / 30.0 + 1.7) ** 2)
            ) for i in range(self.max_iteration - 1)
        ]
        self.palette.append((0, 0, 0))

    def paintEvent(self, a0: QPaintEvent) -> None:
        self.qp.begin(self)
        self.mand_color()
        self.qp.end()

    def mand_bw(self):
        xa, ya, xb, yb = [-2.0, -1.0, 1.0, 1.0]
        img_x, img_y = self.width(), self.height()
        pen = QPen(QColor(0, 0, 0), 1)
        self.qp.setPen(pen)
        for y in range(img_y):
            for x in range(img_x):
                zy = y * (yb - ya) / img_y + ya
                zx = x * (xb - xa) / img_x + xa
                c, z = zx + zy * 1j, 0
                for cnt in range(self.max_iteration):
                    if abs(z) > 2.0:
                        break
                    z = z * z + c
                else:
                    self.qp.drawPoint(QPoint(x, y))

    def mand_gray(self):
        xa, ya, xb, yb = [-2.0, -1.0, 1.0, 1.0]
        img_x, img_y = self.width(), self.height()
        for y in range(img_y):
            for x in range(img_x):
                zy = y * (yb - ya) / img_y + ya
                zx = x * (xb - xa) / img_x + xa
                c, z = zx + zy * 1j, 0
                for cnt in range(self.max_iteration):
                    if abs(z) > 2.0:
                        pen = QPen(QColor(cnt, cnt, cnt), 1)
                        break
                    z = z * z + c
                else:
                    pen = QPen(QColor(0, 0, 0), 1)
                self.qp.setPen(pen)
                self.qp.drawPoint(QPoint(x, y))

    def mand_color(self):
        xa, ya, xb, yb = [-2.0, -1.0, 1.0, 1.0]
        img_x, img_y = self.width(), self.height()
        for y in range(img_y):
            for x in range(img_x):
                zy = y * (yb - ya) / img_y + ya
                zx = x * (xb - xa) / img_x + xa
                c, z = zx + zy * 1j, 0
                for cnt in range(self.max_iteration):
                    if abs(z) > 2.0:
                        break
                    z = z * z + c
                pen = QPen(QColor(*self.palette[cnt]), 1)
                self.qp.setPen(pen)
                self.qp.drawPoint(QPoint(x, y))



if __name__ == '__main__':
    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    wnd = Window()
    wnd.show()
    sys.exit(app.exec())