##
# @brief Import a GUI file made with QT Designer and add some logic. The .ui file is imported instead converting it with pyuic5 or PySide

# Import declarations
from PyQt5.QtWidgets import QApplication
from classes.interface import UI

# Main entry point
if __name__ == "__main__":
    app = QApplication([])
    window = UI()
    window.show()
    app.exec_()