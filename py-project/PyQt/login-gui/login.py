# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(953, 705)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(11, 11, 258, 297))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.username = QtWidgets.QLabel(self.widget)
        self.username.setObjectName("username")
        self.gridLayout.addWidget(self.username, 0, 0, 1, 1)
        self.username_input = QtWidgets.QLineEdit(self.widget)
        self.username_input.setObjectName("username_input")
        self.gridLayout.addWidget(self.username_input, 0, 1, 1, 1)
        self.password = QtWidgets.QLabel(self.widget)
        self.password.setObjectName("password")
        self.gridLayout.addWidget(self.password, 1, 0, 1, 1)
        self.password_input = QtWidgets.QLineEdit(self.widget)
        self.password_input.setObjectName("password_input")
        self.gridLayout.addWidget(self.password_input, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.logout = QtWidgets.QPushButton(self.widget)
        self.logout.setObjectName("logout")
        self.horizontalLayout.addWidget(self.logout)
        self.login = QtWidgets.QPushButton(self.widget)
        self.login.setObjectName("login")
        self.horizontalLayout.addWidget(self.login)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.result_show = QtWidgets.QTextBrowser(self.widget)
        self.result_show.setObjectName("result_show")
        self.verticalLayout_2.addWidget(self.result_show)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.username.setText(_translate("Form", "用户名"))
        self.password.setText(_translate("Form", "密码"))
        self.logout.setText(_translate("Form", "退出"))
        self.login.setText(_translate("Form", "登录"))