from windows.main_window import MainWindow
from PyQt6.QtWidgets import QApplication

if __name__ == "__main__":
	app = QApplication([])
	window = MainWindow()
	window.setup_ui()
	window.show()
	app.exec()