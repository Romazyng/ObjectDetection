from PyQt5 import QtCore, QtGui, QtWidgets
from test import PowerBar


app = QtWidgets.QApplication([])
volume = PowerBar()
volume.show()
app.exec_()