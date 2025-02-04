from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QWidget
from variables import SMALL_FONTE_SIZE 
from PySide6.QtCore import Qt

class Info(QLabel):
    def __init__(self, text: str, parent: QWidget | None = None) -> None:
        super().__init__(text, parent)
        self.configStyle()

    def configStyle(self):
        self.setStyleSheet(f'fonte-size: {SMALL_FONTE_SIZE}px')
        self.setAlignment(Qt.AlignmentFlag.AlignRight)