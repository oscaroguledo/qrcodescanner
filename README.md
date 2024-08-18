# Barcode and QR Code Generators

This repository provides two utility classes for generating barcodes and QR codes. Both classes support embedding a logo into the generated image and offer the ability to save the output either as an image file or as a base64-encoded string in a text file.

## Classes

### BarcodeGenerator

The `BarcodeGenerator` class allows you to generate barcodes with optional embedding of a logo. It supports saving the barcode either as an image file or as a base64-encoded string.

#### Usage

```python
from barcode_generator import BarcodeGenerator  # Adjust the import according to your file structure

# Create an instance of BarcodeGenerator
generator = BarcodeGenerator()

# Generate a barcode and save as a PNG file
result = generator.generate_barcode(
    filename="barcode.png",
    logo_path="logo.png",
    data="123456789012",
    save_as_png=True
)
print(result)  # Output: Barcode has been saved as barcode.png

# Generate a barcode and save as a base64 string in a text file
result = generator.generate_barcode(
    filename="barcode.png",
    logo_path="logo.png",
    data="123456789012",
    save_as_png=False
)
print(result)  # Output: Barcode string has been saved as barcode.txt
