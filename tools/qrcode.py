import qrcode
from PIL import Image
import io
import base64
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

class QRCode:
    """
    QRCodeScanner is a utility class for generating QR codes with optional embedded logos.
    It supports saving the QR code either as an image file or as a base64-encoded string in a text file.
    
    Usage:
        qrcode = QRCode)
        
        # Generate QR code and save as PNG
        qrcode.generate_qrcode(
            filename="output.png", 
            logo_path="logo.png", 
            data="https://www.example.com", 
            save_as_png=True
        )
        
        # Generate QR code and save as base64 string in a text file
        qrcode.generate_qrcode(
            filename="output.png", 
            logo_path="logo.png", 
            data="https://www.example.com", 
            save_as_png=False
        )
    """

    def generate_qrcode(self, filename=None, logo_path=None, data=None, save_as_png=True):
        if data is None:
            data = ''
        if filename is None:
            filename = "qrcode.png"

        # Check if logo_path is provided and is a PNG file
        if logo_path and not logo_path.endswith('.png'):
            raise ValueError(Fore.RED + Style.BRIGHT + 'logo_path must end with .png!')

        # Generate QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)

        # Create an image from the QR code instance
        img = qr.make_image(fill_color="black", back_color="white").convert('RGB')

        if logo_path:
            # Load the logo image
            logo = Image.open(logo_path)

            # Ensure the logo has a white background (in case of transparency)
            logo = logo.convert("RGBA")
            white_background = Image.new("RGBA", logo.size, "WHITE")
            logo = Image.alpha_composite(white_background, logo).convert("RGBA")

            # Calculate the logo size relative to the QR code
            logo_size = int(min(img.size) / 4)

            # Resize the logo
            logo = logo.resize((logo_size, logo_size))

            # Calculate the position to place the logo at the center
            logo_position = (
                (img.size[0] - logo_size) // 2,
                (img.size[1] - logo_size) // 2
            )

            # Paste the logo image onto the QR code, with a mask to handle transparency
            img.paste(logo, logo_position, mask=logo)

        if save_as_png:
            # Save the final QR code image
            img.save(filename)
            return f'QR code has been saved as {filename}'
        else:
            # Convert the image to a byte stream
            buffered = io.BytesIO()
            img.save(buffered, format="PNG")

            # Encode the byte stream to base64
            image_string = base64.b64encode(buffered.getvalue()).decode("utf-8")

            # Replace '.png' with '.txt' in the filename
            filename = filename.replace('.png', '.txt')

            # Save the base64 string to a text file
            with open(filename, "w") as text_file:
                text_file.write(image_string)

            return f'QR code string has been saved as {filename}'


