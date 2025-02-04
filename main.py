import sys
from window import MainWindow
from display import Display
from info import Info
from PySide6.QtWidgets import QApplication, QLabel
from buttons import Button, ButtonsGrid
# from styles import setupTheme
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    # setupTheme()
    window = MainWindow()

    # Info
    info = Info('2.0 ^ 10.0 = 1024')
    window.addToWidgetVLayout(info)

    # Display
    display = Display()
    window.addToWidgetVLayout(display)

    # Grid
    buttonsgrid = ButtonsGrid(display)
    window.vLayout.addLayout(buttonsgrid)



    # Executa tudo
    window.adjustFixedSize()
    window.show()
    app.exec()