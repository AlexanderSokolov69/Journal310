import sys

from PyQt6 import QtCore
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QSplashScreen, QLabel

if __name__ == '__main__':
    app = QApplication(sys.argv)
    spl = QSplashScreen(QPixmap('Splash/Splash01-02.PNG'))
    spl.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)
    lbl = QLabel('Привет, мир!')
    spl.show()

    QtCore.QThread.sleep(5)
    spl.finish(lbl)
    lbl.show()


    sys.exit(app.exec())