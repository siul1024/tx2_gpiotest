import sys
from PyQt5 import QtWidgets
from remote_control_key.control_tool_ui import ControlToolUi


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = ControlToolUi()
    w.ui.show()
    sys.exit(app.exec_())
