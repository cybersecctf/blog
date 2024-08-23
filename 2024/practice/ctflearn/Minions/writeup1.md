<title>Minions- ctflearn</title>

<!DOCTYPE html>
<html>

<body>
    <h1>Minions- ctflearn</h1>

    <h2>Challenge Description</h2>
    <p> Hey! Minions have stolen my flag, encoded it few times in one cipher, and then hidden it somewhere there: https://mega.nz/file/1UBViYgD#kjKISs9pUB4E-1d79166FeX3TiY5VQcHJ_GrcMbaLhg Can you help me? TIP: Decode the flag until you got a sentence.
 
</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
we download image
 <img src=" https://cybersecctf.github.io/blog/2024/practice/ctflearn/Minions/Hey_You.png" alt="minion image" class="inline"/>
nothing found in srtings or  exiftools but using this script in image and 
    <pre>
#python
import blog
import binwalk
import zipfile
import rarfile
import io,os,sys
def extract_and_search(file_path, search_text):
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
def search_in_zip(zip_path, search_text):
    with zipfile.ZipFile(zip_path, 'r') as myzip:
        for i in myzip.infolist():
            if not i.is_dir() and i.filename.endswith('.txt'):
                with myzip.open(i.filename) as myfile:
                    if search_text in myfile.read().decode():
                        print(f'Found "{search_text}" in {i.filename}')
                         
   

def search_in_rar(rar_path, search_text):
    with rarfile.RarFile(rar_path) as myrar:
        for f in myrar.infolist():
            if not f.isdir() and f.filename.endswith('.txt'):
                with myrar.open(f) as myfile:
                    if search_text in myfile.read().decode():
                        print(f'Found "{search_text}" in {f.filename}')
def solve(file,search,type): 
 if type=="rar" or file.endswith("rar"):                                                        
  search_in_rar(file,search)
 elif type=="binwalk" or not file.endswith("zip"):
  extract_and_search(file,search)
 else:
  search_in_zip(file,search)
if __name__ == "__main__" :
 file=blog.set("Hey_You.png",1)
 search=blog.set("",2)
 type=blog.set("rar",3)
 solve(file,search,type)
</pre>
       binwalk say that have files inside it and text inside
Nothing_Here_16/..txt  but can't unrar it because name ..txt is not supported and should be something like 1.txt 
or open it inside tool
 <img src=" https://cybersecctf.github.io/blog/2024/practice/ctflearn/Minions/ubuntuextractor.png" alt="ctf quetion image" class="inline"/>
and see link that open new image of minions
 <img src=" https://cybersecctf.github.io/blog/2024/practice/ctflearn/Minions/Only_Few_Steps.jpg" alt="ctf quetion image" class="inline"/>
    using binwalk of this script give me this image 

 <img src=" https://cybersecctf.github.io/blog/2024/practice/ctflearn/Minions/_Only_Few_Steps.jpg.extracted/YouWon(Almost).jpg" alt="ctf quetion image" class="inline"/>
strings this picture give me this text
<pre>
CTF{VmtaU1IxUXhUbFZSYXpsV1RWUnNRMVpYZEZkYWJFWTJVVmhrVlZGVU1Eaz0=)
</pre>
that is base64 text but should do a lot of(5) base64 text on it to get it
<pre>
 
dawoodctf@dawoodctf-virtual-machine:~/Desktop/blog/2024/practice/ctflearn/Minions decode VmtaU1IxUXhUbFZSYXpsV1RWUnNRMVpYZEZkYWJFWTJVVmhrVlZGVU1Eaz0=
decoded from base64: b'VkZSR1QxTlVRazlWTVRsQ1ZXdFdabEY2UVhkVVFUMDk='

 

dawoodctf@dawoodctf-virtual-machine:~/Desktop/blog/2024/practice/ctflearn/Minions decode VkZSR1QxTlVRazlWTVRsQ1ZXdFdabEY2UVhkVVFUMDk=
decoded from base64: b'VFRGT1NUQk9VMTlCVWtWZlF6QXdUQT09'

dawoodctf@dawoodctf-virtual-machine:~/Desktop/blog/2024/practice/ctflearn/Minions decode VFRGT1NUQk9VMTlCVWtWZlF6QXdUQT09
decoded from base64: b'TTFOSTBOU19BUkVfQzAwTA=='

dawoodctf@dawoodctf-virtual-machine:~/Desktop/blog/2024/practice/ctflearn/Minions decode TTFOSTBOU19BUkVfQzAwTA==
decoded from base64: b'M1NI0NS_ARE_C00L'

</pre>
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">CTFlearn{M1NI0NS_ARE_C00L}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for work on binwalk and unrar and unzip and forensics</p>
</body>
</html>




