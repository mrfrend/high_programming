from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QFrame, QLabel, QVBoxLayout
from PyQt6.QtCore import Qt, pyqtSignal
from py_ui.company_card import Ui_Frame


class CompanyCard(Ui_Frame, QFrame):
	clicked = pyqtSignal(dict)
	def __init__(self, company):
		super().__init__()
		self.setupUi(self)
		self.company = company
		self.setup_ui()

	def mousePressEvent(self, a0) -> None:
		self.clicked.emit(self.company)
		super().mousePressEvent(a0)
