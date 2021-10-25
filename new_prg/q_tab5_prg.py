import sys
import traceback as tb
import datetime

from PyQt5 import QtWidgets, QtCore, QtSql, QtGui
from PyQt5.QtCore import QTimer, QModelIndex, QEvent, pyqtSignal
from PyQt5.QtSql import QSqlQueryModel
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
from new_prg.db_connect import QUsers, QGroups, QJournals


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
        self.in_user_id = None
        self.teach = QUsers(params=(Const.ACC_PREPOD, ), dsort=('u.name', ))
        self.groups = QGroups(dsort=('g.name',))
        self.groupBox.setDisabled(True)
        self.journ = QJournals(params=(-1, ), dsort=('j.date', 'j.tstart'))
        self.tableView.setDisabled(True)

        self.teach_spisok.currentIndexChanged.connect(self.groupsf_refresh_sql)
        self.groupBox.currentIndexChanged.connect(self.journf_refresh_sql)
        if Const.TEST_MODE:
            self.logfile.to_log(f"""======>  Tab5. Finish __init__""")
            print("======>  Tab5. Finish __init__")

    def showEvent(self, a0: QtGui.QShowEvent) -> None:
        self.teachf_refresh_sql()

    def groupsf_refresh_sql(self):
        if self.groupBox.isEnabled():
            self.in_user_id = int(self.teach_spisok.currentText().split()[0])
            self.groups.set_param_str((self.in_user_id, ))
            self.groupBox.clear()
            if self.groups.refresh_select():
                self.groups.first()
                idx = -1
                while self.groups.isValid():
                    self.groupBox.addItem(f"{self.groups.value(Const.GRP_ID):4} : "
                                          f"{self.groups.value(Const.GRP_NAME)} : "
                                          f"{self.groups.value(Const.GRP_COMMENT)}")
                    self.groups.next()
                self.groupBox.setCurrentIndex(0)

    def teachf_refresh_sql(self):
        self.teach_spisok.clear()
        if self.teach.refresh_select():
            self.groupBox.setDisabled(True)
            self.teach.first()
            idx = -1
            while self.teach.isValid():
                self.teach_spisok.addItem(f"{self.teach.value(Const.USR_ID):4} : {self.teach.value(Const.USR_NAME)}")
                if self.user_id == self.teach.value(Const.USR_ID):
                    idx = self.teach.at()
                self.teach.next()
            self.groupBox.setDisabled(False)
            self.teach_spisok.setCurrentIndex(idx)

    def journf_refresh_sql(self):
        self.tableView.setDisabled(True)
        if self.groupBox.currentIndex() >= 0:
            grp = int(self.groupBox.currentText().split()[0])
            print('==> ', grp)
            self.journ.set_param_str((grp, ))
            self.journ.refresh_select()
            val : QtSql.QSqlRecord = None
            print('select: ok')
            for i, val in enumerate(self.journ.data):
                s = []
                for j in range(val.count()):
                    s.append(str(val.value(j)))
                print(', '.join(s))
            model =  QSqlQueryModel()
            model.setQuery(self.journ.data)
            self.tableView.setModel(model)
            self.tableView.resizeColumnsToContents()
        else:
            self.tableView.setModel(None)
#        self.groupBox.clear()
#        if self.journ.refresh_select():
#            self.groups.first()
        self.tableView.setDisabled(False)


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
