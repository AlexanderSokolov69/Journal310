from PyQt5 import QtGui
from PyQt5.QtCore import QAbstractTableModel, pyqtSignal, Qt, QModelIndex
from PyQt5.QtGui import QColor

from classes.cl_const import Const
from new_prg.db_connect import TSqlQuery


class QTableModel(QAbstractTableModel):
    refresh_visual = pyqtSignal()
    def __init__(self, sql_obj: TSqlQuery):
        super(QTableModel, self).__init__()
        self.sql_obj = sql_obj
        # self.sql_obj.last()
        self.sort_col = None

    def sort(self, column: int, order: Qt.SortOrder = ...) -> None:
        pass

    def headerData(self, section: int, orientation: Qt.Orientation, role=None):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return self.sql_obj.record().field(section).name()
            else:
                return ''
        # if role == Qt.BackgroundColorRole: # BackgroundRole:
        #     # See below for the data structure.
        #     return QtGui.QColor('#c0f0f0')
        # if role == Qt.InitialSortOrderRole:
        #     # self.beginResetModel()
        #     if self.sort_col == section:
        #         self.sql_obj.data.sort(key=lambda i: i[section], reverse=True)
        #         self.sort_col = -1
        #     else:
        #         self.sql_obj.data.sort(key=lambda i: i[section])
        #         self.sort_col = section
            # self.endResetModel()
        #     return

    def columnCount(self, parent=None):
        return self.sql_obj.record().count()

    def rowCount(self, parent=None):
        return self.sql_obj.numRowsAffected()  # .size()

    # else:
    #     return 0

    def data(self, index: QModelIndex, role: Qt.ItemDataRole =None):
        ret = None
        row = index.row()
        col = index.column()
        # if col in self.date_col:
        #     ret = date_us_ru(ret)
        if role == Qt.DisplayRole or role == Qt.EditRole:
            self.sql_obj.seek(row)
            ret = self.sql_obj.record().value(col)
            if isinstance(ret, str):
                ret = ret.strip()
            if ret is None:
                return "None"
            else:
                return str(ret)
        if role == Qt.TextAlignmentRole:
            if isinstance(ret, int) or isinstance(ret, float):
                # Align right, vertical middle.
                return Qt.AlignVCenter + Qt.AlignRight
        if role == Qt.BackgroundRole and index.row() % 2:
            # See below for the data structure.
            return QtGui.QColor('#f0fcfc')
        return ret

    def flags(self, index):
            return Qt.ItemIsSelectable | Qt.ItemIsEnabled

    def endResetModel(self) -> None:
        self.refresh_visual.emit()