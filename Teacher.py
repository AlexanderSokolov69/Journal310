import sys
import traceback as tb
from PyQt5.QtWidgets import QApplication
from classes.db_session import connectdb
from classes.qt__classes import LogWriter
from widgets_journal.j_syslogin import LoginDialog
from widgets_teacher.t_mainwindow import MWindow


def except_hook(cls, exception, traceback):
    global flog
    flog.to_log(f"""{exception} | \n{tb.format_tb(traceback)[0]}""")
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    flog = LogWriter(fname='teachLog.txt')
    sys.excepthook = except_hook
    flog.to_log('Старт программы')
    con = connectdb()
    login_user = LoginDialog(con)
    app.exec()
    if login_user.passwd_ok:
        flog.to_log(f"""{login_user.loggedUser['id']}, {login_user.loggedUser['name']}, Успешный вход""")
        wnd = MWindow(con, login_user.loggedUser['id'])
        wnd.showMaximized()
        sys.exit(app.exec())
