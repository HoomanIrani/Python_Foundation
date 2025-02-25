# PyQt5 introduction
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My cool first GUI")
        self.setGeometry(700, 300, 500, 500)
        self.setWindowIcon(QIcon("PS30TH_PS1_4X3_WALLPAPER.png"))

        # Add a label to the window
        label = QLabel("Hello", self)
        label.setFont(QFont("Arial", 40))
        label.setGeometry(0, 0, 500, 100)
        label.setStyleSheet("color: #f5d65b;"
                            "background-color: #6fdcf7;"
                            "font-weight: bold;"
                            "font-style: metalic;"
                            "text-decoration: underline;")
       #label.setAlignment(Qt.AlignTop)
       #label.setAlignment(Qt.AlignBottom)
       #label.setAlignment(Qt.AlignVCenter)
       #label.setAlignment(Qt.AlignRight)
       #label.setAlignment(Qt.AlignLeft)
       #label.setAlignment(Qt.AlignHCenter)
        label.setAlignment(Qt.AlignCenter)


def main():
    # Call the constructors
    app = QApplication(sys.argv)
    window = MainWindow()  # Create an instance of your custom MainWindow class
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()