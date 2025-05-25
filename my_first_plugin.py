from qgis.PyQt.QtWidgets import QAction
from qgis.PyQt.QtGui import QIcon
from .my_first_plugin_dialog import MyFirstPluginDialog

class MyFirstPlugin:
    def __init__(self, iface):
        self.iface = iface
        self.action = None
        self.dialog = None

    def initGui(self):
        self.action = QAction("Open My Plugin", self.iface.mainWindow())
        self.action.triggered.connect(self.run)
        self.iface.addPluginToMenu("&My Plugins", self.action)
        self.iface.addToolBarIcon(self.action)

    def unload(self):
        self.iface.removePluginMenu("&My Plugins", self.action)
        self.iface.removeToolBarIcon(self.action)

    def run(self):
        if not self.dialog:
            self.dialog = MyFirstPluginDialog()
        self.dialog.show()
