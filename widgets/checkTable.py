# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'checkTable.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_tab4Form(object):
    def setupUi(self, tab4Form):
        tab4Form.setObjectName("tab4Form")
        tab4Form.resize(606, 704)
        font = QtGui.QFont()
        font.setPointSize(12)
        tab4Form.setFont(font)
        self.verticalLayout = QtWidgets.QVBoxLayout(tab4Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(tab4Form)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.h_layout_table = QtWidgets.QHBoxLayout()
        self.h_layout_table.setContentsMargins(3, -1, -1, -1)
        self.h_layout_table.setObjectName("h_layout_table")
        self.verticalLayout_2.addLayout(self.h_layout_table)
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.tab4_edit_layout = QtWidgets.QGridLayout()
        self.tab4_edit_layout.setObjectName("tab4_edit_layout")
        self.verticalLayout_2.addLayout(self.tab4_edit_layout)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setMinimumSize(QtCore.QSize(120, 0))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.tab4_count_lcd = QtWidgets.QLCDNumber(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab4_count_lcd.sizePolicy().hasHeightForWidth())
        self.tab4_count_lcd.setSizePolicy(sizePolicy)
        self.tab4_count_lcd.setMinimumSize(QtCore.QSize(0, 30))
        self.tab4_count_lcd.setObjectName("tab4_count_lcd")
        self.verticalLayout_3.addWidget(self.tab4_count_lcd)
        self.tab4_add_btn = QtWidgets.QPushButton(self.frame_3)
        self.tab4_add_btn.setObjectName("tab4_add_btn")
        self.tab4_btn_group = QtWidgets.QButtonGroup(tab4Form)
        self.tab4_btn_group.setObjectName("tab4_btn_group")
        self.tab4_btn_group.addButton(self.tab4_add_btn)
        self.verticalLayout_3.addWidget(self.tab4_add_btn)
        self.tab4_edit_btn = QtWidgets.QPushButton(self.frame_3)
        self.tab4_edit_btn.setObjectName("tab4_edit_btn")
        self.tab4_btn_group.addButton(self.tab4_edit_btn)
        self.verticalLayout_3.addWidget(self.tab4_edit_btn)
        self.tab4_del_btn = QtWidgets.QPushButton(self.frame_3)
        self.tab4_del_btn.setObjectName("tab4_del_btn")
        self.tab4_btn_group.addButton(self.tab4_del_btn)
        self.verticalLayout_3.addWidget(self.tab4_del_btn)
        self.tab4_commit_btn = QtWidgets.QPushButton(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.tab4_commit_btn.setFont(font)
        self.tab4_commit_btn.setObjectName("tab4_commit_btn")
        self.tab4_btn_group.addButton(self.tab4_commit_btn)
        self.verticalLayout_3.addWidget(self.tab4_commit_btn)
        self.tab4_rollback_btn = QtWidgets.QPushButton(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.tab4_rollback_btn.setFont(font)
        self.tab4_rollback_btn.setObjectName("tab4_rollback_btn")
        self.tab4_btn_group.addButton(self.tab4_rollback_btn)
        self.verticalLayout_3.addWidget(self.tab4_rollback_btn)
        self.frame_4 = QtWidgets.QFrame(self.frame_3)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_3.addWidget(self.frame_4)
        self.horizontalLayout.addWidget(self.frame_3)
        self.tab4_rasp_view = QtWidgets.QTableView(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab4_rasp_view.sizePolicy().hasHeightForWidth())
        self.tab4_rasp_view.setSizePolicy(sizePolicy)
        self.tab4_rasp_view.setObjectName("tab4_rasp_view")
        self.horizontalLayout.addWidget(self.tab4_rasp_view)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(tab4Form)
        QtCore.QMetaObject.connectSlotsByName(tab4Form)

    def retranslateUi(self, tab4Form):
        _translate = QtCore.QCoreApplication.translate
        tab4Form.setWindowTitle(_translate("tab4Form", "Form"))
        self.label_2.setText(_translate("tab4Form", "Записей:"))
        self.tab4_add_btn.setText(_translate("tab4Form", "Добавить"))
        self.tab4_edit_btn.setText(_translate("tab4Form", "Изменить"))
        self.tab4_del_btn.setText(_translate("tab4Form", "Удалить"))
        self.tab4_commit_btn.setText(_translate("tab4Form", "Сохранить"))
        self.tab4_rollback_btn.setText(_translate("tab4Form", "Отменить"))
