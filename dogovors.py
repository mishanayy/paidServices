from PySide2.QtWidgets import QMainWindow, QDialog

from dogovorsWindow import Ui_Dialog_Dogovors

"""
##### Диалоговое окно Договоры (список имеющихся договоров)
"""
class OpenDogovorsWindow(Ui_Dialog_Dogovors, QMainWindow):
    def help_window(self):
        widget = QDialog(self)
        ui = Ui_Dialog_Dogovors()
        ui.setupUi(widget)
        self.show()
        widget.exec_()