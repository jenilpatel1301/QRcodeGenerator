import pyqrcode
import png
link = "https://github.com/jenilpatel1301?tab=repositories/" # Add your link here
qr_code = pyqrcode.create(link)
qr_code.png("github.png", scale=5) # give a name of image file

# it will generate a QR code image of that link