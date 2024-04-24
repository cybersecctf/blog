<!DOCTYPE html>
<html>

<body>
    <h1>google ctf begginer quest-  1837 -0</h1>

    <h2>Challenge Description</h2>
    <p>  Operator, could you decode this telegram for us with combinations of brief signals (dots) and long  to plain English? We recently got this telegram frR  ║om across the ocean in the United States and transcribed what we heard from the telegraph sounder, b ut we don't know what it means.                  

    HINT: Some of these letters don't mean anything in  

   the Morse code we use here in Europe. Could they  
  be in some American style encoding?  


<a href="https://cybersecctf.github.io/blog/2024/googlectf/beginners-quest/1837/0/message.txt">message.txt</a>

</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
     we open message code and use normal decrypt morse code and not work so use american  morse code translator with python and it work.
<pre>
import sys
flag = "-   . ..   ....-   -.   ---   ....-   -   ⸺   ....-   -.   -   ..   .. ."
if len(sys.argv)>1:
 flag=sys.argv[1]
american_morse_dict = {
    '-': 'T',
    '. ..': 'R',
    '....-': '4',
    '-.': 'N',
    '---': '5',
    '⸺': 'L',
    '-.': 'N',
    '..': 'I',
    '.. .': 'C'
}

flag = flag.split('   ')
decoded_flag = ''
for code in flag:
    if code in american_morse_dict:
        decoded_flag += american_morse_dict[code]
    else:
        decoded_flag += code
print("FLAG{" + decoded_flag + "}")
</pre>
after run this python will geet flag below.
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">FLAG{TR4N54TL4NTIC}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for decode morse code on american style</p>
</body>
</html>

