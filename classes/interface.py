# This module loads the inteface and provides the logic.
# The .ui file is imported instead converting it with pyuic5 or PySide.
# If you modify the .ui file in Qt Designer, there's no need to convert it.

from PyQt5 import uic
from PyQt5.QtWidgets import (QMainWindow, QPushButton,
                             QSlider, QLabel)

# main class for the application
class UI(QMainWindow):
    def __init__(self):
        # catching global variables from outer scope
        global sliders
        global label
        # parent class init
        super().__init__()

        # this code loads the ui file
        uic.loadUi("testwindow.ui", self)

        # get the button element from UI file
        button = self.findChild(QPushButton, 'printButton')
        # get the sliders from UI file
        slider_1 = self.findChild(QSlider, 'verticalSlider')
        slider_2 = self.findChild(QSlider, 'verticalSlider_2')
        slider_3 = self.findChild(QSlider, 'verticalSlider_3')
        # get the label and set it to an empty string
        label = self.findChild(QLabel, 'label')
        label.setText("Get values...")
        # initialize sliders to 0
        slider_1.setValue(0)
        slider_2.setValue(0)
        slider_3.setValue(0)
        # define an array of sliders
        sliders = [slider_1, slider_2, slider_3]
        # connect the clicked event to click_btn method
        button.clicked.connect(self.click_btn)

    ## click_btn method
    def click_btn(self):
        # catch global var sliders
        global sliders
        value = ""
        for sld in sliders:
            val = sld.value()
            value += str(val) + " + "
        print("button clicked")
        # strip the unnecessary 2 chars at the end
        value = value[:-2]
        self.label.setText(value)