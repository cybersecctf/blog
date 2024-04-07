
<!DOCTYPE html>
<html>

<body>
    <h1>Trivial Flag Transfer Protocol- cTrivial Flag Transfer Protocol</h1>

    <h2>Challenge Description</h2>
    <p> AUTHOR: DANNY

Description
Figure out how they moved the <a href="https://mercury.picoctf.net/static/88553d672efbccbc5868002f4c6eb737/tftp.pcapng">flag</a>.

</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
        <li> steps1 </li>
first i export contert of pcapng wifi file with<p id="code1">File > Export Objects > TFTP</p> and see files inside it.
     
  i open instructions.txt content is:

GSGCQBRFAGRAPELCGBHEGENSSVPFBJRZHFGQVFTHVFRBHESYNTGENAFSRE.SVTHERBHGNJNLGBUVQRGURSYNTNAQVJVYYPURPXONPXSBEGURCYNA

after test some method rot13 work and convert text to 

TFTPDOESNTENCRYPTOURTRAFFICSOWEMUSTDISGUISEOURFLAGTRANSFER.FIGUREOUTAWAYTOHIDETHEFLAGANDIWILLCHECKBACKFORTHEPLAN

first i thisnk it want work too but then i see that should separte words and find true pharse 

TFTP DOESNT ENCRYPT OUR TRAFFIC SO WE MUST DISGUISE OUR FLAG TRANSFER. FIGURE OUT A WAY TO HIDE THE FLAG AND I WILL CHECK BACK FOR THE PLAN

plain?so maybe should see  plain file ?

VHFRQGURCEBTENZNAQUVQVGJVGU-QHRQVYVTRAPR.PURPXBHGGURCUBGBF

this was again rot13 and after convert it find

<p id="code1">IUSEDTHEPROGRAMANDHIDITWITH-DUEDILIGENCE.CHECKOUTTHEPHOTOS</p>

after convert it with separation<p id="code1">I USED THE PROGRAM AND HID IT WITH-DUEDILIGENCE. CHECKOUTTHEPHOTOS</p>

program was in zip in user/bin steghide so extract one of file.see size of picture3.bmp is bigger than normal so should use it?
    <pre>
$steghide extract -sf picture3.bmp
</pre>
and enter passphrase  DUEDILIGENCE and it extract <a href="https://phantom1ss.github.io/blog/2024/practice/picoctf/TrivialFlagTransferProtocol/flag.txt">flag.txt</a>
that ahve flag inside it.
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">picoCTF{h1dd3n_1n_pLa1n_51GHT_18375919}
</p>

    <h2>Conclusion</h2>
    <p>this is a    easy chanllenge forforensics and steganography and work with pcappng zip file</p>
</body>
</html>



 