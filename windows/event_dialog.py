from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QPushButton

class EventDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Event Dialog")
        layout = QVBoxLayout()
        self.phone_input = QLineEdit()
        layout.addWidget(self.phone_input)
        self.ok_button = QPushButton("OK")
        layout.addWidget(self.ok_button)
        self.setLayout(layout)
        self.ok_button.clicked.connect(self.accept)
