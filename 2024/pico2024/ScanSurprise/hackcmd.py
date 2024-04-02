from PIL import Image
from pyzbar.pyzbar import decode
import zipfile
import os,sys
def search_qr_text_in_zip(zip_file_path):
    found_text = []

    # Open the zip file
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        # Extract the contents to a temporary directory
        extract_dir = "./temp_extract"
        zip_ref.extractall(extract_dir)

        # Traverse through the extracted directory
        for root, dirs, files in os.walk(extract_dir):
            for file in files:
                file_path = os.path.join(root, file)
                # Check if the file is a text file
                if file_path.endswith('.png'):
                  s=search_text_in_qrcode(file_path)
                  found_text.append(s)

    return found_text
def search_text_in_qrcode(png_file_path):
    # Open the PNG file
    image = Image.open(png_file_path)
    
    # Decode QR code
    decoded_objects = decode(image)
    
    if decoded_objects:
        # Iterate over decoded objects
        for obj in decoded_objects:
            # Check if the decoded object is of type QR code
            if obj.type == 'QRCODE':
                # Return the text contained in the QR code
                return obj.data.decode('utf-8')
    else:
        print("No QR code found in the image.")

    # If no QR code is found, return None
    return None
stext="pico"
zip_file_path = 'challenge.zip'
if len(sys.argv)>1:
    zip_file_path = sys.argv[1]
if len(sys.argv)>2:
    stext = sys.argv[2]

found_text= search_qr_text_in_zip(zip_file_path)
if found_text:
    print("Found qr text in the following files:")
    for text in found_text:
        if stext in text:
         print(text)
else:
    print("Text not found in any files.")