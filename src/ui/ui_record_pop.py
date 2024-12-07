# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_record_pop.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(361, 738)
        Form.setMinimumSize(QtCore.QSize(361, 382))
        Form.setMaximumSize(QtCore.QSize(361, 1080))
        Form.setSizeIncrement(QtCore.QSize(0, 0))
        Form.setWindowOpacity(10.0)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet("")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_race_label_3 = QtWidgets.QLabel(Form)
        self.label_race_label_3.setMinimumSize(QtCore.QSize(0, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_race_label_3.setFont(font)
        self.label_race_label_3.setScaledContents(False)
        self.label_race_label_3.setWordWrap(False)
        self.label_race_label_3.setObjectName("label_race_label_3")
        self.verticalLayout.addWidget(self.label_race_label_3, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.label_16 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_2.addWidget(self.label_16)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.widget1 = QtWidgets.QWidget(Form)
        self.widget1.setMinimumSize(QtCore.QSize(0, 41))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.label1 = QtWidgets.QLabel(self.widget1)
        self.label1.setMinimumSize(QtCore.QSize(36, 36))
        self.label1.setMaximumSize(QtCore.QSize(36, 36))
        self.label1.setStyleSheet("border-image: url(media/rtime.svg);")
        self.label1.setText("")
        self.label1.setObjectName("label1")
        self.horizontalLayout_3.addWidget(self.label1)
        self.label_1 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_1.setFont(font)
        self.label_1.setScaledContents(False)
        self.label_1.setWordWrap(False)
        self.label_1.setObjectName("label_1")
        self.horizontalLayout_3.addWidget(self.label_1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout.addWidget(self.widget1)
        self.widget3 = QtWidgets.QWidget(Form)
        self.widget3.setMinimumSize(QtCore.QSize(0, 41))
        self.widget3.setObjectName("widget3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget3)
        self.horizontalLayout_6.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem4)
        self.label3 = QtWidgets.QLabel(self.widget3)
        self.label3.setMinimumSize(QtCore.QSize(36, 36))
        self.label3.setMaximumSize(QtCore.QSize(36, 36))
        self.label3.setStyleSheet("border-image: url(media/bbbv_s.svg);")
        self.label3.setText("")
        self.label3.setObjectName("label3")
        self.horizontalLayout_6.addWidget(self.label3)
        self.label_3 = QtWidgets.QLabel(self.widget3)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setScaledContents(False)
        self.label_3.setWordWrap(False)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_6.addWidget(self.label_3)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem5)
        self.verticalLayout.addWidget(self.widget3)
        self.widget5 = QtWidgets.QWidget(Form)
        self.widget5.setMinimumSize(QtCore.QSize(0, 41))
        self.widget5.setObjectName("widget5")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget5)
        self.horizontalLayout_7.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem6)
        self.label5 = QtWidgets.QLabel(self.widget5)
        self.label5.setMinimumSize(QtCore.QSize(36, 36))
        self.label5.setMaximumSize(QtCore.QSize(36, 36))
        self.label5.setStyleSheet("border-image: url(media/stnb.svg);")
        self.label5.setText("")
        self.label5.setObjectName("label5")
        self.horizontalLayout_7.addWidget(self.label5)
        self.label_5 = QtWidgets.QLabel(self.widget5)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setScaledContents(False)
        self.label_5.setWordWrap(False)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_7.addWidget(self.label_5)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem7)
        self.verticalLayout.addWidget(self.widget5)
        self.widget7 = QtWidgets.QWidget(Form)
        self.widget7.setMinimumSize(QtCore.QSize(0, 41))
        self.widget7.setObjectName("widget7")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.widget7)
        self.horizontalLayout_10.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem8)
        self.label7 = QtWidgets.QLabel(self.widget7)
        self.label7.setMinimumSize(QtCore.QSize(36, 36))
        self.label7.setMaximumSize(QtCore.QSize(36, 36))
        self.label7.setStyleSheet("border-image: url(media/ioe.svg);")
        self.label7.setText("")
        self.label7.setObjectName("label7")
        self.horizontalLayout_10.addWidget(self.label7)
        self.label_7 = QtWidgets.QLabel(self.widget7)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setScaledContents(False)
        self.label_7.setWordWrap(False)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_10.addWidget(self.label_7)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem9)
        self.verticalLayout.addWidget(self.widget7)
        self.widget9 = QtWidgets.QWidget(Form)
        self.widget9.setMinimumSize(QtCore.QSize(0, 41))
        self.widget9.setObjectName("widget9")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.widget9)
        self.horizontalLayout_12.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem10)
        self.label9 = QtWidgets.QLabel(self.widget9)
        self.label9.setMinimumSize(QtCore.QSize(36, 36))
        self.label9.setMaximumSize(QtCore.QSize(36, 36))
        self.label9.setStyleSheet("border-image: url(media/path.svg);")
        self.label9.setText("")
        self.label9.setObjectName("label9")
        self.horizontalLayout_12.addWidget(self.label9)
        self.label_9 = QtWidgets.QLabel(self.widget9)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setScaledContents(False)
        self.label_9.setWordWrap(False)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_12.addWidget(self.label_9)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem11)
        self.verticalLayout.addWidget(self.widget9)
        self.widget11 = QtWidgets.QWidget(Form)
        self.widget11.setMinimumSize(QtCore.QSize(0, 41))
        self.widget11.setObjectName("widget11")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.widget11)
        self.horizontalLayout_13.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem12)
        self.label11 = QtWidgets.QLabel(self.widget11)
        self.label11.setMinimumSize(QtCore.QSize(36, 36))
        self.label11.setMaximumSize(QtCore.QSize(36, 36))
        self.label11.setStyleSheet("border-image: url(media/rqp.svg);")
        self.label11.setText("")
        self.label11.setObjectName("label11")
        self.horizontalLayout_13.addWidget(self.label11)
        self.label_11 = QtWidgets.QLabel(self.widget11)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_11.setFont(font)
        self.label_11.setScaledContents(False)
        self.label_11.setWordWrap(False)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_13.addWidget(self.label_11)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem13)
        self.verticalLayout.addWidget(self.widget11)
        self.widget13 = QtWidgets.QWidget(Form)
        self.widget13.setMinimumSize(QtCore.QSize(0, 41))
        self.widget13.setObjectName("widget13")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.widget13)
        self.horizontalLayout_15.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem14)
        self.label13 = QtWidgets.QLabel(self.widget13)
        self.label13.setMinimumSize(QtCore.QSize(36, 36))
        self.label13.setMaximumSize(QtCore.QSize(36, 36))
        self.label13.setStyleSheet("border-image: url(media/pb.svg);")
        self.label13.setText("")
        self.label13.setObjectName("label13")
        self.horizontalLayout_15.addWidget(self.label13)
        self.label_13 = QtWidgets.QLabel(self.widget13)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_13.setFont(font)
        self.label_13.setScaledContents(False)
        self.label_13.setWordWrap(False)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_15.addWidget(self.label_13)
        self.label__13 = QtWidgets.QLabel(self.widget13)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label__13.setFont(font)
        self.label__13.setText("148")
        self.label__13.setScaledContents(False)
        self.label__13.setWordWrap(False)
        self.label__13.setObjectName("label__13")
        self.horizontalLayout_15.addWidget(self.label__13)
        self.label___13 = QtWidgets.QLabel(self.widget13)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label___13.setFont(font)
        self.label___13.setScaledContents(False)
        self.label___13.setWordWrap(False)
        self.label___13.setObjectName("label___13")
        self.horizontalLayout_15.addWidget(self.label___13)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem15)
        self.verticalLayout.addWidget(self.widget13)
        self.widget14 = QtWidgets.QWidget(Form)
        self.widget14.setMinimumSize(QtCore.QSize(0, 41))
        self.widget14.setObjectName("widget14")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.widget14)
        self.horizontalLayout_16.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem16)
        self.label14 = QtWidgets.QLabel(self.widget14)
        self.label14.setMinimumSize(QtCore.QSize(36, 36))
        self.label14.setMaximumSize(QtCore.QSize(36, 36))
        self.label14.setStyleSheet("border-image: url(media/pb.svg);")
        self.label14.setText("")
        self.label14.setObjectName("label14")
        self.horizontalLayout_16.addWidget(self.label14)
        self.label_14 = QtWidgets.QLabel(self.widget14)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_14.setFont(font)
        self.label_14.setScaledContents(False)
        self.label_14.setWordWrap(False)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_16.addWidget(self.label_14)
        self.label__14 = QtWidgets.QLabel(self.widget14)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label__14.setFont(font)
        self.label__14.setText("148")
        self.label__14.setScaledContents(False)
        self.label__14.setWordWrap(False)
        self.label__14.setObjectName("label__14")
        self.horizontalLayout_16.addWidget(self.label__14)
        self.label___14 = QtWidgets.QLabel(self.widget14)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label___14.setFont(font)
        self.label___14.setScaledContents(False)
        self.label___14.setWordWrap(False)
        self.label___14.setObjectName("label___14")
        self.horizontalLayout_16.addWidget(self.label___14)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem17)
        self.verticalLayout.addWidget(self.widget14)
        self.widget15 = QtWidgets.QWidget(Form)
        self.widget15.setMinimumSize(QtCore.QSize(0, 41))
        self.widget15.setObjectName("widget15")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.widget15)
        self.horizontalLayout_17.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem18)
        self.label15 = QtWidgets.QLabel(self.widget15)
        self.label15.setMinimumSize(QtCore.QSize(36, 36))
        self.label15.setMaximumSize(QtCore.QSize(36, 36))
        self.label15.setStyleSheet("border-image: url(media/pb.svg);")
        self.label15.setText("")
        self.label15.setObjectName("label15")
        self.horizontalLayout_17.addWidget(self.label15)
        self.label_15 = QtWidgets.QLabel(self.widget15)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_15.setFont(font)
        self.label_15.setScaledContents(False)
        self.label_15.setWordWrap(False)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_17.addWidget(self.label_15)
        self.label__15 = QtWidgets.QLabel(self.widget15)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label__15.setFont(font)
        self.label__15.setText("148")
        self.label__15.setScaledContents(False)
        self.label__15.setWordWrap(False)
        self.label__15.setObjectName("label__15")
        self.horizontalLayout_17.addWidget(self.label__15)
        self.label___15 = QtWidgets.QLabel(self.widget15)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label___15.setFont(font)
        self.label___15.setScaledContents(False)
        self.label___15.setWordWrap(False)
        self.label___15.setObjectName("label___15")
        self.horizontalLayout_17.addWidget(self.label___15)
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem19)
        self.verticalLayout.addWidget(self.widget15)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setMinimumSize(QtCore.QSize(0, 41))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem20 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem20)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setMinimumSize(QtCore.QSize(271, 41))
        self.pushButton.setMaximumSize(QtCore.QSize(271, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setMouseTracking(False)
        self.pushButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pushButton.setStyleSheet("border-image: url(media/button.png);\n"
"font: 16pt \"黑体\";\n"
"color:white;font: bold;")
        self.pushButton.setAutoDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem21 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem21)
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(Form.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "关于"))
        self.label_race_label_3.setText(_translate("Form", "恭喜打破："))
        self.label.setText(_translate("Form", "模式："))
        self.label_16.setText(_translate("Form", "未标雷（标准）"))
        self.label_1.setText(_translate("Form", "Time成绩！"))
        self.label_3.setText(_translate("Form", "3BV/s成绩！"))
        self.label_5.setText(_translate("Form", "STNB成绩！"))
        self.label_7.setText(_translate("Form", "IOE成绩！"))
        self.label_9.setText(_translate("Form", "Path成绩！"))
        self.label_11.setText(_translate("Form", "RQP成绩！"))
        self.label_13.setText(_translate("Form", "初级"))
        self.label___13.setText(_translate("Form", "个人最佳！"))
        self.label_14.setText(_translate("Form", "中级"))
        self.label___14.setText(_translate("Form", "个人最佳！"))
        self.label_15.setText(_translate("Form", "高级"))
        self.label___15.setText(_translate("Form", "个人最佳！"))
        self.pushButton.setText(_translate("Form", "确定"))
        self.pushButton.setShortcut(_translate("Form", "Space"))
