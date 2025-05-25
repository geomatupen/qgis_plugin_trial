def classFactory(iface):
    from .my_first_plugin import MyFirstPlugin
    return MyFirstPlugin(iface)
