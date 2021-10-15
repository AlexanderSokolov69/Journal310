import sqlite3
import sys
import traceback as tb

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QTimer, QModelIndex
from PyQt5.QtWidgets import QMainWindow, QApplication, QAbstractItemView, QPushButton, QLineEdit, QLabel, QCheckBox, \
    QWidget, QFrame

from classes.bb_converts import date_us_ru, date_ru_us
from classes.qt__classes import LogWriter
from classes.t_journal import TJournalModel, Const
from classes.t_tables import TRasp, TJournals, TUsers, TGroups, TGroupTable
from forms_teacher.t_tab5 import Ui_tab5Form


def except_hook(cls, exception, traceback):
    global flog
    flog.to_log(f"""{exception} | \n{tb.format_tb(traceback)[0]}""")
    sys.__excepthook__(cls, exception, traceback)


class T5Window(QWidget, Ui_tab5Form):  # tab5 формы
    def __init__(self, con, user_id):
        super(T5Window, self).__init__()
        self.setupUi(self)
        self.con: sqlite3.connect = con
        self.user_id = user_id
        self.edit_spisok = []

        self.user = TUsers(con)
        self.user.set_filter( f'u.id = {self.user_id}')
        self.groups = TGroups(con)
        self.groups.set_filter( f'g.idUsers = {self.user_id}')
        # print(self.groups.data)
        self.group_table = TGroupTable(con)
        self.teachName.setText(self.user.data[0][1])
        self.journ = TJournals(self.con)
        model = TJournalModel(self.journ, [1])
        self.tableView.setModel(model)
        self.groupBox.currentIndexChanged.connect(self.change_current_group)
        self.activate()
        self.tableView.model().dataChanged.connect(self.signal)
        self.tableView.doubleClicked.connect(self.start_edit_day)

        self.commitButton.clicked.connect(self.commit_action)
        self.rollbackButton.clicked.connect(self.commit_action)
        self.installEventFilter(self)

    def activate(self):
        self.tableView.model().beginResetModel()
        self.groups.update()
        self.groupBox.clear()
        self.groupBox.setCurrentIndex(-1)
        if self.groups.rows() > 0:
            self.groupBox.insertItems(0, [val[1] for val in self.groups.data])
        else:
            self.journ.set_filter(f"j.idGroups = -1")
        self.tableView.model().endResetModel()
        self.show()

    def commit_action(self):
        self.tableView.model().beginResetModel()
        if self.sender().objectName() == 'commitButton':
            self.journ.commit()
        else:
            self.journ.rollback()
        self.journ.update()
        self.tableView.model().endResetModel()
        self.tableView.resizeColumnsToContents()
        self.tableView.selectRow(0)
        self.tableView.setFocus()

    def eventFilter(self, object, event):
        if self.con.in_transaction:
            self.commitButton.show()
            self.rollbackButton.show()
        else:
            self.commitButton.hide()
            self.rollbackButton.hide()
        return False

    def start_edit_day(self):
        lyoutCorr = self.letter_place.layout()
        self.labelHead.setDisabled(False)
        self.frame_2.setDisabled(True)
        self.tableView.setDisabled(True)
        self.record_cursor = self.tableView.currentIndex().row()
        pos = 0

        preset = {'present': [], 'estim': [], 'shtraf': []}
        preset['present'] = list(map(int, (self.journ.data[self.record_cursor][Const.PRESENT]).split()))
        preset['estim'] = {val[0]: val[1] for val in (self.journ.data[self.record_cursor][Const.ESTIM]).split()}
        preset['shtraf'] = {val[0]: val[1] for val in (self.journ.data[self.record_cursor][Const.SHTRAF]).split()}
        lyoutCorr.setAlignment(QtCore.Qt.AlignCenter)
        le = QLineEdit(self.journ.data[self.record_cursor][2])
        le.setObjectName('lesson Name')
        self.edit_spisok.append(le)
        lyoutCorr.addWidget(le, pos, 0, pos + 1, 8)
        le = QLineEdit(date_us_ru(self.journ.data[self.record_cursor][1]))
        le.setObjectName('lesson Date')
        le.setInputMask('00.00.0000')
        le.setMaximumWidth(100)
        self.edit_spisok.append(le)
        lyoutCorr.addWidget(le, pos, 8)
        pos += 1

        lb = QLabel('Начало:')
        lb.setMaximumWidth(100)
        self.edit_spisok.append(lb)
        lyoutCorr.addWidget(lb, pos, 2)
        le = QLineEdit(self.journ.data[self.record_cursor][3])
        le.setMaximumWidth(100)
        le.setInputMask('00:00')
        le.setObjectName('lesson Start')
        self.edit_spisok.append(le)
        lyoutCorr.addWidget(le, pos, 3)
        lb = QLabel('')
        lb.setMaximumWidth(100)
        self.edit_spisok.append(lb)
        lyoutCorr.addWidget(lb, pos, 5)
        pos += 1

        lb = QLabel('Окончание:')
        self.edit_spisok.append(lb)
        lb.setMaximumWidth(100)
        lyoutCorr.addWidget(lb, pos, 2)
        le = QLineEdit(self.journ.data[self.record_cursor][4])
        le.setMaximumWidth(100)
        le.setInputMask('00:00')
        le.setObjectName('lesson End')
        self.edit_spisok.append(le)
        lyoutCorr.addWidget(le, pos, 3)
        lb = QLabel(' ')
        self.edit_spisok.append(lb)
        lb.setMinimumWidth(100)
        lyoutCorr.addWidget(lb, pos, 6)
        btn = QPushButton('Сохранить')
        btn.setObjectName('Save')
        btn.setMinimumWidth(100)
        self.edit_spisok.append(btn)
        btn.clicked.connect(self.end_edit_day)
        lyoutCorr.addWidget(btn, pos, 7)
        btn = QPushButton('Отменить')
        btn.setObjectName('Cancel')
        btn.setMinimumWidth(100)
        self.edit_spisok.append(btn)
        btn.clicked.connect(self.end_edit_day)
        lyoutCorr.addWidget(btn, pos, 8)
        pos += 2

        lb = QLabel('№')
        lb.setMinimumWidth(50)
        self.edit_spisok.append(lb)
        lyoutCorr.addWidget(lb, pos, 0, pos, 0)
        lb = QLabel('Фамилия И.О.')
        lb.setMinimumWidth(250)
        self.edit_spisok.append(lb)
        lyoutCorr.addWidget(lb, pos, 2, pos, 4)
        lb = QCheckBox('Посещ.')
        lb.stateChanged.connect(self.click_in_table)
        lb.setMinimumWidth(100)
        self.edit_spisok.append(lb)
        lyoutCorr.addWidget(lb, pos, 6, pos, 6)
        lb = QLabel('Оценка')
        lb.setMinimumWidth(100)
        self.edit_spisok.append(lb)
        lyoutCorr.addWidget(lb, pos, 7, pos, 7)
        lb = QLabel('Штраф')
        lb.setMinimumWidth(100)
        self.edit_spisok.append(lb)
        lyoutCorr.addWidget(lb, pos, 8, pos, 8)
        pos += 2

        h_line = QFrame()
        h_line.setFrameShape(QFrame.HLine)
        lyoutCorr.addWidget(h_line, pos, 0, pos + 1, 8)

        pos += 2
        self.group_table.set_filter(f"g.id = {self.groups.data[self.groupBox.currentIndex()][0]}")
        if self.group_table.rows() > 0:
            for i, user in enumerate(self.group_table.data):
                userId = self.group_table.data[i][0]
#                print(type(userId), userId)
#                print(preset)
                lb = QLabel(f"{i + 1:02}")
                self.edit_spisok.append(lb)
                lyoutCorr.addWidget(lb, pos, 0, pos + 1, 1)

                lb = QLabel(user[2])
                self.edit_spisok.append(lb)
                lyoutCorr.addWidget(lb, pos, 2, pos + 1, 4)

                chb = QCheckBox()
                chb.setObjectName(f"lesson {userId} check")
                chb.setChecked(userId in preset['present'])
                self.edit_spisok.append(chb)
                lyoutCorr.addWidget(chb, pos, 6, pos + 1, 6)

                oc = QLineEdit()
                oc.setMaximumWidth(30)
                oc.setObjectName(f"lesson {userId} estim")
                oc.setText(preset['estim'].get(userId, ''))
                self.edit_spisok.append(oc)
                lyoutCorr.addWidget(oc, pos, 7, pos + 1, 7)

                oc = QLineEdit()
                oc.setMaximumWidth(100)
                oc.setObjectName(f"lesson {userId} shtraf")
                oc.setText(preset['shtraf'].get(userId, ''))
                self.edit_spisok.append(oc)
                lyoutCorr.addWidget(oc, pos, 8, pos + 1, 8)
                pos += 3
        # for w in self.edit_spisok:
        #     w.setMinimumWidth(100)

    def click_in_table(self):
        new_state = self.sender().isChecked()
        for chb in self.edit_spisok:
            if isinstance(chb, QCheckBox):
                chb.setChecked(new_state)

    def end_edit_day(self):
        to_save = self.sender().objectName() == 'Save'
        self.labelHead.setDisabled(True)
        self.frame_2.setDisabled(False)
        self.tableView.setDisabled(False)
        result_head = {'present': [], 'estim': [], 'shtraf': []}
        # result_head['Id'] = self.journ.data[self.record_cursor][0]
        for wid in self.edit_spisok:
            if to_save:
                if 'lesson' in wid.objectName():
                    args = wid.objectName().split()
                    if len(args) == 2:
                        if args[1] == 'Date':
                            result_head[args[1]] = date_ru_us(wid.text())
                        else:
                            result_head[args[1]] = f'{wid.text()}'
                    elif len(args) == 3:
                        if args[2] == 'check':
                            if wid.isChecked():
                                result_head['present'].append(args[1])
                        if args[2] == 'estim':
                            if wid.text():
                                result_head['estim'].append(f'{args[1]}={wid.text().split()[0]}')
                        if args[2] == 'shtraf':
                            if wid.text():
                                result_head['shtraf'].append(f'{args[1]}={wid.text().split()[0]}')
            self.letter_place.layout().removeWidget(wid)
            wid.deleteLater()
        if to_save:
            self.tableView.model().beginResetModel()
            id = self.journ.data[self.record_cursor][0]
            result_head['present'] = ' '.join(result_head['present'])
            result_head['estim'] = ' '.join(result_head['estim'])
            result_head['shtraf'] = ' '.join(result_head['shtraf'])
            self.journ.rec_update(id, result_head)

    #        self.journ.commit()
            self.journ.update()
            self.tableView.model().endResetModel()
            self.tableView.resizeColumnsToContents()
        self.tableView.setFocus()
        self.edit_spisok.clear()

    def change_current_group(self):
        self.tableView.model().beginResetModel()
        self.programName.setText(self.groups.data[self.groupBox.currentIndex()][2])
        self.journ.set_filter(f"j.idGroups = {self.groups.data[self.groupBox.currentIndex()][0]}")
        self.tableView.setCurrentIndex(self.tableView.model().index(0, 0))
        self.tableView.model().endResetModel()
        self.tableView.resizeColumnsToContents()
        self.tableView.selectRow(0)
        self.tableView.setFocus()

    def signal(self):
        print('!!')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    flog = LogWriter(fname='teachLog.txt')
    sys.excepthook = except_hook
    con = sqlite3.connect('..\\db\\database_J.db')
    wnd = T5Window(con, 15)
    wnd.showMaximized()
    sys.exit(app.exec())
