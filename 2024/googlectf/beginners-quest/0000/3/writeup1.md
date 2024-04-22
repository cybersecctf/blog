<!DOCTYPE html>
<html>

<body>
    <h1>beginnersquest-0000-3</h1>

    <h2>Challenge Description</h2>
    <p>This tricky one introduces transposition 
   <a href="https://cybersecctf.github.io/blog/2024/googlectf/beginners-quest/0000/3/message.txt">message.txt</a>                                       
</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
       This suggest that the message is encrypted using a Substitution cipher and frequency analyis .we check word repeated word and map character and use tgis script for find flag.for example in ANSU{QEX_RJV_NVSOQVZ_GH_SIBF} ANSU IS FLAG and PDV is repeating more so is THE (P is T, D is H ,V is E ,F is A, ...)
<pre>
#python
import os,sys
#FREQUENCY CAESAR CIPHER
def FCcipher(MESSAGE: str) -> str:
    
    if  os.path.isfile(message) :
     with open(message, 'r') as f:
        text = f.read()
    else:
            text=  message
    result = ''
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if len(sys.argv)>2:
          alphabet=sys.argv[2]
    change =    'FCKHOSMYBVQUPLRTNIAJGEZWXD'
    if len(sys.argv)>3:
          change=sys.argv[3] 
    for char in text:
        if char in alphabet:
            result += change[alphabet.index(char)]
        else:
            result += char
    return result

message = "ANSU{QEX_RJV_NVSOQVZ_GH_SIBF}"
if len(sys.argv)>1:
 message=sys.argv[1]

print(FCcipher(message))
</pre>
 
       
    
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">FLAG{NOW_IVE_LEARNED_MY_ABCS}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for caesar chipher with frequency analysis </p>
</body>
</html>


 