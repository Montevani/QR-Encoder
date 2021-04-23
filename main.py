import qrcode
import os

path = os.getcwd() + "/qrcode.png"
data = 'https://github.com/Montevani/QR-Encoder'

qr = qrcode.QRCode(version = 1, box_size=8, border=2)

qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color = 'black', back_color = 'white')

img.save(path)