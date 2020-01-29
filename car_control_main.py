import sys
from PyQt5 import QtWidgets
from siul1024.control_tool_ui import ControlToolUi


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = ControlToolUi()
    w.ui.show()
    sys.exit(app.exec_())
