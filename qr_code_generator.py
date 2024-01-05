"""
QR Code Generator from a given input string.
"""
import os

import qrcode


class QRGenerator:
    def __init__(self, size: int, padding: int):
        self.qr = qrcode.QRCode(box_size=size, border=padding)

    def generate(self, data: str, file_name: str, fg: str, bg: str) -> None:
        """
        Generate QR Code from given data and save it as a PNG file.
        """
        os.makedirs('artifacts', exist_ok=True)
        file_path = os.path.join('artifacts', file_name)
        try:
            self.qr.add_data(data)
            self.qr.make(fit=True)
            img = self.qr.make_image(fill_color=fg, back_color=bg)
            img.save(file_path)

            print(f"QR Code generated successfully as {file_name}")
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    qr = QRGenerator(10, 5)
    user_input = input("Enter the data to be converted to the QR: ")
    qr.generate(user_input, "qr.png", "black", "white")
