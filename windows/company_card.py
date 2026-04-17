from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QFrame
from PyQt6.QtCore import pyqtSignal
from py_ui.company_card import Ui_Frame


class CompanyCard(Ui_Frame, QFrame):
	clicked = pyqtSignal(dict)
	def __init__(self, company):
		super().__init__()
		self.setupUi(self)
		self.company = company
		
		self.name.setText(self.company["name"])
		self.contribution.setText(f"Взнос {self.company['contribution_price']} р.")
		pixmap = QPixmap(f"images/{self.company['logo']}").scaled(100, 100)
		self.image.setPixmap(pixmap)

	def mousePressEvent(self, a0) -> None:
		self.clicked.emit(self.company)
		super().mousePressEvent(a0)
