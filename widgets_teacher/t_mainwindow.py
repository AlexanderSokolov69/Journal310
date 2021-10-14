import sqlite3
import sys
import traceback as tb

from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QMainWindow, QApplication, QAbstractItemView, QPushButton
from classes.qt__classes import LogWriter
from classes.t_journal import TJournalModel
from classes.t_tables import TRasp, TJournals
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
        self.rasp = TJournals(self.con)

        # self.timer = QTimer()
        # self.timer.setInterval(4000)
        # self.timer.timeout.connect(self.click)
        model = TJournalModel(self.rasp, [1])
        self.tableView.setModel(model)
        self.tableView.resizeColumnsToContents()
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableView.installEventFilter(self)
        # self.tableView.setIndexWidget(model.index(0, 3), QPushButton("button"))
        # self.timer.start()

    # def click(self):
    #     self.idx = (self.idx + 1) % 2
    #     self.rasp = self.spis[self.idx]
    #     print(self.idx)
    #     self.tableView.setModel(TJournalModel(self.rasp, [1]))
    #     self.tableView.resizeColumnsToContents()
    #     self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
    #     self.timer.start()

    def eventFilter(self, object, event=None):
        print(event.type())
        return False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    flog = LogWriter(fname='teachLog.txt')
    sys.excepthook = except_hook
    con = sqlite3.connect('..\\db\\database_J.db')
    wnd = MWindow(con, 15)
    wnd.showMaximized()
    sys.exit(app.exec())
