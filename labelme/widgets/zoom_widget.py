from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets


class ZoomWidget(QtWidgets.QSpinBox):
    def __init__(self, value=100, max_zoom=5000):
        super().__init__()
        self.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        # Configurable max zoom for tiny defect annotation (default 5000% = 50x)
        self.setRange(1, max_zoom)
        self.setSuffix(" %")
        self.setValue(value)
        self.setToolTip("Zoom Level")
        self.setStatusTip(self.toolTip())
        self.setAlignment(QtCore.Qt.AlignCenter)

    def minimumSizeHint(self):
        height = super().minimumSizeHint().height()
        fm = QtGui.QFontMetrics(self.font())
        width = fm.width(str(self.maximum()))
        return QtCore.QSize(width, height)
