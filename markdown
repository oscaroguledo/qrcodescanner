from tools.qrcode import QRCode
from tools.barcode import Barcode

# Example usage for QR Code generation
try:
    qrcode = QRCode()
    result = qrcode.generate_qrcode(
        data='https://www.thepythoncode.com', 
        logo_path='logo.png', 
        filename='qrcode.png', 
        save_as_png=True
    )
    print(result)
except ValueError as e:
    print(f"Error: {e}")

# Example usage for QR Code scanning
try:
    qrcode = QRCode()
    result = qrcode.scan_qrcode('qrcode.png')
    print(result)
except ValueError as e:
    print(f"Error: {e}")

# Example usage for Barcode generation
try:
    barcode = Barcode()
    result = barcode.generate_barcode(
        data='123456789012', 
        logo_path='logo.png', 
        filename='barcode.png', 
        save_as_png=True
    )
    print(result)
except ValueError as e:
    print(f"Error: {e}")

# Example usage for Barcode scanning
try:
    barcode = Barcode()
    result = barcode.scan_barcode('barcode.png')
    print(result)
except ValueError as e:
    print(f"Error: {e}")
