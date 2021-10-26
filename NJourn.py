import os
import sys

from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtSql import QSqlQuery
from PyQt5.QtWidgets import QApplication, QSplashScreen

from classes.cl_const import Const
from classes.cl_logwriter import LogWriter
from new_prg.q_tab5_prg import QT5Window
from widgets_prg.t_db_session import QtConnectDb


def except_hook(cls, exception, traceback):
    global flog
    flog.to_log(f"""{exception} | \n{tb.format_tb(traceback)[0]}""")
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    flog = LogWriter()

    spl = QSplashScreen(QPixmap('Splash/Splash01-02.PNG'))
    spl.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)
    spl.show()

    if QtConnectDb('settings.ini').get_con():
        if Const.TEST_MODE:
            print('Connect: Ok')
        qsql = QSqlQuery()
        qsql.exec(f"select id from users where winlogin = '{os.getlogin()}'")
        qsql.first()
        wnd = QT5Window(int(qsql.record().value(0)))
        spl.finish(wnd)
        wnd.showMaximized()
    sys.exit(app.exec())
