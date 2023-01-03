from typing import NoReturn
from pathlib import Path
import by_pandas
from PyQt6.QtWidgets import (
    QMainWindow,
    QPushButton,
    QGridLayout,
    QWidget,
    QFileDialog,
    QLineEdit,
    QLabel,
    QComboBox
)


class MainWindow(QMainWindow):
    """
    Class to create a window dialog.
    ...
    Methods
    _______
    set_window(self):
        creates window's structure
    open_csvfile_dialog(self):
        opens dialog to choose CSV file with items
    open_folder_dialog(self):
        opens dialog to choose or create folder destination to save barcode images
    create_labels(self):
        runs barcode creating function after press button
    """
    def __init__(self):
        super().__init__()
        self.set_window()

    def set_window(self) -> NoReturn:
        """Creates window's structure"""
        self.setWindowTitle("excel combiner")
        self.setGeometry(100, 100, 200, 100)
        self.setMinimumSize(300, 200)
        self.setMaximumSize(900, 600)

        self.button_folder = QPushButton('Where excel files are?')
        self.button_folder.clicked.connect(lambda: self.open_folder_dialog())
        self.label_foldername = QLineEdit()

        self.label_pattern_sheet =
        self.label_pattern_sheet = QLineEdit('Шаблон для поставщика')

        self.button_create = QPushButton('Combine!')
        self.button_create.clicked.connect(lambda: by_pandas.combine())

        container = QWidget()
        layout = QGridLayout()
        layout.addWidget(self.button_folder, 3, 0)
        layout.addWidget(self.label_foldername, 3, 1, 1, 1)
        layout.addWidget(self.label_pattern_sheet, 4, 1, 1, 1)
        layout.addWidget(self.button_create, 5, 0, 1, 2)

        container.setLayout(layout)
        self.setCentralWidget(container)

    def open_folder_dialog(self):
        """opens dialog to choose folder with Excel files"""
        excel_folder = QFileDialog.getExistingDirectory(self, 'Choose folder where excel file are')
        self.label_foldername.setText(excel_folder)
        excel_files = by_pandas.create_file_list(excel_folder)
        return excel_files
