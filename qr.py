"""
QR Code Generator Module

This module provides functionality to generate QR codes from text.
It uses the qrcode library to create QR code images and the PIL library to save them.
"""

import qrcode
from PIL import Image

def generate_qr_code(text:str, fg_color:str = "#000000", bg_color:str = "#FFFFFF", error_level:str = "L", box_size:int = 10):
    """
    Generate a QR code image from the given text.

    Args:
        text (str): The content to encode in the QR code (URL, text, etc.)
        fg_color (str): The color of the QR code (default is black)
        bg_color (str): The color of the QR code background (default is white)
    
    Returns:
        A PIL Image object containing the generated QR code.
    """

    #map the error correction level to the qrcode constants
    error_levels = {
        "L": qrcode.constants.ERROR_CORRECT_L,
        "M": qrcode.constants.ERROR_CORRECT_M,
        "Q": qrcode.constants.ERROR_CORRECT_Q,
        "H": qrcode.constants.ERROR_CORRECT_H,
    }

    #create the default QR code object with default settings
    qr = qrcode.QRCode(
        version=1,
        error_correction=error_levels.get(error_level, qrcode.constants.ERROR_CORRECT_L),
        box_size=box_size,
        border=4,
    )

    #add the text data to the QR code
    qr.add_data(text)
    qr.make(fit=True) #autoadjust the size of the QR code to fit the data even if it is large

    #create and return the image
    qr_image = qr.make_image(fill_color=fg_color, back_color=bg_color)
    return qr_image


