from PySide6.QtWidgets import QLineEdit
from variables import BIG_FONTE_SIZE, TEXT_MARGIN, MINIMUM_WIDTH
from  PySide6.QtCore import Qt

class Display(QLineEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        margins = [TEXT_MARGIN for _ in range(4)]
        self.setStyleSheet(f'fonte-size: {BIG_FONTE_SIZE}px')
        self.setMinimumHeight(BIG_FONTE_SIZE * 2)
        self.setMinimumWidth(MINIMUM_WIDTH)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setTextMargins(*margins)