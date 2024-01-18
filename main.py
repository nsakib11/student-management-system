from PyQt6.QtWidgets import QApplication, QLabel, QWidget, \
    QLineEdit, QGridLayout, QPushButton, QMainWindow
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Management System")


app = QApplication(sys.argv)
age_calculator = MainWindow()
age_calculator.show()
sys.exit(app.exec())