import qrcode
from PIL import Image

linkedin_url = "https://www.linkedin.com/in/avi-atul-makkar-09682a240/"  # <-- replace this
output_path = "image.png"
qr_box_size = 10
qr_border = 4
error_correction = qrcode.constants.ERROR_CORRECT_M

qr = qrcode.QRCode(
    version=None,
    error_correction=error_correction,
    box_size=qr_box_size,
    border=qr_border,
)
qr.add_data(linkedin_url)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white").convert('RGB')

# optional margin
margin = 20
w, h = img.size
canvas = Image.new('RGB', (w + margin*2, h + margin*2), 'white')
canvas.paste(img, (margin, margin))

canvas.save(output_path)
print("Saved QR code to:", output_path)
