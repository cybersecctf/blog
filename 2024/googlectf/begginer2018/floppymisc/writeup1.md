
<!DOCTYPE html>
<html>

<body>
    <h1>ctf event- challengename Challenge Writeup(first save it)</h1>

    <h2>Challenge Description</h2>
    <p> Using the credentials from the letter, you logged in to the Foobanizer9000-PC. It has a floppy drive...why? There is an .ico file on the disk, but it doesn't smell right
 <a href="https://cybersecctf.github.io/blog/2024/googlectf/begginer2018/floppymisc/foo.ico">attachment</a>
</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
in this challenge we see that this file is zip file in txy format so via this  <a href="https://cybersecctf.github.io/blog/2024/practice/picoctf/firstfind/writeup1.md">writeup</a>find this code for search on it 

        <pre>
#python
import zipfile
import os,sys
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
zip_file_path = 'foo.ico'
search_text = 'CTF'
if len(sys.argv)>1:
  zip_file_path=sys.argv[1]
if len(sys.argv)>2:
  search_text=sys.argv[2]
found_files = search_text_in_zip(zip_file_path, search_text)
if found_files:
    print("Found in the following files:")
 
    for file in found_files:
        print(file)
        os.system("cat "+file)
else:
    print("Text not found in any files.")
#same with  https://cybersecctf.github.io/blog/2024/practice/picoctf/firstfind/writeup1.md

</pre>
    and find flag IN driver.txt in foo.ico  in text below
<code>
./temp_extract/driver.txt
This is the driver for the Aluminum-Key Hardware password storage device.
     CTF{qeY80sU6Ktko8BJW}

In case of emergency, run www.com

</code>
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">     CTF{qeY80sU6Ktko8BJW}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for search text in zip on misc</p>
</body>
</html>



