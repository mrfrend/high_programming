from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QGridLayout, QVBoxLayout, QWidget, QLineEdit

from database.database import db
from windows.company_card import CompanyCard


class MainWindow(QWidget):
	def __init__(self):
		super().__init__()
		self.setup_ui()
		self.load_companies()

	def load_companies(self):
		while self.companies_layout.count() > 0:
			widget = self.companies_layout.takeAt(0).widget()
			if widget:
				widget.deleteLater()

		companies = db.get_companies()
		i = 0
		for company in companies:
			card = CompanyCard(company)
			row = i // 2
			col = i % 2
			self.companies_layout.addWidget(card, row, col, Qt.AlignmentFlag.AlignHCenter)
			card.clicked.connect(self.on_company_clicked)

			i += 1

	def setup_ui(self):
		self.main_layout = QVBoxLayout()
		self.companies_layout = QGridLayout()
		self.searchEdit = QLineEdit()
		self.main_layout.addWidget(self.searchEdit)
		self.main_layout.addLayout(self.companies_layout)
		self.setLayout(self.main_layout)

	def on_company_clicked(self, company):
		print(company)
