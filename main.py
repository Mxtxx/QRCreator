"""
QR Code Generator Application

A simple GUI application that allows users to create customizable QR codes
with options for colors, rounded corners, and logo overlay.
"""

from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtCore import Qt
from qr import generate_qr_code


class QRCodeGenerator(QWidget):
    """
    Main window for the QR Code Generator application.

    This class handles the main window and the user interface.
    
    """
    
    def __init__(self):
        """Initialize the window and set up the UI."""
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        """
        Initialize the main window properties and layout.
        
        This method sets the window title, geometry, and initializes the UI components.
        """
        self.setWindowTitle("QR Code Generator")
        self.setGeometry(100, 100, 800, 600)

        #create the layout for the window
        layout = QVBoxLayout()

        #create the text input field
        self.text_input = QLineEdit()
        self.text_input.setPlaceholderText("Enter the text to convert to QR code")
        layout.addWidget(self.text_input)

        self.setLayout(layout)

        #create the generate QR code button
        self.generate_button = QPushButton("Generate QR Code")
        layout.addWidget(self.generate_button)

        #Preview the QR code
        self.preview_label = QLabel()
        self.preview_label.setAlignment(Qt.AlignCenter) 
        self.preview_label.setMinimumSize(300, 300)
        layout.addWidget(self.preview_label)
        # UI components will be added here.

def main():
    """Entry point of the application.
    
    Here the QApplication is created and the main window is shown.
    """
    app = QApplication([])
    window = QRCodeGenerator()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()

