from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QGridLayout, QVBoxLayout, QWidget, QLineEdit

from database.database import db
from windows.company_card import CompanyCard
from py_ui.main_window import Ui_Form


class MainWindow(QWidget, Ui_Form):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.load_companies()
		self.searchEdit.textChanged.connect(self.load_companies)

	def load_companies(self):
		while self.companies_layout.count() > 0:
			widget = self.companies_layout.takeAt(0).widget()
			if widget:
				widget.deleteLater()
		
		self.companies_layout.setColumnStretch(0, 1)
		self.companies_layout.setColumnStretch(1, 1)
		
		search_text = self.searchEdit.text().strip() or None
		companies = db.get_companies(search_text)
		i = 0
		for company in companies:
			card = CompanyCard(company)
			row = i // 2
			col = i % 2
			self.companies_layout.addWidget(card, row, col)
			card.clicked.connect(self.on_company_clicked)

			i += 1

	def on_company_clicked(self, company):
		print(company)
