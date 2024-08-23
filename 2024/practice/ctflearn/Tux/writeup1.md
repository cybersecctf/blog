<title>Tux! - ctflearn</title>
<!DOCTYPE html>
<html>

<body>
    <h1>Tux! - ctflearn</h1>

    <h2>Challenge Description</h2>
    <p> The flag is hidden inside the Penguin! Solve this challenge before solving my 100 point Scope challenge which uses similar techniques as this one.
https://ctflearn.com/challenge/download/973
</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
        we download image
 <img src=" https://cybersecctf.github.io/blog/2024/practice/ctflearn/Tux/973.png" alt="ctf quetion image" class="inline"/>
and do exiftool  
 
 see base 64 that is password  <code>b'      Password: Linux12345\n'</code>    so this image have 
file inside it use binwalk on it
<pre>
#python
import binwalk,os
import blog 
def solve(file_path, search_text):
    # Use binwalk to extract files
    for module in binwalk.scan(file_path, signature=True, quiet=False, extract=True):
        print(f"{module.name} Results:")
        for result in module.results:
            print(f"\t{result.file.name}    0x{result.offset:X}    {result.description}")

    # Search for the text in the extracted files
    extracted_dir = file_path + '.extracted'
    for root, dirs, files in os.walk(extracted_dir):
        for file in files:
            with open(os.path.join(root, file), 'r') as f:
                contents = f.read()
                if search_text in contents:
                    print(f"Found '{search_text}' in {file}")
if __name__ == "__main__" :
 print("d")
 file=blog.set('test.bin',1)
 search=blog.set('text',2)
 print("d")
 solve(file,search)
</pre>
and see 1570 zip file is protected and use Linux12345 as password and unzip it and see flag
    
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">CTFlearn{Linux_Is_Awesome}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for work on exiftool and binwalk and zipfile and forensics/p>
</body>
</html>


