import sys
import traceback as tb
from PyQt5.QtWidgets import QApplication

from classes.cl_const import Const
from classes.db_session import ConnectDb
from classes.qt__classes import LogWriter
from widgets_journal.j_mainwindow import MWindow
from widgets_journal.j_syslogin import LoginDialog


def except_hook(cls, exception, traceback):
    global flog
    flog.to_log(f"""{exception} | \n{tb.format_tb(traceback)[0]}""")
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    if Const.TEST_MODE:
        print('app = QApplication(sys.argv)')
    app = QApplication(sys.argv)
    if Const.TEST_MODE:
        print('flog = LogWriter()')
    flog = LogWriter()
    if Const.TEST_MODE:
        print('sys.excepthook = except_hook')
    sys.excepthook = except_hook
    if Const.TEST_MODE:
        print("flog.to_log('Старт программы')")
    flog.to_log('Старт программы')
    if Const.TEST_MODE:
        print("ConnectDb('settings.ini').get_con()")
    con = ConnectDb('settings.ini').get_con()
    if Const.TEST_MODE:
        print('login_user = LoginDialog(con)')
    login_user = LoginDialog(con)
    if Const.TEST_MODE:
        print('app.exec()')
    app.exec()
    if Const.TEST_MODE:
        print('if login_user.passwd_ok:')
    if login_user.passwd_ok:
        # print(login_user.loggedUser['id'])
        flog.to_log(f"""{login_user.loggedUser['id']}, {login_user.loggedUser['name'].strip()}, Успешный вход""")
        if Const.TEST_MODE:
            print("wnd = MWindow(con, login_user.loggedUser['id'])")
        wnd = MWindow(con, login_user.loggedUser['id'])
        if Const.TEST_MODE:
            print('wnd.showMaximized()')
        wnd.showMaximized()
        if Const.TEST_MODE:
            print('sys.exit(app.exec())')
        sys.exit(app.exec())
