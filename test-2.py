import sys
import math
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QFrame
from PyQt5.QtGui import QPixmap, QPainter, QColor, QPen, QImage, QCursor
from PyQt5.QtCore import Qt, QPoint, QTimer, QEvent


def except_hook(cls, exception, traceback ):
    sys.__excepthook__(cls, exception, traceback)


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setFixedSize(600, 400)
        self.setWindowTitle('Цветной Мандельброт')
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
        self.image = QLabel(self)
        self.image.move(0, 0)
        self.image.resize(self.width(), self.height())
        self.images = [{'params': (-2.0, -1.0, 1.0, 1.0), 'image': None}]
        self.images[-1]['image'] = QImage(self.width(), self.height(), QImage.Format_ARGB32_Premultiplied)
        self.mand_timer = QTimer(self)
        self.mand_timer.setInterval(10)
        self.mand_timer.timeout.connect(self.build_mand_line)
        # создаём рамку
        self.frame = QFrame(self)
        self.frame.setGeometry(0, 0, 90, 60)
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setLineWidth(3)
        self.frame.setStyleSheet("color: blue;")
        self.installEventFilter(self)
        self.mouse_pos = None

        # Запускаем построитель
        self.start_build_mand()

    def eventFilter(self, object, event):
        if event.type() == QEvent.Enter:
            self.frame.setCursor(QCursor(Qt.OpenHandCursor))
        elif event.type() == QEvent.Leave:
            self.frame.setCursor(QCursor(Qt.ArrowCursor))
        elif event.type() == QEvent.MouseButtonPress:
            if event.buttons() == Qt.LeftButton:
                self.frame.setCursor(QCursor(Qt.ClosedHandCursor))
                self.mouse_pos = event.windowPos()
        elif event.type() == QEvent.MouseButtonRelease:
            self.frame.setCursor(QCursor(Qt.OpenHandCursor))
        elif event.type() == QEvent.MouseMove:
            if event.buttons() == Qt.LeftButton:
                # Двигаем рамку
                move_vector = event.windowPos() - self.mouse_pos
                new_pos = self.frame.pos() + move_vector
                self.frame.move(int(new_pos.x()), int(new_pos.y()))
                self.mouse_pos = event.windowPos()
        elif event.type() == QEvent.MouseButtonDblClick:
            if event.buttons() == Qt.LeftButton:
                old_xa, old_ya, old_xb, old_yb = self.images[-1]['params']
                new_xa = old_xa + self.frame.x() * (old_xb - old_xa) / self.width()
                new_ya = old_ya + self.frame.y() * (old_yb - old_ya) / self.height()
                new_xb = new_xa + self.frame.width() * (old_xb - old_xa) / self.width()
                new_yb = new_ya + self.frame.height() * (old_yb - old_ya) / self.height()
                self.images.append({'params': (new_xa, new_ya, new_xb, new_yb), 'images': None})
                self.images[-1]['image'] = QImage(self.width(), self.height(), QImage.Format_ARGB32_Premultiplied)
                self.start_build_mand()
            else:
                if len(self.images) > 1:
                    self.images.pop()
                    self.image.setPixmap(QPixmap.fromImage(self.images[-1]['image']))

        return super().eventFilter(object, event)

    def start_build_mand(self):
        # Прячем рамку
        self.frame.hide()
        self.frame.move(0, 0)
        # Генератор отрисовки
        self.image_gerator = self.mand_color()
        self.mand_timer.start()

    def build_mand_line(self):
        try:
            next(self.image_gerator)
            self.image.setPixmap(QPixmap.fromImage(self.images[-1]['image']))
        except StopIteration:
            self.mand_timer.stop()
            # Подвинуть рамку в начало

            # Показать рамку
            self.frame.show()

    # def paintEvent(self, a0: QPaintEvent) -> None:
    #     self.qp.begin(self)
    #     self.mand_color()
    #     self.qp.end()

    def mand_color(self):
        painter = QPainter()
        painter.begin(self.images[-1]['image'])
        xa, ya, xb, yb = self.images[-1]['params']
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
                painter.setPen(pen)
                painter.drawPoint(QPoint(x, y))
            yield True
        painter.end()

if __name__ == '__main__':
    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    wnd = Window()
    wnd.show()
    sys.exit(app.exec())