from pyzbar.pyzbar import decode
from PIL import Image

# Load the image from a file
img = Image.open('qrcode.png')

# Decode the QR code
decoded_objects = decode(img)

# Print the result
for obj in decoded_objects:
    print('Type: ', obj.type)
    print('Data: ', obj.data.decode('utf-8'))