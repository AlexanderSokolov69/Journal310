import sys
import sqlite3

from PyQt5.QtCore import QModelIndex, pyqtSignal, Qt, QEvent, QObject
from PyQt5.QtGui import QFocusEvent
from PyQt5.QtWidgets import QWidget, QApplication, QTableWidgetItem, QAbstractItemView, QTableView, QGridLayout, QLabel, \
    QCheckBox, QFrame, QButtonGroup, QSizePolicy, QPushButton, QComboBox, QLineEdit
from PyQt5 import QtGui, QtCore

from classes.bb_converts import get_day_list, get_kab_list, get_time_list, get_short_day_list
from classes.cl_courses import Courses
from classes.cl_group_table import GroupTable
from classes.cl_groups import Groups
from classes.cl_rasp import Rasp
from classes.cl_users import Users
from classes.db_session import connectdb
from classes.qt_classes import MultiClicker, QLabelClk
from widgets.checkTable import Ui_tab4Form
from widgets.tab3_form import Ui_tab3Form


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


class tab4FormWindow(QWidget, Ui_tab4Form):
    # NUM_SLOTS = 20
    FONT_SIZE = 9
    collisium = pyqtSignal()
    LABEL_OK = '[  ]'
    LABEL_FREE = ' ' * 4
    LABEL_COLL = 'XXX'

    def __init__(self, con):
        super(tab4FormWindow, self).__init__()
        self.setupUi(self)
        self.initUi(con)

    def initUi(self, con):
        self.con = con
        self.days_lst = get_day_list(self.con)
        self.short_days_lst = get_short_day_list(self.con)
        self.kab_lst = get_kab_list(self.con)
        self.time_lst = get_time_list(self.con)
        self.chk_buttonGroup = QButtonGroup(self)
        calend = []
        self.slots_dic = {}
        self.id = -1
        self.current_data = []
        self.new_preset = dict()
        self.edit_widgets = []
        self.h_layout_table.addWidget(QLabel())
        for nday in range(len(self.days_lst)):
            calend.append(self.create_day(nday))
            self.h_layout_table.addLayout(calend[-1])
#        self.chk_buttonGroup.buttonClicked.connect(self.click)
        self.rasp = Rasp(self.con)
        self.map_table()
        self.tab4_add_btn.clicked.connect(self.group_clicked)
        self.tab4_edit_btn.clicked.connect(self.group_clicked)
        self.tab4_del_btn.clicked.connect(self.group_clicked)
        self.tab4_commit_btn.clicked.connect(self.group_clicked)
        self.tab4_rollback_btn.clicked.connect(self.group_clicked)
        # self.installEventFilter(self)
        self.flt_user.clear()
        self.flt_user.insertItem(0, '')
        sql = f"""select distinct u.id || " : " || u.name 
            from groups g
            join users u on g.idUsers = u.id
            order by u.name"""
        cur = self.con.cursor()
        spis = cur.execute(sql).fetchall()
        self.flt_user.addItems([val[:][0] for val in spis])
        self.flt_user.setCurrentIndex(0)
        self.flt_day.insertItem(0, '')
        self.flt_day.addItems(self.days_lst)
        self.flt_day.setCurrentIndex(0)
        self.flt_kab.insertItem(0, '')
        self.flt_kab.addItems([s[0] for s in self.kab_lst])
        self.flt_kab.setCurrentIndex(0)
        self.flt_user.currentIndexChanged.connect(self.rasp_set_filter)
        self.flt_day.currentIndexChanged.connect(self.rasp_set_filter)
        self.flt_kab.currentIndexChanged.connect(self.rasp_set_filter)
        self.activate()

    def rasp_set_filter(self):
        filters = []
        if self.flt_user.count():
            if self.flt_user.currentIndex() > 0:
                id = self.flt_user.currentText().split()[0]
                filters.append(f'g.idUsers = {id}')
            if self.flt_day.currentIndex() > 0:
                id = self.flt_day.currentIndex() - 1
                filters.append(f'r.idDays = {id}')
            if self.flt_kab.currentIndex() > 0:
                id = self.flt_kab.currentIndex() - 1
                filters.append(f'r.idKabs = {id}')
            if filters:
                self.rasp.set_filter(' and '.join(filters))
            else:
                self.rasp.set_filter()
            self.activate()

    def group_clicked(self):
        btn : QPushButton = self.sender()
        name_btn = btn.objectName()
        if 'commit' in name_btn:
            self.rasp.commit()
            self.map_table()
            return
        elif 'rollback' in name_btn:
            self.rasp.rollback()
            self.map_table()
            return
        elif 'del' in name_btn:
            for row in [id.row() for id in self.tab4_rasp_view.selectedIndexes() if id.column() == 0]:
                id = self.rasp.data[row][0]
                self.rasp.rec_delete(id)
            self.map_table()
            return
        elif 'add' in name_btn:
            self.id = 0
        elif 'edit' in name_btn:
            self.id = self.rasp.data[self.tab4_rasp_view.currentIndex().row()][0]
        self.start_edit_rasp()

    def start_edit_rasp(self):
        self.current_data = []
        self.create_edit_widgets()
        self.map_table()
        self.tab4_rasp_view.setDisabled(True)
        for btn in self.tab4_btn_group.buttons():
            btn.setDisabled(True)

    def showEvent(self, a0):
        self.map_table()
        return super().showEvent(a0)

    def map_table(self):
        self.tab4_rasp_view.setDisabled(False)
        for btn in self.tab4_btn_group.buttons():
            btn.setDisabled(False)

        self.rasp.update()
        self.tab4_count_lcd.display(self.rasp.rows())
        if self.con.in_transaction:
            self.tab4_commit_btn.setDisabled(False)
            self.tab4_rollback_btn.setDisabled(False)
        else:
            self.tab4_commit_btn.setDisabled(True)
            self.tab4_rollback_btn.setDisabled(True)

        self.tab4_rasp_view.setModel(self.rasp.model())
        self.tab4_rasp_view.resizeColumnsToContents()
        self.tab4_rasp_view.setSelectionBehavior(QAbstractItemView.SelectRows)
        for d, day in enumerate(self.days_lst):
            for k, kab in enumerate(self.kab_lst):
                for t, time in enumerate(self.time_lst):
                    widg : QLabelClk = self.slots_dic.get(f"{d} {k} {t}", None)
                    if widg:
                        widg.setText(self.LABEL_FREE)
                        widg.setStyleSheet(
                            f"""background-color: rgb(255, 255, 255); font: {self.FONT_SIZE}pt "MS Shell Dlg 2";""")
        if not len(self.rasp.data[0]):
            return
        for rec in self.rasp.data:
            nday = self.days_lst.index(rec[2])
            nkab = -1
            for i, val in enumerate(self.kab_lst):
                if val[0] == rec[3]:
                    nkab = i
            for i, t in enumerate(self.time_lst):
                if rec[4] <= t < rec[5]:
                    widg : QLabel = self.slots_dic.get(f"{nday} {nkab} {i}", None)
                    if widg:
                        if widg.text() == self.LABEL_OK:
                            self.collisium.emit()
                            widg.setText(self.LABEL_COLL)
                        else:
                            widg.setText(self.LABEL_OK)
                            widg.setToolTip(f"{rec[0]} {rec[1]}")

                        widg.setStyleSheet(
                            f"""background-color: rgb{self.kab_lst[nkab][1]}; font: {self.FONT_SIZE}pt "MS Shell Dlg 2";""")

    def set_current_record(self, id=None):
        for i in range(self.tab4_rasp_view.model().rowCount()):
            # print(self.tab4_rasp_view.model().itemData(self.tab4_rasp_view.model().index(i, 0)))
            if self.tab4_rasp_view.model().itemData(self.tab4_rasp_view.model().index(i, 0))[0] == id:
                self.tab4_rasp_view.setCurrentIndex(self.tab4_rasp_view.model().index(i, 0))

    def color_table_click(self):
        if len(self.edit_widgets):
            return
        lbl : QLabelClk = self.sender()
#        print(lbl.objectName())
        if lbl.toolTip():
            self.set_current_record(lbl.toolTip().split()[0])
            self.tab4_rasp_view.setFocus()

    def color_table_dbl_click(self):
        if len(self.edit_widgets):
            return
        lbl : QLabelClk = self.sender()
#        print(lbl.toolTip())
        if lbl.toolTip():
            self.set_current_record(lbl.toolTip().split()[0])
            self.tab4_edit_btn.click()
        else:
            day, kab, tim = lbl.objectName().split()
            self.new_preset.clear()
            self.new_preset['idDays'] = int(day)
            self.new_preset['idKabs'] = int(kab)
            self.new_preset['start'] = self.time_lst[int(tim)]
            self.new_preset['end'] = self.add1_5hours(self.time_lst[int(tim)])

            self.tab4_add_btn.click()
        # print('dbl', lbl.objectName())

    def add1_5hours(self, time0 : str):
        try:
            h, m = time0.split(':')
            m2 = (int(m) + 30) % 60
            h2 = int(h) + 1 + (int(m) + 30) // 60
        except Exception:
            m2 = 0
            h2 = 0
        return(f"{h2:02}:{m2:02}")

    # def mouseDoubleClickEvent(self, a0: QtGui.QMouseEvent) -> None:
    #     print(a0, self.sender())
    #     # return self.super().MouseDoubleClickEvent(self, a0)

    def click(self):
        btn : QCheckBox = self.sender()
        # print(btn.objectName(), type(btn))
        num_day, num_kab, num_time = map(int, btn.objectName().split())
        if btn.isChecked():
            btn.setStyleSheet(f"background-color: rgb{self.kab_lst[num_kab][1]};")
        else:
            btn.setStyleSheet(f"background-color: rgb(255, 255, 255);")

    def create_day(self, day=0):
        obj = QGridLayout()
        obj.setAlignment(QtCore.Qt.AlignCenter)
        # obj.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        head = QLabel(self.short_days_lst[day])
        head.setAlignment(QtCore.Qt.AlignCenter)
        head.setStyleSheet(f"""font: {self.FONT_SIZE + 2}pt "MS Shell Dlg 2";""")

        obj.addWidget(head, 0, 0)
#        obj.addWidget(head, 0, 0, 1, 7)
        for i, num in enumerate(self.kab_lst):
            lbl = QLabel(f" {num[0]} ")
            # lbl.setStyleSheet(f'background-color: rgb{num[1]}; font: {self.FONT_SIZE}pt "MS Shell Dlg 2";')
            lbl.setAlignment(QtCore.Qt.AlignCenter)
            # sizePolicy.setHeightForWidth(lbl.sizePolicy().hasHeightForWidth())
            lbl.setSizePolicy(sizePolicy)
            lbl.setStyleSheet(f"""font: {self.FONT_SIZE}pt "MS Shell Dlg 2";""")
#            lbl.setStyleSheet(f"background-color: rgb{num[1]};")
            obj.addWidget(lbl, 0, i + 1)
        for i in range(len(self.time_lst)):
            lbl = QLabel(f"{self.time_lst[i]} ")
            lbl.setSizePolicy(sizePolicy)
            lbl.setStyleSheet(f"""font: {self.FONT_SIZE}pt "MS Shell Dlg 2";""")
#            lbl.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
#            sizePolicy.setHeightForWidth(lbl.sizePolicy().hasHeightForWidth())
            lbl.setAlignment(QtCore.Qt.AlignCenter)
            obj.addWidget(lbl, i + 1, 0)
            for j, num in enumerate(self.kab_lst):
                # ch_b = QCheckBox(' ')
                ch_b = QLabelClk('')
                ch_b.clicked.connect(self.color_table_click)
                ch_b.dblClicked.connect(self.color_table_dbl_click)
                ch_b.setAlignment(QtCore.Qt.AlignCenter)
                ch_b.setObjectName(f"{day} {j} {i}")
                ch_b.setStyleSheet(f"""background-color: rgb(255, 255, 255);  font: {self.FONT_SIZE}pt "MS Shell Dlg 2";""")
                sizePolicy.setHeightForWidth(ch_b.sizePolicy().hasHeightForWidth())
                ch_b.setSizePolicy(sizePolicy)
                self.slots_dic[ch_b.objectName()] = ch_b
                obj.addWidget(ch_b, i + 1, j + 1)
        v_line = QFrame()
        v_line.setFrameShape(QFrame.VLine)
        obj.addWidget(v_line, 0, len(self.kab_lst) + 1, i + 2, len(self.kab_lst) + 1)
        return obj

    def delete_edit_form(self, curLayout):
        """ Удаляем поля редактирования """
        for widg in self.edit_widgets:
            curLayout.removeWidget(widg)
            widg.deleteLater()
        self.edit_widgets.clear()

    def create_edit_widgets(self):
        curLayout = self.tab4_edit_layout
        """ Создание полей редактирования записи """
        self.current_data = self.rasp.get_record(self.id)
        self.delete_edit_form(curLayout)
#        print(self.current_data)
        if not self.current_data[0][2] and self.new_preset:
            self.current_data[1][2] = self.new_preset['idDays']
            self.current_data[2][2] = self.new_preset['idKabs']
            self.current_data[3][2] = self.new_preset['start']
            self.current_data[4][2] = self.new_preset['end']
            self.new_preset.clear()
        lrow = 0
        sP = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        lP = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        for i, val in enumerate(self.current_data):
            self.edit_widgets.append(QLabel(val[1], self))
            curLayout.addWidget(self.edit_widgets[-1], i, 0)
            self.edit_widgets[-1].setSizePolicy(lP)
            if val[0][:2] == 'id':
                self.edit_widgets.append(QComboBox(self))
                self.edit_widgets[-1].setDisabled(False)
                self.edit_widgets[-1].setSizePolicy(sP)
                self.edit_widgets[-1].setFocusPolicy(Qt.StrongFocus)
                curLayout.addWidget(self.edit_widgets[-1], i, 1)
                if val[0][2:] == 'Groups':
                    sql = f"""select id || " : " || name from {val[0][2:]} order by name"""
                else:
                    sql = f"""select id || " : " || name from {val[0][2:]}"""
                # sql = f"select name from {val[0][2:]}"
                cur = self.con.cursor()
                spis = cur.execute(sql).fetchall()
                self.edit_widgets[-1].addItems([val[:][0] for val in spis])
                for i in range(self.edit_widgets[-1].count()):
                    fnd = self.edit_widgets[-1].itemText(i)
                    id = fnd[:fnd.find(':') - 1]
                    if id == str(val[2]):
                        self.edit_widgets[-1].setCurrentIndex(i)
                # print(self.edit_widgets[-1].count())
            else:
                le = QLineEdit(str(val[2]), self)
                if val[0][:] in ['start', 'end']:
                    le.setInputMask('99:99')
                    le.setObjectName(val[0][:])
                    if val[0][:] == 'end':
                        le.installEventFilter(self)
                        le.returnPressed.connect(self.calculate)
                    else:
                        le.returnPressed.connect(self.selected_edit)
                self.edit_widgets.append(le)
                curLayout.addWidget(self.edit_widgets[-1], i, 1)
                self.edit_widgets[-1].setSizePolicy(sP)
            self.edit_widgets[1].setFocus()
            lrow = i
        pbS = QPushButton('Применить')
        pbS.setSizePolicy(sP)
        pbS.setObjectName('Save')
        pbS.clicked.connect(self.edit_buttons)
        curLayout.addWidget(pbS, 4, 2)
        self.edit_widgets.append(pbS)
        pbC = QPushButton('Отменить')
        pbC.setSizePolicy(sP)
        pbC.setObjectName('Cancel')
        pbC.clicked.connect(self.edit_buttons)
        curLayout.addWidget(pbC, 5, 2)
        curLayout.addWidget(QFrame(), 0, 3, lrow, 3)
        self.edit_widgets.append(pbC)

    def calculate(self, object):
        new = ''
        for key, _, val in self.current_data:
            if key == 'start':
                new = self.add1_5hours(val)
                break
        object.setText(new)


    def selected_edit(self):
        if self.sender().objectName() in ['start', 'end']:
            self.sender().selectAll()


    def edit_buttons(self):
        if self.sender().objectName() in 'Save':
            self.update_edit_frame()
        self.delete_edit_form(self.tab4_edit_layout)
        self.map_table()

    def update_edit_frame(self):
        """ Сохраняем результаты редактирования. либо создание новой записи """
        arg = {}
        for i, widg in enumerate(self.edit_widgets[1:-2:2]):
            if type(widg) == QLineEdit:
                arg[self.current_data[i][0]] = widg.text().strip()
            elif type(widg) == QComboBox:
                fnd = widg.currentText()
                id = fnd[:fnd.find(':') - 1]
                arg[self.current_data[i][0]] = str(id)
            else:
                print('Ошибочный тип в редакторе!')
        for widg in self.edit_widgets:
            widg.deleteLater()
        self.edit_widgets.clear()
        if self.id == 0:
            self.rasp.rec_append(arg)
        else:
            self.rasp.rec_update(self.id, arg)

    def activate(self):
        """ Проверка на сохранение данных при выходе из программы """
        self.delete_edit_form(self.tab4_edit_layout)
        self.map_table()
        self.show()

    def eventFilter(self, object: 'QObject', event: 'QEvent') -> bool:
        # # print(object.objectName(), event.type())
        # if object.objectName() == 'end':
        #     if event.type() == 12:
        #         self.calculate(object)
        return super().eventFilter(object, event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    sys.excepthook = except_hook
    con = sqlite3.connect('../db/database_J.db')
#    con = sqlite3.connect('O:/Журналы/db/database_J.db')
    wnd = tab4FormWindow(con)
    wnd.show()
    sys.exit(app.exec())
