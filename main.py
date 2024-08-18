import argparse
from tools.qrcode import QRCode
from tools.barcode import Barcode

def generate_qrcode(data, logo_path=None, filename='qrcode.png', save_as_png=True):
    qr = QRCode()
    return qr.generate_qrcode(data=data, logo_path=logo_path, filename=filename, save_as_png=save_as_png)

def scan_qrcode(filename):
    qr = QRCode()
    return qr.scan_qrcode(filename)

def generate_barcode(data, logo_path=None, filename='barcode.png', save_as_png=True):
    barcode = Barcode()
    return barcode.generate_barcode(data=data, logo_path=logo_path, filename=filename, save_as_png=save_as_png)

def scan_barcode(filename):
    barcode = Barcode()
    return barcode.scan_barcode(filename)

def main():
    parser = argparse.ArgumentParser(description='Generate or scan barcodes and QR codes.')

    # Define mutually exclusive group for generate or scan
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--generate', choices=['barcode', 'qrcode'], help='Type of code to generate')
    group.add_argument('--scan', help='Path to the image file to scan')

    # Arguments for generating codes
    parser.add_argument('--data', help='Data to encode in the code')
    parser.add_argument('--logo', help='Path to the logo image to embed')
    parser.add_argument('--output', help='Output file name', default='output.png')
    parser.add_argument('--save_as_png', action='store_true', help='Save as PNG image')

    args = parser.parse_args()

    try:
        if args.generate:
            if args.generate == 'qrcode':
                if not args.data:
                    parser.error("--data is required when generating a QR code")
                result = generate_qrcode(
                    data=args.data, 
                    logo_path=args.logo, 
                    filename=args.output, 
                    save_as_png=args.save_as_png
                )
                print(result)
            elif args.generate == 'barcode':
                if not args.data:
                    parser.error("--data is required when generating a barcode")
                result = generate_barcode(
                    data=args.data, 
                    logo_path=args.logo, 
                    filename=args.output, 
                    save_as_png=args.save_as_png
                )
                print(result)
        elif args.scan:
            if args.output.endswith('.png'):
                if 'barcode' in args.scan:
                    result = scan_barcode(args.scan)
                else:
                    result = scan_qrcode(args.scan)
            else:
                parser.error("Scanning only supports PNG files")
            print(result)
        else:
            print("Please specify either --generate or --scan.")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()
