import sys
import traceback as tb
import datetime

from PyQt5 import QtWidgets, QtCore, QtSql, QtGui
from PyQt5.QtCore import QTimer, QModelIndex, QEvent, pyqtSignal
from PyQt5.QtGui import QPixmap
from PyQt5.QtSql import QSqlQueryModel
from PyQt5.QtWidgets import QMainWindow, QApplication, QAbstractItemView, QPushButton, QLineEdit, QLabel, QCheckBox, \
    QWidget, QFrame, QInputDialog, QTextEdit, QSizePolicy, QPlainTextEdit, QComboBox, QSplashScreen

from classes.bb_converts import date_us_ru, date_ru_us
from classes.cl_logwriter import LogWriter
from classes.cl_const import Const
from forms_journ.t_tab5 import Ui_tab5Form
from new_prg.db_connect import QUsers, QGroups, QJournals, QGroupTables
from new_prg.q_models import QTableModel
from widgets_prg.t_db_session import QtConnectDb


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
        self.edit_spisok = []
        self.groupBox.hide()
        self.txt_comment.hide()

        self.teach = QUsers(params=(Const.ACC_PREPOD, ), dsort=('u.name', ))
        self.groups = QGroups(dsort=('g.name',))
        self.journ = QJournals(params=(-1, ), dsort=('j.date', 'j.tstart'))
        self.gtable =  QGroupTables(dsort=('u.name',))

        self.teach_spisok.currentIndexChanged.connect(self.groupsf_refresh_sql)
        self.groupBox.currentIndexChanged.connect(self.journf_refresh_sql)
        self.tableView.doubleClicked.connect(self.journf_start_edit_day)
        if Const.TEST_MODE:
            self.logfile.to_log(f"""======>  Tab5. Finish __init__""")
            print("======>  Tab5. Finish __init__")

    def journf_start_edit_day(self):
#        print('click', self.tableView.currentIndex().row())
        data : QTableModel = self.tableView.model()
        # print(data.index(self.tableView.currentIndex().row(), 0).data())
        # print(data.sql_obj.at())
        # print(data.sql_obj.record().value(1))
#
        self.labelHead.setDisabled(False)
        self.frame_2.setDisabled(True)
        self.tableView.setDisabled(True)
#
        MaxWidth = 800
        layoutCorr = self.letter_place.layout()
        layoutShape = self.shape_frame.layout()
        self.shape_frame.setSizePolicy(QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum))
        layoutCorr.setContentsMargins(20, 20, 20, 20)
        layoutCorr.setAlignment(QtCore.Qt.AlignCenter)
        # self.shape_frame.setMaximumWidth(MaxWidth)
        # self.letter_place.setMaximumWidth(MaxWidth)
        # self.txt_comment.setMaximumWidth(MaxWidth)
        self.txt_comment.show()
        self.txt_comment.setPlainText(data.sql_obj.record().value(Const.JRN_COMMENT))
        self.txt_comment.setMinimumWidth(MaxWidth)
        pos = 1
#
        preset = {'present': [], 'estim': [], 'shtraf': []}
        preset['present'] = list(map(int, (data.sql_obj.record().value(Const.JRN_PRESENT).split())))
        preset['estim'] = {val.split('=')[0]: val.split('=')[1] for val in
                           data.sql_obj.record().value(Const.JRN_ESTIM).split()}
        preset['shtraf'] = {val.split('=')[0]: val.split('=')[1] for val in
                            data.sql_obj.record().value(Const.JRN_SHTRAF).split()}
#
        posSh = 0
        le1 = QPlainTextEdit(data.sql_obj.record().value(Const.JRN_THEME))
        le1.setObjectName('lesson Name')
        le1.setMaximumHeight(50)
        self.edit_spisok.append(le1)
        layoutShape.addWidget(le1, posSh, 0, posSh + 1, 9)
        posSh += 1
#
        lb = QLabel('Начало:')
        lb.setMaximumWidth(100)
        self.edit_spisok.append(lb)
        layoutShape.addWidget(lb, posSh, 2)
        le = QLineEdit(data.sql_obj.record().value(Const.JRN_START))
        le.setMaximumWidth(100)
        le.setInputMask('00:00')
        le.setObjectName('lesson tStart')
        self.edit_spisok.append(le)
        layoutShape.addWidget(le, posSh, 3)
        le = QLineEdit(date_us_ru(data.sql_obj.record().value(Const.JRN_DATE)))
        le.setObjectName('lesson Date')
        le.setInputMask('00.00.0000')
        le.setMaximumWidth(100)
        self.edit_spisok.append(le)
        layoutShape.addWidget(le, posSh, 8)
        posSh += 1
#
        lb = QLabel('Окончание:')
        self.edit_spisok.append(lb)
        lb.setMaximumWidth(100)
        layoutShape.addWidget(lb, posSh, 2)
        le = QLineEdit(data.sql_obj.record().value(Const.JRN_END))
        le.setMaximumWidth(100)
        le.setInputMask('00:00')
        le.setObjectName('lesson tEnd')
        self.edit_spisok.append(le)
        layoutShape.addWidget(le, posSh, 3)
        lb = QLabel(' ')
        self.edit_spisok.append(lb)
        lb.setMinimumWidth(30)
        layoutShape.addWidget(lb, posSh, 6)
        btn = QPushButton('Сохранить')
        btn.clicked.connect(self.journf_end_edit_day)
        # btn.installEventFilter(self)
        btn.setObjectName('Save')
        # self.clicked_enter.connect(btn.click)
        btn.setMinimumWidth(100)
        self.edit_spisok.append(btn)
        layoutShape.addWidget(btn, posSh, 7)
        btn = QPushButton('Отменить')
        btn.clicked.connect(self.journf_end_edit_day)
        # self.clicked_cancel.connect(btn.click)
        # btn.installEventFilter(self)
        btn.setObjectName('Cancel')
        btn.setMinimumWidth(100)
        self.edit_spisok.append(btn)
        layoutShape.addWidget(btn, posSh, 8)
        posSh += 2
#
        lb = QLabel('№')
        lb.setAlignment(QtCore.Qt.AlignCenter)
        self.edit_spisok.append(lb)
        layoutCorr.addWidget(lb, pos, 0)

        lb = QLabel('Фамилия И.О.')
        lb.setAlignment(QtCore.Qt.AlignCenter)
        self.edit_spisok.append(lb)
        layoutCorr.addWidget(lb, pos, 1)
#
        lb = QCheckBox('')
        lb.stateChanged.connect(self.click_in_table)
        self.edit_spisok.append(lb)
        layoutCorr.addWidget(lb, pos, 3)
        lb = QLabel('Оценка')
        lb.setAlignment(QtCore.Qt.AlignCenter)
        self.edit_spisok.append(lb)
        layoutCorr.addWidget(lb, pos, 4)
        lb = QLabel('Рейтинг')
        lb.setAlignment(QtCore.Qt.AlignCenter)
        self.edit_spisok.append(lb)
        layoutCorr.addWidget(lb, pos, 5)
        h_line = QFrame()
        h_line.setFrameShape(QFrame.HLine)
        layoutCorr.addWidget(h_line, pos, 0, pos + 1, 6)
        pos += 1
        lb = QLabel('')
        self.edit_spisok.append(lb)
        layoutCorr.addWidget(lb, pos, 3)
        pos += 2

        self.gtable.set_param_str((data.sql_obj.record().value(Const.JRN_IDG), ))
        self.gtable.refresh_select()
        self.gtable.first()
        i = 0
        while self.gtable.isValid():
            val = self.gtable.record()
            userId = val.value(Const.QGT_IDU)
            lb = QLineEdit(f"{i + 1}")
            lb.setReadOnly(True)
            lb.setStyleSheet("background-color: rgb(240, 240, 240);font: 12pt \"MS Shell Dlg 2\";")
            lb.setAlignment(QtCore.Qt.AlignCenter)
            lb.setMaximumWidth(30)
            self.edit_spisok.append(lb)
            layoutCorr.addWidget(lb, pos, 0)
            lb = QLineEdit(val.value(Const.QGT_STUDNAME).strip())
            lb.setReadOnly(True)
            lb.setStyleSheet("background-color: rgb(240, 240, 240);font: 12pt \"MS Shell Dlg 2\";")
            # lb.setMinimumWidth(300)
            lb.setAlignment(QtCore.Qt.AlignLeft)
            self.edit_spisok.append(lb)
            layoutCorr.addWidget(lb, pos, 1)
            lb = QLabel(' ')
            # lb.setMinimumWidth(50)
            self.edit_spisok.append(lb)
            layoutCorr.addWidget(lb, pos, 2)
            chb = QCheckBox()
            # chb.setMinimumWidth(40)
            chb.setMaximumWidth(40)
            chb.setObjectName(f"lesson {userId} check")
            chb.setChecked(userId in preset['present'])
            self.edit_spisok.append(chb)
            layoutCorr.addWidget(chb, pos, 3)
            oc = QLineEdit()
            oc.setMaximumWidth(60)
            oc.setObjectName(f"lesson {userId} estim")
            oc.setText(preset['estim'].get(str(userId), ''))
            self.edit_spisok.append(oc)
            layoutCorr.addWidget(oc, pos, 4)
            oc = QLineEdit()
            oc.setMaximumWidth(110)
            oc.setObjectName(f"lesson {userId} shtraf")
            oc.setText(preset['shtraf'].get(str(userId), ''))
            self.edit_spisok.append(oc)
            layoutCorr.addWidget(oc, pos, 5)
            pos += 2
            self.gtable.next()
            i += 1
        le1.selectAll()
        le1.setFocus()

    def journf_end_edit_day(self):
        print('click')

    def click_in_table(self):
        pass

    def showEvent(self, a0: QtGui.QShowEvent) -> None:
        self.teachf_refresh_sql()

    def groupsf_refresh_sql(self):
        if self.groupBox.isVisible():
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
            self.groupBox.hide()
            self.teach.first()
            idx = -1
            while self.teach.isValid():
                self.teach_spisok.addItem(f"{self.teach.value(Const.USR_ID):4} : {self.teach.value(Const.USR_NAME)}")
                if self.user_id == self.teach.value(Const.USR_ID):
                    idx = self.teach.at()
                self.teach.next()
            self.groupBox.show()
            self.teach_spisok.setCurrentIndex(idx)

    def journf_refresh_sql(self):
        if self.groupBox.currentIndex() >= 0:
            grp = int(self.groupBox.currentText().split()[0])
#            print('==> ', grp)
            self.journ.set_param_str((grp, ))
            self.journ.refresh_select()
            model =  QTableModel(self.journ)
            self.tableView.setModel(model)

            self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
            # self.tableView.setMaximumWidth(800)
            self.tableView.resizeColumnsToContents()
            self.tableView.setCurrentIndex(self.tableView.model().index(0, 0))
            self.tableView.setFocus()

        else:
            self.tableView.setModel(None)


if __name__ == '__main__':
    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    flog = LogWriter()

    spl = QSplashScreen(QPixmap('../Splash/Splash01-02.PNG'))
    spl.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)
    spl.show()

    # conn_str = 'Driver=SQL Server;Server=172.16.1.12,1433;Database=Journal4303;UID=sa;PWD=Prestige2011!;'
    # db =  QtSql.QSqlDatabase.addDatabase('QODBC')
    # db.setDatabaseName(conn_str)
    # if db.open():

    if QtConnectDb('../settings.ini').get_con():
        if Const.TEST_MODE:
            print('Connect: Ok')
        wnd = QT5Window(15)
        spl.finish(wnd)
        wnd.showMaximized()
    sys.exit(app.exec())
