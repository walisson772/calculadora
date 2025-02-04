from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)
        # Configurando o layout básico
        self.cw = QWidget()
        self.vLayout = QVBoxLayout()
        self.cw.setLayout(self.vLayout)
        self.setCentralWidget(self.cw)
        # Título da janela
        self.setWindowTitle('Calculadora')

    def adjustFixedSize(self):
        # Ultima coisa a ser feita
        self.adjustSize()
        
    
    def addToVLayout(self, widget: QWidget):
        self.vLayout.addWidget(widget)
        self.adjustFixedSize()  
