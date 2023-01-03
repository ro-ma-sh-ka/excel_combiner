import by_pandas
from window import MainWindow
from PyQt6.QtWidgets import QApplication


app = QApplication([])
window = MainWindow()
window.show()
exit(app.exec())
