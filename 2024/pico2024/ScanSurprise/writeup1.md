
<!DOCTYPE html>
<html>

<body>
    <h1>Scan Surprise- picoctf2024</h1>

    <h2>Challenge Description</h2>
    <p> 
 AUTHOR: JEFFERY JOHN

Description
I've gotten bored of handing out flags as text. Wouldn't it be cool if they were an image instead?
You can download the challenge files here:
<a href="https://phantom1ss.github.io/blog/2024/pico2024/ScanSurprise/challenge.zip">challenge.zip</a>
Additional details will be available after launching your challenge instance.


</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
    <pre>
import zipfile
import os
from PIL import Image
from pyzbar.pyzbar import decode

def search_text_in_qrcode(png_file_path,text):
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
                print(obj.data.decode('utf-8')) 
                if  text in obj.data.decode('utf-8'):
                        return True
    else:
        return False

    # If no QR code is found, return None
    return False

def search_text_in_zip(zip_file_path, search_text):
    found_files = []

    # Open the zip file
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        # Extract the contents to a temporary directory
        extract_dir = "./challenges"
        zip_ref.extractall(extract_dir)

        # Traverse through the extracted directory
        for root, dirs, files in os.walk(extract_dir):
            for file in files:
                file_path = os.path.join(root, file)
                # Check if the file is a text file
      
                if search_text_in_qrcode(file_path,search_text)
                            found_files.append(file_path)

    return found_files

# Example usage
zip_file_path = 'challenge.zip'
search_text = 'challenge'
found_files = search_text_in_zip(zip_file_path, search_text)
if found_files:
    print("Found in the following files:")
    for file in found_files:
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
    <p>this is a very   easy chanllenge for  search qrcodes in zip files</p>
</body>
</html>


