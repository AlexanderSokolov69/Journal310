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
        tab4Form.resize(1315, 900)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(tab4Form.sizePolicy().hasHeightForWidth())
        tab4Form.setSizePolicy(sizePolicy)
        tab4Form.setMinimumSize(QtCore.QSize(1200, 900))
        font = QtGui.QFont()
        font.setPointSize(10)
        tab4Form.setFont(font)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(tab4Form)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame = QtWidgets.QFrame(tab4Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(800, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(3, 2, 2, 0)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_6 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setContentsMargins(4, 4, 4, 4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_7 = QtWidgets.QFrame(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setMinimumSize(QtCore.QSize(200, 0))
        self.frame_7.setMaximumSize(QtCore.QSize(300, 999))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setLineWidth(2)
        self.frame_7.setMidLineWidth(0)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 12)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.tab4_commit_frame = QtWidgets.QFrame(self.frame_7)
        self.tab4_commit_frame.setFrameShape(QtWidgets.QFrame.Panel)
        self.tab4_commit_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tab4_commit_frame.setLineWidth(3)
        self.tab4_commit_frame.setObjectName("tab4_commit_frame")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tab4_commit_frame)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.tab4_commit_btn = QtWidgets.QPushButton(self.tab4_commit_frame)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.tab4_commit_btn.setFont(font)
        self.tab4_commit_btn.setStyleSheet("color: rgb(255, 0, 0);")
        self.tab4_commit_btn.setObjectName("tab4_commit_btn")
        self.tab4_btn_group = QtWidgets.QButtonGroup(tab4Form)
        self.tab4_btn_group.setObjectName("tab4_btn_group")
        self.tab4_btn_group.addButton(self.tab4_commit_btn)
        self.verticalLayout_6.addWidget(self.tab4_commit_btn)
        self.tab4_rollback_btn = QtWidgets.QPushButton(self.tab4_commit_frame)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.tab4_rollback_btn.setFont(font)
        self.tab4_rollback_btn.setStyleSheet("color: rgb(255, 0, 0);")
        self.tab4_rollback_btn.setObjectName("tab4_rollback_btn")
        self.tab4_btn_group.addButton(self.tab4_rollback_btn)
        self.verticalLayout_6.addWidget(self.tab4_rollback_btn)
        self.verticalLayout_5.addWidget(self.tab4_commit_frame)
        self.tab4_curr_grp = QtWidgets.QLabel(self.frame_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab4_curr_grp.sizePolicy().hasHeightForWidth())
        self.tab4_curr_grp.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tab4_curr_grp.setFont(font)
        self.tab4_curr_grp.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tab4_curr_grp.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tab4_curr_grp.setAlignment(QtCore.Qt.AlignCenter)
        self.tab4_curr_grp.setObjectName("tab4_curr_grp")
        self.verticalLayout_5.addWidget(self.tab4_curr_grp)
        self.tab4_journ_frame = QtWidgets.QFrame(self.frame_7)
        self.tab4_journ_frame.setMinimumSize(QtCore.QSize(220, 50))
        self.tab4_journ_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.tab4_journ_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tab4_journ_frame.setLineWidth(2)
        self.tab4_journ_frame.setObjectName("tab4_journ_frame")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.tab4_journ_frame)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_8 = QtWidgets.QLabel(self.tab4_journ_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.label_8.setMouseTracking(True)
        self.label_8.setToolTip("")
        self.label_8.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_8.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_7.addWidget(self.label_8)
        self.tab4_count_lcd_3 = QtWidgets.QLCDNumber(self.tab4_journ_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab4_count_lcd_3.sizePolicy().hasHeightForWidth())
        self.tab4_count_lcd_3.setSizePolicy(sizePolicy)
        self.tab4_count_lcd_3.setMinimumSize(QtCore.QSize(0, 28))
        self.tab4_count_lcd_3.setObjectName("tab4_count_lcd_3")
        self.horizontalLayout_7.addWidget(self.tab4_count_lcd_3)
        self.verticalLayout_7.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.tab4_add_btn_3 = QtWidgets.QPushButton(self.tab4_journ_frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tab4_add_btn_3.setFont(font)
        self.tab4_add_btn_3.setObjectName("tab4_add_btn_3")
        self.horizontalLayout_5.addWidget(self.tab4_add_btn_3)
        self.tab4_lmonts = QtWidgets.QComboBox(self.tab4_journ_frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tab4_lmonts.setFont(font)
        self.tab4_lmonts.setObjectName("tab4_lmonts")
        self.horizontalLayout_5.addWidget(self.tab4_lmonts)
        self.verticalLayout_7.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pushButton = QtWidgets.QPushButton(self.tab4_journ_frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_6.addWidget(self.pushButton)
        self.verticalLayout_7.addLayout(self.horizontalLayout_6)
        self.verticalLayout_5.addWidget(self.tab4_journ_frame)
        self.horizontalLayout_4.addWidget(self.frame_7)
        self.tab4_rasp_user = QtWidgets.QVBoxLayout()
        self.tab4_rasp_user.setSpacing(2)
        self.tab4_rasp_user.setObjectName("tab4_rasp_user")
        self.label_7 = QtWidgets.QLabel(self.frame_6)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.tab4_rasp_user.addWidget(self.label_7)
        self.line = QtWidgets.QFrame(self.frame_6)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.tab4_rasp_user.addWidget(self.line)
        self.tab4_journ_view = QtWidgets.QTableView(self.frame_6)
        self.tab4_journ_view.setObjectName("tab4_journ_view")
        self.tab4_rasp_user.addWidget(self.tab4_journ_view)
        self.horizontalLayout_4.addLayout(self.tab4_rasp_user)
        self.verticalLayout_2.addWidget(self.frame_6)
        self.line_5 = QtWidgets.QFrame(self.frame)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.verticalLayout_2.addWidget(self.line_5)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setContentsMargins(4, 0, 4, 4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMinimumSize(QtCore.QSize(220, 0))
        self.frame_3.setMaximumSize(QtCore.QSize(1000, 1000))
        self.frame_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setLineWidth(2)
        self.frame_3.setMidLineWidth(0)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setContentsMargins(10, 2, 10, 2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.label_3.setMouseTracking(True)
        self.label_3.setToolTip("")
        self.label_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_8.addWidget(self.label_3)
        self.tab4_count_lcd = QtWidgets.QLCDNumber(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab4_count_lcd.sizePolicy().hasHeightForWidth())
        self.tab4_count_lcd.setSizePolicy(sizePolicy)
        self.tab4_count_lcd.setMinimumSize(QtCore.QSize(0, 28))
        self.tab4_count_lcd.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tab4_count_lcd.setObjectName("tab4_count_lcd")
        self.horizontalLayout_8.addWidget(self.tab4_count_lcd)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.tab4_add_btn = QtWidgets.QPushButton(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tab4_add_btn.setFont(font)
        self.tab4_add_btn.setObjectName("tab4_add_btn")
        self.tab4_btn_group.addButton(self.tab4_add_btn)
        self.verticalLayout_3.addWidget(self.tab4_add_btn)
        self.tab4_edit_btn = QtWidgets.QPushButton(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tab4_edit_btn.setFont(font)
        self.tab4_edit_btn.setObjectName("tab4_edit_btn")
        self.tab4_btn_group.addButton(self.tab4_edit_btn)
        self.verticalLayout_3.addWidget(self.tab4_edit_btn)
        self.tab4_del_btn = QtWidgets.QPushButton(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tab4_del_btn.setFont(font)
        self.tab4_del_btn.setObjectName("tab4_del_btn")
        self.tab4_btn_group.addButton(self.tab4_del_btn)
        self.verticalLayout_3.addWidget(self.tab4_del_btn)
        self.horizontalLayout.addWidget(self.frame_3)
        self.tab4_edit_layout = QtWidgets.QGridLayout()
        self.tab4_edit_layout.setContentsMargins(-1, -1, -1, 10)
        self.tab4_edit_layout.setObjectName("tab4_edit_layout")
        self.label = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setText("")
        self.label.setObjectName("label")
        self.tab4_edit_layout.addWidget(self.label, 0, 0, 1, 1)
        self.horizontalLayout.addLayout(self.tab4_edit_layout)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        self.frame_5 = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_3.addWidget(self.frame_5)
        self.filtersLayout = QtWidgets.QVBoxLayout()
        self.filtersLayout.setObjectName("filtersLayout")
        self.tab4_filter_frame = QtWidgets.QFrame(self.frame_2)
        self.tab4_filter_frame.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab4_filter_frame.sizePolicy().hasHeightForWidth())
        self.tab4_filter_frame.setSizePolicy(sizePolicy)
        self.tab4_filter_frame.setMinimumSize(QtCore.QSize(320, 0))
        self.tab4_filter_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.tab4_filter_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tab4_filter_frame.setLineWidth(2)
        self.tab4_filter_frame.setObjectName("tab4_filter_frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab4_filter_frame)
        self.verticalLayout_4.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_10 = QtWidgets.QLabel(self.tab4_filter_frame)
        self.label_10.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_4.addWidget(self.label_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setSpacing(6)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_2 = QtWidgets.QLabel(self.tab4_filter_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_11.addWidget(self.label_2)
        self.frame_9 = QtWidgets.QFrame(self.tab4_filter_frame)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_11.addWidget(self.frame_9)
        self.flt_user = QtWidgets.QComboBox(self.tab4_filter_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.flt_user.sizePolicy().hasHeightForWidth())
        self.flt_user.setSizePolicy(sizePolicy)
        self.flt_user.setMinimumSize(QtCore.QSize(200, 0))
        self.flt_user.setObjectName("flt_user")
        self.horizontalLayout_11.addWidget(self.flt_user)
        self.verticalLayout_4.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_4 = QtWidgets.QLabel(self.tab4_filter_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_10.addWidget(self.label_4)
        self.frame_10 = QtWidgets.QFrame(self.tab4_filter_frame)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_10.addWidget(self.frame_10)
        self.flt_day = QtWidgets.QComboBox(self.tab4_filter_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.flt_day.sizePolicy().hasHeightForWidth())
        self.flt_day.setSizePolicy(sizePolicy)
        self.flt_day.setMinimumSize(QtCore.QSize(200, 0))
        self.flt_day.setObjectName("flt_day")
        self.horizontalLayout_10.addWidget(self.flt_day)
        self.verticalLayout_4.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_5 = QtWidgets.QLabel(self.tab4_filter_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_9.addWidget(self.label_5)
        self.frame_11 = QtWidgets.QFrame(self.tab4_filter_frame)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout_9.addWidget(self.frame_11)
        self.flt_kab = QtWidgets.QComboBox(self.tab4_filter_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.flt_kab.sizePolicy().hasHeightForWidth())
        self.flt_kab.setSizePolicy(sizePolicy)
        self.flt_kab.setMinimumSize(QtCore.QSize(200, 0))
        self.flt_kab.setObjectName("flt_kab")
        self.horizontalLayout_9.addWidget(self.flt_kab)
        self.verticalLayout_4.addLayout(self.horizontalLayout_9)
        self.filtersLayout.addWidget(self.tab4_filter_frame)
        self.horizontalLayout_3.addLayout(self.filtersLayout)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.line_4 = QtWidgets.QFrame(self.frame)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_2.addWidget(self.line_4)
        self.h_layout_table = QtWidgets.QHBoxLayout()
        self.h_layout_table.setContentsMargins(1, 10, -1, -1)
        self.h_layout_table.setSpacing(2)
        self.h_layout_table.setObjectName("h_layout_table")
        self.label_9 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.h_layout_table.addWidget(self.label_9)
        self.verticalLayout_2.addLayout(self.h_layout_table)
        self.horizontalLayout_2.addWidget(self.frame)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_6 = QtWidgets.QLabel(tab4Form)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.tab4_rasp_view = QtWidgets.QTableView(tab4Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab4_rasp_view.sizePolicy().hasHeightForWidth())
        self.tab4_rasp_view.setSizePolicy(sizePolicy)
        self.tab4_rasp_view.setMinimumSize(QtCore.QSize(400, 0))
        self.tab4_rasp_view.setMaximumSize(QtCore.QSize(600, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tab4_rasp_view.setFont(font)
        self.tab4_rasp_view.setObjectName("tab4_rasp_view")
        self.verticalLayout.addWidget(self.tab4_rasp_view)
        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(tab4Form)
        QtCore.QMetaObject.connectSlotsByName(tab4Form)

    def retranslateUi(self, tab4Form):
        _translate = QtCore.QCoreApplication.translate
        tab4Form.setWindowTitle(_translate("tab4Form", "Form"))
        self.tab4_commit_btn.setText(_translate("tab4Form", "Сохранить"))
        self.tab4_rollback_btn.setText(_translate("tab4Form", "Отменить"))
        self.tab4_curr_grp.setText(_translate("tab4Form", "asasda"))
        self.label_8.setText(_translate("tab4Form", "Журнал:"))
        self.tab4_add_btn_3.setText(_translate("tab4Form", "Заполнить"))
        self.pushButton.setText(_translate("tab4Form", "Удалить"))
        self.label_7.setText(_translate("tab4Form", "Журнал занятий"))
        self.label_3.setText(_translate("tab4Form", "Занятия:"))
        self.tab4_add_btn.setText(_translate("tab4Form", "Добавить"))
        self.tab4_edit_btn.setText(_translate("tab4Form", "Изменить"))
        self.tab4_del_btn.setText(_translate("tab4Form", "Удалить"))
        self.label_10.setText(_translate("tab4Form", "Фильтры:"))
        self.label_2.setText(_translate("tab4Form", "Наставник:"))
        self.label_4.setText(_translate("tab4Form", "День недели:"))
        self.label_5.setText(_translate("tab4Form", "Кабинет:"))
        self.label_6.setText(_translate("tab4Form", "РАСПИСАНИЕ"))
