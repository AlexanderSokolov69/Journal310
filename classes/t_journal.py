from PyQt5 import QtGui
from PyQt5.QtCore import QAbstractTableModel, QModelIndex, Qt
from PyQt5.QtWidgets import QComboBox

from classes.bb_converts import date_us_ru
from classes.t__sqlobject import TSQLObject


class Const:
    PRESENT = 5
    ESTIM = 6
    SHTRAF = 7


class TJournalModel(QAbstractTableModel):
    def __init__(self, sql_obj: TSQLObject, date_col=[]):
        super(TJournalModel, self).__init__()
        self.sql_obj = sql_obj
        self.date_col = date_col
        self.sort_col = None

    def headerData(self, section: int, orientation: Qt.Orientation, role=None):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return self.sql_obj.header[section]
            else:
                return ''
        if role == Qt.BackgroundColorRole: # BackgroundRole:
            # See below for the data structure.
            return QtGui.QColor('#c0f0f0')
        if role == Qt.InitialSortOrderRole:
            self.beginResetModel()
            if self.sort_col == section:
                self.sql_obj.data.sort(key=lambda i: i[section], reverse=True)
                self.sort_col = -1
            else:
                self.sql_obj.data.sort(key=lambda i: i[section])
                self.sort_col = section
            self.endResetModel()
            return

    def columnCount(self, parent=None):
        if len(self.sql_obj.data) == 0:
            return 0
        else:
            return len(self.sql_obj.data[0])

    def rowCount(self, parent=None):
        return self.sql_obj.rows()

    def data(self, index: QModelIndex, role=None):
        ret = None
        if self.sql_obj.rows() > 0:
            row = index.row()
            col = index.column()
            if col in [Const.PRESENT, Const.ESTIM, Const.SHTRAF]:
                ret = len(self.sql_obj.data[row][col].split())
            else:
                ret = self.sql_obj.data[row][col]
            if col in self.date_col:
                ret = date_us_ru(ret)
        else:
            ret = ' '
        if role == Qt.DisplayRole or role == Qt.EditRole:
            if ret is None:
                return ""
            else:
                return str(ret)
        if role == Qt.TextAlignmentRole:
            if isinstance(ret, int) or isinstance(ret, float):
                # Align right, vertical middle.
                return Qt.AlignVCenter + Qt.AlignRight
        if role == Qt.BackgroundRole and index.row() % 2:
            # See below for the data structure.
            return QtGui.QColor('#f0fcfc')

    def flags(self, index):
            return Qt.ItemIsSelectable | Qt.ItemIsEnabled
