<title>Binwalk- ctflearn</title>

<!DOCTYPE html>
<html>

<body>
    <h1>Binwalk- ctflearn</h1>

    <h2>Challenge Description</h2>
    <p> Here is a file with another file hidden inside it. Can you extract it? https://mega.nz/#!qbpUTYiK!-deNdQJxsQS8bTSMxeUOtpEclCI-zpK7tbJiKV0tX
 
</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
for use binwalk for advanced big files and search text or extract can use this python code
<pre>
#python
import binwalk,os,sys
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

file='test.bin'
search='text'
if len(sys.argv)>1:
 file=sys.argv[1]
if len(sys.argv)>2:
 search=sys.argv[2]
 extract_and_search(file,search)
else:
  os.system("binwalk --dd='.*'  "+file)
</pre>
or simply for this problem can use this command
<pre>
$binwalk --dd='.*'  PurpleThing.jpeg
</pre>
    and find image have pic and get flag
 <img src=" https://cybersecctf.github.io/blog/2024/practice/ctflearn/Binwalk/25795.jpg" alt="flag" class="inline"/>
    </ol> 
<br>
    <h2>Flag</h2>
    <p class="flag">ABCTF{b1nw4lk_is_us3ful}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for use and search with binwalk and forensics</p>
</body>
</html>


