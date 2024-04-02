
<!DOCTYPE html>
<html>

<body>
    <h1>Scan Surprise- picoctf2024</h1>

    <h2>Challenge Description</h2>
    <p> AUTHOR: JEFFERY JOHN

Description
I've gotten bored of handing out flags as text. Wouldn't it be cool if they were an image instead?
You can download the challenge files here:
<a href="https://artifacts.picoctf.net/c_atlas/1/challenge.zip">challenge.zip</a>
Additional details will be available after launching your challenge instance.
</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
      we can use this code and run for find qrcode text in zipfile
<pre>
from PIL import Image
from pyzbar.pyzbar import decode
import zipfile
import os
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

zip_file_path = 'challenge.zip'
 
found_text= search_qr_text_in_zip(zip_file_path)
if found_files:
    print("Found qr text in the following files:")
    for file in found_text:
        print(file)
else:
    print("Text not found in any files.")
</pre>
    
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">picoCTF{p33k_@_b00_3f7cf1ae}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for work on develper tools in in chrome and web exploitations</p>
</body>
</html>


