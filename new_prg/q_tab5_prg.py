import sys
import traceback as tb
import datetime

from PyQt5 import QtWidgets, QtCore, QtSql, QtGui
from PyQt5.QtCore import QTimer, QModelIndex, QEvent, pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QApplication, QAbstractItemView, QPushButton, QLineEdit, QLabel, QCheckBox, \
    QWidget, QFrame, QInputDialog, QTextEdit, QSizePolicy, QPlainTextEdit, QComboBox

from classes.bb_converts import date_us_ru, date_ru_us
from classes.cl_logwriter import LogWriter
from classes.cl_statistics import Statistics
from classes.db_session import ConnectDb
from classes.t_journal import TJournalModel
from classes.cl_const import Const
from classes.t_tables import TRasp, TJournals, TUsers, TGroups, TGroupTable
from forms_journ.t_tab5 import Ui_tab5Form
from new_prg.db_connect import QUsers


def except_hook(cls, exception, traceback):
    global flog
    flog.to_log(f"""{exception} | \n{tb.format_tb(traceback)[0]}""")
    sys.__excepthook__(cls, exception, traceback)


class QT5Window(QWidget, Ui_tab5Form):  # tab5 формы
    def __init__(self, user_id):
        self.logfile = LogWriter()
        if Const.TEST_MODE:
            self.logfile.to_log(f"""======>  Tab5. Start __init__""")
            print("======>  Tab5. Start __init__")
        super(QT5Window, self).__init__()
        self.setupUi(self)
        self.initUi(user_id)

    def initUi(self, user_id=None):
        self.user_id = user_id
        self.teach = QUsers(params=(Const.ACC_PREPOD,), dsort=('u.name',))

        if Const.TEST_MODE:
            self.logfile.to_log(f"""======>  Tab5. Finish __init__""")
            print("======>  Tab5. Finish __init__")

    def showEvent(self, a0: QtGui.QShowEvent) -> None:
        self.teachf_refresh_sql()

    def teachf_refresh_sql(self):
        self.teach_spisok.clear()
        if self.teach.refresh_select():
            self.teach.first()
            idx = -1
            while self.teach.isValid():
                self.teach_spisok.addItem(f"{self.teach.value(0):4} : {self.teach.value(1)}")
                if self.user_id == self.teach.value(0):
                    idx = self.teach.at()
                self.teach.next()
            self.teach_spisok.setCurrentIndex(idx)


if __name__ == '__main__':
    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    flog = LogWriter()
    conn_str = 'Driver=SQL Server;Server=172.16.1.12,1433;Database=Journal4303;UID=sa;PWD=Prestige2011!;'
    db =  QtSql.QSqlDatabase.addDatabase('QODBC')
    db.setDatabaseName(conn_str)
    if db.open():
        if Const.TEST_MODE:
            print('Connect: Ok')
        wnd = QT5Window(15)
        wnd.showMaximized()
    sys.exit(app.exec())
