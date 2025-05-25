from PyQt5 import QtCore, QtWidgets

class Ui_MyFirstPluginDialog(object):
    def setupUi(self, MyFirstPluginDialog):
        MyFirstPluginDialog.setObjectName("MyFirstPluginDialog")
        MyFirstPluginDialog.resize(300, 200)

        self.firstNameLabel = QtWidgets.QLabel(MyFirstPluginDialog)
        self.firstNameLabel.setGeometry(QtCore.QRect(20, 20, 80, 25))
        self.firstNameLabel.setText("First Name:")
        self.firstNameInput = QtWidgets.QLineEdit(MyFirstPluginDialog)
        self.firstNameInput.setGeometry(QtCore.QRect(100, 20, 160, 25))

        self.lastNameLabel = QtWidgets.QLabel(MyFirstPluginDialog)
        self.lastNameLabel.setGeometry(QtCore.QRect(20, 60, 80, 25))
        self.lastNameLabel.setText("Last Name:")
        self.lastNameInput = QtWidgets.QLineEdit(MyFirstPluginDialog)
        self.lastNameInput.setGeometry(QtCore.QRect(100, 60, 160, 25))

        self.emailLabel = QtWidgets.QLabel(MyFirstPluginDialog)
        self.emailLabel.setGeometry(QtCore.QRect(20, 100, 80, 25))
        self.emailLabel.setText("Email:")
        self.emailInput = QtWidgets.QLineEdit(MyFirstPluginDialog)
        self.emailInput.setGeometry(QtCore.QRect(100, 100, 160, 25))

        self.submitButton = QtWidgets.QPushButton(MyFirstPluginDialog)
        self.submitButton.setGeometry(QtCore.QRect(100, 140, 100, 30))
        self.submitButton.setObjectName("submitButton")

        self.retranslateUi(MyFirstPluginDialog)
        QtCore.QMetaObject.connectSlotsByName(MyFirstPluginDialog)

    def retranslateUi(self, MyFirstPluginDialog):
        _translate = QtCore.QCoreApplication.translate
        MyFirstPluginDialog.setWindowTitle(_translate("MyFirstPluginDialog", "User Form"))
        self.submitButton.setText(_translate("MyFirstPluginDialog", "Submit"))
