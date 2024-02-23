import qrcode
import io

# code to generate QR code and return the URL
def generate_qrcode(url: str):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img_byte = io.BytesIO()
    img.save(img_byte, format="PNG")

    #placeholder for upload to cloud storage
    #replace with actual cloud storage upload logic
    qrcode_url = "https://example.com/qrcode.png"
    return qrcode_url