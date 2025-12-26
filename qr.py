"""
QR Code Generator Module

This module provides functionality to generate QR codes from text.
It uses the qrcode library to create QR code images and the PIL library to save them.
"""

import qrcode
from PIL import Image

def generate_qr_code(text:str):
    """
    Generate a QR code image from the given text.

    Args:
        text (str): The content to encode in the QR code (URL, text, etc.)
    
    Returns:
        A PIL Image object containing the generated QR code.
    """
    #create the default QR code object with default settings
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L, #low error correction level
        box_size=10,
        border=4,
    )

    #add the text data to the QR code
    qr.add_data(text)
    qr.make(fit=True) #autoadjust the size of the QR code to fit the data even if it is large

    #create and return the image
    qr_image = qr.make_image(fill_color="black", back_color="white")
    return qr_image


