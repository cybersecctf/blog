
<!DOCTYPE html>
<html>

<body>
    <h1>google-ctf-2018-beginners misc-floppy1</h1>

    <h2>Challenge Description</h2>
    <p> description: Looks like you found a way to open the file in the floppy! But that <a href="https://cybersecctf.github.io/blog/2024/googlectf/begginer2018/floppymisc2/attachments/temp_extract/www.com">www.com<</a>  file looks suspicious.. Dive in and take another look?
 
</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
since .com file were ms dos file and were in floppy so for test run www.com in msdos
<pre>
#python
import sys
file="www.com"
if len(sys.argv)>1:
    file=sys.argv[1]
os.system("dosbox "+file)
</pre>
 emulator on ubuntu with this command and on emulator type www.com>www.txt and in <a href="https://cybersecctf.github.io/blog/2024/googlectf/begginer2018/floppymisc2/attachments/temp_extract/www.txt">www.txt<</a> see flag
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">CTF{g00do1dDOS-FTW}
</p>

    <h2>Conclusion</h2>
    <p>this is a    easy chanllenge for run msdox file on ubuntu linux</p>
</body>
</html>




