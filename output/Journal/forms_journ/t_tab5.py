# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 't_tab5.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_tab5Form(object):
    def setupUi(self, tab5Form):
        tab5Form.setObjectName("tab5Form")
        tab5Form.resize(1225, 834)
        self.verticalLayout = QtWidgets.QVBoxLayout(tab5Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.commitButton = QtWidgets.QPushButton(tab5Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.commitButton.sizePolicy().hasHeightForWidth())
        self.commitButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.commitButton.setFont(font)
        self.commitButton.setStyleSheet("color: rgb(0, 170, 0);\n"
"")
        self.commitButton.setObjectName("commitButton")
        self.horizontalLayout_3.addWidget(self.commitButton)
        self.rollbackButton = QtWidgets.QPushButton(tab5Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rollbackButton.sizePolicy().hasHeightForWidth())
        self.rollbackButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.rollbackButton.setFont(font)
        self.rollbackButton.setStyleSheet("color: rgb(255, 0, 0);")
        self.rollbackButton.setObjectName("rollbackButton")
        self.horizontalLayout_3.addWidget(self.rollbackButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.frame_2 = QtWidgets.QFrame(tab5Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QtCore.QSize(400, 0))
        self.frame_2.setMaximumSize(QtCore.QSize(400, 16777215))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setLineWidth(2)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.teach_spisok = QtWidgets.QComboBox(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.teach_spisok.setFont(font)
        self.teach_spisok.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.teach_spisok.setObjectName("teach_spisok")
        self.verticalLayout_3.addWidget(self.teach_spisok)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.groupBox = QtWidgets.QComboBox(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_2.addWidget(self.groupBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.programName = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.programName.sizePolicy().hasHeightForWidth())
        self.programName.setSizePolicy(sizePolicy)
        self.programName.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.programName.setFont(font)
        self.programName.setWordWrap(True)
        self.programName.setObjectName("programName")
        self.verticalLayout_3.addWidget(self.programName)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.lcd_year = QtWidgets.QLCDNumber(self.frame_2)
        self.lcd_year.setMinimumSize(QtCore.QSize(0, 30))
        self.lcd_year.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lcd_year.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcd_year.setLineWidth(1)
        self.lcd_year.setDigitCount(4)
        self.lcd_year.setObjectName("lcd_year")
        self.horizontalLayout_5.addWidget(self.lcd_year)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(tab5Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMaximumSize(QtCore.QSize(400, 16777215))
        self.frame_3.setStyleSheet("")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setLineWidth(2)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setContentsMargins(9, -1, -1, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignCenter)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignCenter)
        self.formLayout.setObjectName("formLayout")
        self.label_4 = QtWidgets.QLabel(self.frame_3)
        self.label_4.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lcd_cnt_grp = QtWidgets.QLCDNumber(self.frame_3)
        self.lcd_cnt_grp.setMinimumSize(QtCore.QSize(0, 30))
        self.lcd_cnt_grp.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lcd_cnt_grp.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lcd_cnt_grp.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcd_cnt_grp.setDigitCount(4)
        self.lcd_cnt_grp.setObjectName("lcd_cnt_grp")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lcd_cnt_grp)
        self.label_5 = QtWidgets.QLabel(self.frame_3)
        self.label_5.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.lcd_cnt_stud = QtWidgets.QLCDNumber(self.frame_3)
        self.lcd_cnt_stud.setMinimumSize(QtCore.QSize(0, 30))
        self.lcd_cnt_stud.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lcd_cnt_stud.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcd_cnt_stud.setDigitCount(4)
        self.lcd_cnt_stud.setObjectName("lcd_cnt_stud")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lcd_cnt_stud)
        self.label_6 = QtWidgets.QLabel(self.frame_3)
        self.label_6.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.lcd_cnt_week = QtWidgets.QLCDNumber(self.frame_3)
        self.lcd_cnt_week.setMinimumSize(QtCore.QSize(0, 30))
        self.lcd_cnt_week.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lcd_cnt_week.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcd_cnt_week.setDigitCount(4)
        self.lcd_cnt_week.setObjectName("lcd_cnt_week")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lcd_cnt_week)
        self.label_7 = QtWidgets.QLabel(self.frame_3)
        self.label_7.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.lcd_h_to_week = QtWidgets.QLCDNumber(self.frame_3)
        self.lcd_h_to_week.setMinimumSize(QtCore.QSize(0, 30))
        self.lcd_h_to_week.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lcd_h_to_week.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcd_h_to_week.setDigitCount(4)
        self.lcd_h_to_week.setObjectName("lcd_h_to_week")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.lcd_h_to_week)
        self.label_8 = QtWidgets.QLabel(self.frame_3)
        self.label_8.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.lb_date_min = QtWidgets.QLabel(self.frame_3)
        self.lb_date_min.setMinimumSize(QtCore.QSize(0, 30))
        self.lb_date_min.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lb_date_min.setFont(font)
        self.lb_date_min.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_date_min.setObjectName("lb_date_min")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lb_date_min)
        self.label_10 = QtWidgets.QLabel(self.frame_3)
        self.label_10.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.lb_date_max = QtWidgets.QLabel(self.frame_3)
        self.lb_date_max.setMinimumSize(QtCore.QSize(0, 30))
        self.lb_date_max.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lb_date_max.setFont(font)
        self.lb_date_max.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_date_max.setObjectName("lb_date_max")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lb_date_max)
        self.horizontalLayout_4.addLayout(self.formLayout)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(tab5Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_2.addWidget(self.frame_4)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.line_2 = QtWidgets.QFrame(tab5Form)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout.addWidget(self.line_2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(0, -1, -1, 0)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.labelHead = QtWidgets.QLabel(tab5Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelHead.sizePolicy().hasHeightForWidth())
        self.labelHead.setSizePolicy(sizePolicy)
        self.labelHead.setMinimumSize(QtCore.QSize(0, 28))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelHead.setFont(font)
        self.labelHead.setStyleSheet("")
        self.labelHead.setAlignment(QtCore.Qt.AlignCenter)
        self.labelHead.setObjectName("labelHead")
        self.verticalLayout_4.addWidget(self.labelHead)
        self.shape_frame = QtWidgets.QFrame(tab5Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.shape_frame.sizePolicy().hasHeightForWidth())
        self.shape_frame.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.shape_frame.setFont(font)
        self.shape_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.shape_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.shape_frame.setLineWidth(2)
        self.shape_frame.setObjectName("shape_frame")
        self.shape_layout = QtWidgets.QGridLayout(self.shape_frame)
        self.shape_layout.setContentsMargins(6, 12, 6, 18)
        self.shape_layout.setVerticalSpacing(16)
        self.shape_layout.setObjectName("shape_layout")
        self.verticalLayout_4.addWidget(self.shape_frame)
        self.letter_place = QtWidgets.QFrame(tab5Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.letter_place.sizePolicy().hasHeightForWidth())
        self.letter_place.setSizePolicy(sizePolicy)
        self.letter_place.setMinimumSize(QtCore.QSize(200, 0))
        self.letter_place.setSizeIncrement(QtCore.QSize(30, 30))
        self.letter_place.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.letter_place.setFont(font)
        self.letter_place.setFrameShape(QtWidgets.QFrame.Box)
        self.letter_place.setFrameShadow(QtWidgets.QFrame.Raised)
        self.letter_place.setLineWidth(2)
        self.letter_place.setObjectName("letter_place")
        self.gridLayout = QtWidgets.QGridLayout(self.letter_place)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(-1, -1, 9, -1)
        self.gridLayout.setHorizontalSpacing(4)
        self.gridLayout.setVerticalSpacing(7)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_4.addWidget(self.letter_place)
        self.txt_comment = QtWidgets.QPlainTextEdit(tab5Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_comment.sizePolicy().hasHeightForWidth())
        self.txt_comment.setSizePolicy(sizePolicy)
        self.txt_comment.setMaximumSize(QtCore.QSize(16777215, 50))
        self.txt_comment.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.txt_comment.setFrameShape(QtWidgets.QFrame.Box)
        self.txt_comment.setFrameShadow(QtWidgets.QFrame.Raised)
        self.txt_comment.setLineWidth(2)
        self.txt_comment.setObjectName("txt_comment")
        self.verticalLayout_4.addWidget(self.txt_comment)
        self.frame_5 = QtWidgets.QFrame(tab5Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.test_label = QtWidgets.QLabel(self.frame_5)
        self.test_label.setGeometry(QtCore.QRect(70, 360, 47, 13))
        self.test_label.setText("")
        self.test_label.setObjectName("test_label")
        self.verticalLayout_4.addWidget(self.frame_5)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.line_3 = QtWidgets.QFrame(tab5Form)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout.addWidget(self.line_3)
        self.tableView = QtWidgets.QTableView(tab5Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableView.sizePolicy().hasHeightForWidth())
        self.tableView.setSizePolicy(sizePolicy)
        self.tableView.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tableView.setFont(font)
        self.tableView.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.tableView.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableView.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableView.setSortingEnabled(True)
        self.tableView.setCornerButtonEnabled(False)
        self.tableView.setObjectName("tableView")
        self.horizontalLayout.addWidget(self.tableView)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.frame = QtWidgets.QFrame(tab5Form)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(tab5Form)
        QtCore.QMetaObject.connectSlotsByName(tab5Form)

    def retranslateUi(self, tab5Form):
        _translate = QtCore.QCoreApplication.translate
        tab5Form.setWindowTitle(_translate("tab5Form", "Form"))
        self.commitButton.setText(_translate("tab5Form", "Сохранить"))
        self.rollbackButton.setText(_translate("tab5Form", "Отменить"))
        self.label.setText(_translate("tab5Form", "Уч.группа:  "))
        self.programName.setText(_translate("tab5Form", "TextLabel"))
        self.label_3.setText(_translate("tab5Form", "Учебный год:"))
        self.label_4.setText(_translate("tab5Form", "Количество учебных групп: "))
        self.label_5.setText(_translate("tab5Form", "Количество кубистов:"))
        self.label_6.setText(_translate("tab5Form", "Количество занятий в неделю:"))
        self.label_7.setText(_translate("tab5Form", "Количество часов в неделю:"))
        self.label_8.setText(_translate("tab5Form", "Первая запись журнала"))
        self.lb_date_min.setText(_translate("tab5Form", "1"))
        self.label_10.setText(_translate("tab5Form", "Последняя запись журнала:"))
        self.lb_date_max.setText(_translate("tab5Form", "2"))
        self.labelHead.setText(_translate("tab5Form", "Лист журнала:"))