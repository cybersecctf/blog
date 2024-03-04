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
def solve():
 import os
 filename = "dolls.jpg"
 extract_dir = "ext"
 flag = 0
 while flag == 0:
    print("\n== Extracting ==\n")
    os.system("unzip {} -d {}".format(filename,extract_dir))
    if os.path.exists(extract_dir+"/base_images"):
        os.chdir(extract_dir+"/base_images")
    else:
        os.chdir(extract_dir)
    for file in os.listdir():
        if file.endswith(".txt"):
            print("\n== FLAG: ")
            print(os.system("cat {}".format(file)))
            flag = 1
        else:
            filename = file
</pre>
and get flag.
  </li>
               

      
    </ol>

    <flag>picoCTF{336cf6d51c9d9774fd37196c1d7320ff}</flag>

    <h2>Conclusion</h2>
    <p>easy ctf for Forensics and get flag and folders from image and even zip files</p>
</body>
</html>
