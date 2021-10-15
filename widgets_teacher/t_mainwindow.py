import sqlite3
import sys
import traceback as tb

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QTimer, QModelIndex
from PyQt5.QtWidgets import QMainWindow, QApplication, QAbstractItemView, QPushButton, QLineEdit, QLabel, QCheckBox

from classes.bb_converts import date_us_ru
from classes.qt__classes import LogWriter
from classes.t_journal import TJournalModel
from classes.t_tables import TRasp, TJournals, TUsers, TGroups, TGroupTable
from forms_teacher.main_window import Ui_TchWindow


def except_hook(cls, exception, traceback):
    global flog
    flog.to_log(f"""{exception} | \n{tb.format_tb(traceback)[0]}""")
    sys.__excepthook__(cls, exception, traceback)


class MWindow(QMainWindow, Ui_TchWindow):  # Главное окно приложения
    def __init__(self, con, user_id):
        super(MWindow, self).__init__()
        self.setupUi(self)
        self.con = con
        self.user_id = user_id
        self.edit_spisok = []
        self.journ = TJournals(self.con)
        model = TJournalModel(self.journ, [1])
        self.tableView.setModel(model)
        # self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        # self.tableView.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableView.model().dataChanged.connect(self.signal)
        self.tableView.doubleClicked.connect(self.start_edit_day)

        self.user = TUsers(con)
        self.user.set_filter( f'u.id = {self.user_id}')
        self.groups = TGroups(con)
        self.groups.set_filter( f'u.id = {self.user_id}')
        self.group_table = TGroupTable(con)
        self.teachName.setText(self.user.data[0][1])
        self.groupBox.setCurrentIndex(-1)
        self.groupBox.currentIndexChanged.connect(self.change_current_group)
        self.groupBox.insertItems(0, [val[1] for val in self.groups.data])

    def start_edit_day(self):
        self.labelHead.setDisabled(False)
        self.frame_2.setDisabled(True)
        self.tableView.setDisabled(True)
        self.record_cursor = self.tableView.currentIndex().row()
        pos = 0
        # self.frame_4.setMaximumWidth(500)

        self.frame_4.layout().setAlignment(QtCore.Qt.AlignCenter)
        le = QLineEdit(self.journ.data[self.record_cursor][2])
        self.edit_spisok.append(le)
        self.frame_4.layout().addWidget(le, pos, 0, pos + 1, 8)
        le = QLineEdit(date_us_ru(self.journ.data[self.record_cursor][1]))
        le.setInputMask('00.00.0000')
        le.setMaximumWidth(100)
        self.edit_spisok.append(le)
        self.frame_4.layout().addWidget(le, pos, 8)
        pos += 1

        lb = QLabel('Начало:')
        lb.setMaximumWidth(100)
        self.edit_spisok.append(lb)
        self.frame_4.layout().addWidget(lb, pos, 2)
        le = QLineEdit(self.journ.data[self.record_cursor][3])
        le.setMaximumWidth(100)
        le.setInputMask('00:00')
        self.edit_spisok.append(le)
        self.frame_4.layout().addWidget(le, pos, 3)
        lb = QLabel('')
        lb.setMaximumWidth(100)
        self.edit_spisok.append(lb)
        self.frame_4.layout().addWidget(lb, pos, 5)
        pos += 1

        lb = QLabel('Окончание:')
        self.edit_spisok.append(lb)
        lb.setMaximumWidth(100)
        self.frame_4.layout().addWidget(lb, pos, 2)
        le = QLineEdit(self.journ.data[self.record_cursor][4])
        le.setMaximumWidth(100)
        le.setInputMask('00:00')
        self.edit_spisok.append(le)
        self.frame_4.layout().addWidget(le, pos, 3)
        lb = QLabel(' ')
        self.edit_spisok.append(lb)
        lb.setMinimumWidth(100)
        self.frame_4.layout().addWidget(lb, pos, 6)
        btn = QPushButton('Сохранить')
        btn.setMinimumWidth(100)
        self.edit_spisok.append(btn)
        btn.clicked.connect(self.end_edit_day)
        self.frame_4.layout().addWidget(btn, pos, 7)
        btn = QPushButton('Отменить')
        btn.setMinimumWidth(100)
        self.edit_spisok.append(btn)
        btn.clicked.connect(self.end_edit_day)
        self.frame_4.layout().addWidget(btn, pos, 8)
        pos += 2

        lb = QLabel('№')
        lb.setMinimumWidth(50)
        self.edit_spisok.append(lb)
        self.frame_4.layout().addWidget(lb, pos, 0, pos, 0)
        lb = QLabel('Фамилия И.О.')
        lb.setMinimumWidth(250)
        self.edit_spisok.append(lb)
        self.frame_4.layout().addWidget(lb, pos, 2, pos, 4)
        lb = QCheckBox('Посещ.')
        lb.setMinimumWidth(100)
        self.edit_spisok.append(lb)
        self.frame_4.layout().addWidget(lb, pos, 6, pos, 6)
        lb = QLabel('Оценка')
        lb.setMinimumWidth(100)
        self.edit_spisok.append(lb)
        self.frame_4.layout().addWidget(lb, pos, 7, pos, 7)
        lb = QLabel('Штраф')
        lb.setMinimumWidth(100)
        self.edit_spisok.append(lb)
        self.frame_4.layout().addWidget(lb, pos, 8, pos, 8)
        pos += 2

        line = QtWidgets.QFrame(self.centralwidget)
        line.setFrameShape(QtWidgets.QFrame.HLine)
        line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_4.layout().addWidget(line, pos, 0, pos + 1, 8)

        pos += 2
        self.group_table.set_filter(f"g.id = {self.groups.data[self.groupBox.currentIndex()][0]}")
        if self.group_table.rows() > 0:
            for i, user in enumerate(self.group_table.data):
                lb = QLabel(f"{i + 1:02}")
                self.edit_spisok.append(lb)
                self.frame_4.layout().addWidget(lb, pos, 0, pos + 1, 1)

                lb = QLabel(user[2])
                self.edit_spisok.append(lb)
                self.frame_4.layout().addWidget(lb, pos, 2, pos + 1, 4)

                chb = QCheckBox()
#                chb.setLayoutDirection(QtCore.Qt.RightToLeft)
                self.edit_spisok.append(chb)
                self.frame_4.layout().addWidget(chb, pos, 6, pos + 1, 6)

                oc = QLineEdit()
                oc.setMaximumWidth(30)
                self.edit_spisok.append(oc)
                self.frame_4.layout().addWidget(oc, pos, 7, pos + 1, 7)

                oc = QLineEdit()
                oc.setMaximumWidth(100)
                self.edit_spisok.append(oc)
                self.frame_4.layout().addWidget(oc, pos, 8, pos + 1, 8)
                pos += 3
        # for w in self.edit_spisok:
        #     w.setMinimumWidth(100)

    def end_edit_day(self):
        self.labelHead.setDisabled(True)
        self.frame_2.setDisabled(False)
        self.tableView.setDisabled(False)
        for wid in self.edit_spisok:
            self.frame_4.layout().removeWidget(wid)
            wid.deleteLater()
        self.edit_spisok.clear()

    def change_current_group(self):
        self.tableView.model().beginResetModel()
        self.programName.setText(self.groups.data[self.groupBox.currentIndex()][2])
        self.journ.set_filter(f"j.idGroups = {self.groups.data[self.groupBox.currentIndex()][0]}")
        self.tableView.setCurrentIndex(self.tableView.model().index(0, 0))
        self.tableView.model().endResetModel()
        # self.tableView.resizeColumnsToContents()
        self.tableView.selectRow(0)
        self.tableView.setFocus()

    def signal(self):
        print('!!')

    def eventFilter(self, object, event=None):
        print(event.type())
        return False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    flog = LogWriter(fname='teachLog.txt')
    sys.excepthook = except_hook
    con = sqlite3.connect('..\\db\\database_J.db')
    wnd = MWindow(con, 19)
    wnd.showMaximized()
    sys.exit(app.exec())
