from tools.qrcode import QRCode
from tools.barcode import Barcode 

# Example usage
# try:
#     sqrcode = QRCode()
#     result = qrcode.generate_qrcode(data='https://www.thepythoncode.com', logo_path='logo.png', save_as_png=False)
#     print(result)
# except ValueError as e:
#     print(e)

# Example usage
try:
    barcode = Barcode()
    result = barcode.generate_barcode(data='123456789012', logo_path='logo.png', save_as_png=True)
    print(result)
except ValueError as e:
    print(e)
