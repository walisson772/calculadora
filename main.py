import sys
from window import MainWindow
from display import Display
from info import Info
from PySide6.QtWidgets import QApplication, QLabel
from buttons import Button
# from styles import setupTheme
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    # setupTheme()
    window = MainWindow()

    # Info
    info = Info('2.0 ^ 10.0 = 1024')
    window.addToVLayout(info)

    # Display
    display = Display()
    window.addToVLayout(display)

    button = Button('Texto do botão')
    window.addToVLayout(button)
    button2 = Button('Texto do botão')
    window.addToVLayout(button2)

    # Executa tudo
    window.adjustFixedSize()
    window.show()
    app.exec()