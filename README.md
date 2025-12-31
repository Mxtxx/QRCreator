# QR Code Generator

A simple desktop application for creating customizable QR codes.

## Features

- Generate QR codes from any text or URL
- Customize foreground and background colors
- Adjust error correction level (L, M, Q, H)
- Adjust QR code size
- Rounded corner modules option
- Add logo overlay in the center
- Save QR codes as PNG or JPEG

## Requirements

- Python 3.x
- PySide6
- qrcode
- Pillow

## Installation

1. Clone this repository
2. Install dependencies:
pip install PySide6 qrcode Pillow

## Usage

Run the application:

python main.py


1. Enter text or URL in the input field
2. Customize colors, size, and options as desired
3. Click "Generate QR Code" to preview
4. Click "Save QR Code" to export

**Note**: When using a logo, select Q (25%) or H (30%) error correction.

## Author

Matteo Gamboni

## AI support:
Used as aid for overall structure, advisor, information source and for a more complex method in qr.py