
<!DOCTYPE html>
<html>
 
<body>
    <h1>Big Zip- picogym exclusive</h1>

    <h2>Challenge Description</h2>
    <p> AUTHOR: LT 'SYREAL' JONES

Description
Unzip this archive and find the flag.
Download zip file:https://artifacts.picoctf.net/c/505/big-zip-files.zip
</p>

    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
       it was like <a href="https://phantom1ss.github.io/blog/2024/practice/picoctf/firstfind/writeup1.md">firstfind</a> writeup from this blog .open zip and search flag that is hard and tak long in this challenge or use this code and get flag<pre>
import zipfile
import os
def search_text_in_zip(zip_file_path, search_text):
    found_files = []
    content=[]
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
                if file_path.endswith('.txt'):#can use for find specicifc file
                    # Open the text file and search for the text
                    with open(file_path, 'r') as f:
                        if search_text in f.read():
                            found_files.append(file_path)
                            content.append(file_path)
    return found_files

# Example usage
zip_file_path = 'big-zip-files.zip'
search_text = 'pico'
found_files = search_text_in_zip(zip_file_path, search_text)
if found_files:
    print("Found in the following files:")
 
    for file in found_files:
        print(file)
        os.system("cat "+file)
else:
    print("Text not found in any files.")
</pre>
  
       
    
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">picoCTF{gr3p_15_m4g1c_ef8790dc}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for search on zip files</p>
</body>
</html>


