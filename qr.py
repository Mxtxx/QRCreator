"""
QR Code Generator Module

This module provides functionality to generate QR codes from text.
It uses the qrcode library to create QR code images and the PIL library to save them.
"""

import qrcode
from PIL import Image, ImageDraw

def generate_qr_code(text:str, fg_color:str = "#000000", bg_color:str = "#FFFFFF", error_level:str = "L", box_size:int = 10, rounded:bool = False):
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


    #create the rounded QR code if the rounded checkbox is checked
    if rounded:
        qr_image = create_rounded_qr(qr, fg_color, bg_color, box_size)
    else:
        qr_image = qr.make_image(fill_color=fg_color, back_color=bg_color)
    return qr_image

def create_rounded_qr(qr, fg_color:str, bg_color:str, box_size:int):
    """
    Create a rounded QR code image from the given QR code object.

    For this part, Claude AI was used to help me create the rounded QR code with the mathematical formulas and logic.
    """

    #get the size of the QR code
    matrix = qr.get_matrix()

    #calculate the image size
    module_count = len(matrix)
    border = 4
    image_size = (module_count + border * 2) * box_size

    #create the image with blank 
    image = Image.new("RGBA", (image_size, image_size), bg_color)
    draw = ImageDraw.Draw(image)

    radius = box_size / 2

    #draw the rounded corners modules
    for row_index in enumerate(matrix):
        for col_index, isfilled in enumerate(row):
            if isfilled:
                #calculate the position of the module
                x = (col_index + border) * box_size
                y = (row_index + border) * box_size

                #draw the rounded corner module
                draw.rounded_rectangle([x, y, x + box_size, y + box_size], radius, fill=fg_color)
    return image
    



