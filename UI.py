import os
import sys
import tempfile
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QFileDialog, QMessageBox
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt
from fpdf import FPDF
from urllib.request import urlretrieve


class ImageToPdfConverter(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image to PDF Converter")
        self.setFixedSize(600, 600)

        # Create a label to display the dropped image
        self.image_label = QLabel(self)
        self.image_label.setGeometry(10, 10, 580, 380)
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setStyleSheet("border: 1px solid gray;")

        # Create a button to start the conversion process
        self.convert_button = QPushButton("Convert to PDF", self)
        self.convert_button.setGeometry(240, 420, 120, 30)
        self.convert_button.setEnabled(False)
        self.convert_button.clicked.connect(self.convert_image_to_pdf)

        # Create a label to display the status of the conversion
        self.status_label = QLabel(self)
        self.status_label.setGeometry(10, 480, 580, 30)
        self.status_label.setAlignment(Qt.AlignCenter)
        self.status_label.setStyleSheet("font-weight: bold;")

        # Create a label to display the download link for the PDF file
        self.download_label = QLabel(self)
        self.download_label.setGeometry(10, 520, 580, 30)
        self.download_label.setAlignment(Qt.AlignCenter)
        self.download_label.setOpenExternalLinks(True)

        # Enable drag and drop
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        # Allow the user to drag and drop an image file onto the GUI
        if event.mimeData().hasUrls():
            for url in event.mimeData().urls():
                if url.isLocalFile() and url.toLocalFile().endswith(".png"):
                    event.accept()
                    return
        event.ignore()

    def dropEvent(self, event):
        # Display the dropped image in the label and enable the convert button
        url = event.mimeData().urls()[0]
        file_path = url.toLocalFile()
        pixmap = QPixmap(file_path).scaled(580, 380, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.image_label.setPixmap(pixmap)
        self.convert_button.setEnabled(True)

    def convert_image_to_pdf(self):
        # Disable the convert button to prevent multiple conversions
        self.convert_button.setEnabled(False)
        self.status_label.setText("Converting image to PDF...")

        # Get the path to the image file
        image_path = list(QFileDialog.getOpenFileNames(self, "Select Image", "", "Images (*.png)"))[0][0]

        # Create a temporary file to store the PDF
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
            pdf_path = tmp_file.name

        # Convert the image to PDF and save it to the temporary file
        pdf = FPDF(unit="pt", format=(self.width(), self.height()))
        pdf.add_page()
        pdf.image(image_path, 0, 0, self.width(), self.height)
