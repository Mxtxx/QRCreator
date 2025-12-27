"""
QR Code Generator Application

A simple GUI application that allows users to create customizable QR codes
with options for colors, rounded corners, and logo overlay.
"""

from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QFileDialog
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
        self.current_qr_image = None #to store the current QR code image
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

        

        #create the generate QR code button and connect it to the generate_qr_code method
        self.generate_button = QPushButton("Generate QR Code")
        self.generate_button.clicked.connect(self.generate_qr)
        layout.addWidget(self.generate_button) 

        #Preview the QR code
        self.preview_label = QLabel()
        self.preview_label.setAlignment(Qt.AlignCenter) 
        self.preview_label.setMinimumSize(300, 300)
        layout.addWidget(self.preview_label)
        
        #set the layout for the window
        self.setLayout(layout)

        #add a save button to the window
        self.save_button = QPushButton("Save QR Code")
        self.save_button.clicked.connect(self.save_qr)
        layout.addWidget(self.save_button)

    def generate_qr(self):
        """
        Generate the QR code from the text input field and display it in the preview label.
    
        Called when the generate button is clicked.
        """
        #get the text from the text input field and check if it is empty
        text = self.text_input.text()
        if not text:
            return

        #generate the QR code using the generate_qr_code function from the qr module
        qr_image = generate_qr_code(text)

        #store the current QR code image
        self.current_qr_image = qr_image

        #convert the PIL image to a QPixmap for display in the preview label 
        # since PySide 6 doesn't support PIL images directly
        qr_image = qr_image.convert("RGBA")
        data = qr_image.tobytes("raw", "RGBA")
        qt_image = QImage(data, qr_image.width, qr_image.height, QImage.Format_RGBA8888)
        pixmap = QPixmap.fromImage(qt_image)

        #display the QR code in the preview label
        self.preview_label.setPixmap(pixmap)

    def save_qr(self):
        """
        Save the current QR code image to a file.

        Opens a file dialog for the user to choose the save location and filename.
        """

        if self.current_qr_image is None:
            return
        
        #open a file dialog for the user to choose the save location and filename
        file_path, _ = QFileDialog.getSaveFileName(
            self, "Save QR Code", "qr_code.png", "PNG Files (*.png);;JPEG Files (*.jpg)")

        #if the user cancels the dialog, return
        if not file_path:
            return



    

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

