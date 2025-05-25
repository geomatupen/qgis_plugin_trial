from qgis.PyQt.QtWidgets import QDialog, QMessageBox
from .my_first_plugin_dialog_base import Ui_MyFirstPluginDialog

class MyFirstPluginDialog(QDialog, Ui_MyFirstPluginDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.submitButton.clicked.connect(self.on_submit)

    def on_submit(self):
        first_name = self.firstNameInput.text()
        last_name = self.lastNameInput.text()
        email = self.emailInput.text()

        message = f"First Name: {first_name}\nLast Name: {last_name}\nEmail: {email}"
        QMessageBox.information(self, "Form Submitted", message)
