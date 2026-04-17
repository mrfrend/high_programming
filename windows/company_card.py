from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QFrame, QLabel, QVBoxLayout
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtWidgets import QSizePolicy


class CompanyCard(QFrame):
	clicked = pyqtSignal(dict)
	def __init__(self, company):
		super().__init__()
		self.company = company
		self.setup_ui()

	def setup_ui(self):
		self.setFrameStyle(QFrame.Shape.Box | QFrame.Shadow.Plain)
		layout = QVBoxLayout()
		name_label = QLabel(self.company["name"])
		name_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
		layout.addWidget(name_label)

		image_label = QLabel()
		pixmap = QPixmap(f"images/{self.company['logo']}").scaled(100, 100)
		image_label.setPixmap(pixmap)

		layout.addWidget(image_label)

		contribution_label = QLabel(f" Взнос {self.company['contribution_price']} р.")
		contribution_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
		layout.addWidget(contribution_label)

		self.setLayout(layout)
	
	def mousePressEvent(self, a0) -> None:
		self.clicked.emit(self.company)
		super().mousePressEvent(a0)
