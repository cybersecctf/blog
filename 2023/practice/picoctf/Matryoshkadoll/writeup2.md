<!DOCTYPE html>
<html>


<body>
    <h1>picopractice(2021)- Matryoshka doll Challenge Writeup</h1>

    <h2>Challenge Description</h2>
    <p>Matryoshka dolls are a set of wooden dolls of decreasing size placed one inside another. What's the final one? Image: this 
</p>

    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
        <li>matrioska doll is a nested dool commonly means nested files and zip and image in this case for solve this problem i use this code fr</li>
        <li>
<pre>
import zipfile
import os

def search_text_in_zip(zip_file_path, search_text):
    found_files = []

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
                if file_path.endswith('.txt'):
                    # Open the text file and search for the text
                    with open(file_path, 'r') as f:
                        if search_text in f.read():
                            found_files.append(file_path)

    # Cleanup the temporary directory
  

    return found_files

# Example usage
zip_file_path = 'files.zip'
search_text = 'pico'
found_files = search_text_in_zip(zip_file_path, search_text)
if found_files:
    print("Found in the following files:")
    for file in found_files:
        print(file)
else:
    print("Text not found in any files.")

</pre>
and get flag.
  </li>
               

      
    </ol>

    <flag>picoCTF{336cf6d51c9d9774fd37196c1d7320ff}</flag>

    <h2>Conclusion</h2>
    <p>easy ctf for Forensics and get flag and folders from image and even zip files</p>
</body>
</html>
