from PySide6.QtWidgets import QPushButton, QGridLayout
from variables import MEDIUM_FONTE_SIZE
import re
from display import Display


NUM_OR_DOT_REGEX = re.compile(r'^[0-9.]$')
def isNumOrDot(string: str):
    return bool(NUM_OR_DOT_REGEX.search(string))

def isValidNumber(string: str):
    valid = False 
    try:
        float(string)
        valid = True

    except ValueError:
        valid = False

    return valid

def isEmpty(string: str):
    return len(string) == 0


class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        font = self.font()
        font.setPixelSize(MEDIUM_FONTE_SIZE)
        self.setFont(font)
        self.setMinimumSize(50, 50)

class ButtonsGrid(QGridLayout):
    def __init__(self, display: Display,*args, **kwargs):
        super().__init__(*args, **kwargs)

        self._gridMask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['',  '0', '.', '='],
        ]
        self.display = display
        self._makeGrid()

    def _makeGrid(self):
        for rowNumber, rowdata in  enumerate(self._gridMask):
            for columNuber, buttonText in enumerate(rowdata):
                button = Button(buttonText)
                self.addWidget(button, rowNumber, columNuber)
                buttonSlot = self._makeSlot(self._insertButton, button)
                button.clicked.connect(buttonSlot)

    def _makeSlot(self, func, *args, **kwargs):
        
        def realSlot(_):
            func(*args, **kwargs)
        return realSlot

    def _insertButton(self, button):
        buttonText = button.text()

        newDisplayValue = self.display.text() + buttonText

        if not isValidNumber(newDisplayValue):
            return

        self.display.insert(buttonText)