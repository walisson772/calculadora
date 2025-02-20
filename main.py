import sys
from window import Window
from display import Display
from info import Info
from PySide6.QtWidgets import QApplication, QLabel
from buttons import Button, ButtonsGrid
# from styles import setupTheme
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    # setupTheme()
    window = Window()

    # Info
    info = Info('Sua conta')
    window.addToWidgetVLayout(info)

    # Display
    display = Display()
    window.addToWidgetVLayout(display)

    # Grid
    buttonsgrid = ButtonsGrid(display, info, window)
    window.vLayout.addLayout(buttonsgrid)



    # Executa tudo
    window.adjustFixedSize()
    window.show()
    app.exec()