<!DOCTYPE html>
<html>

<body>
    <h1>Morse Code-ctflearn</h1>

    <h2>Challenge Description</h2>
    <p> ..-. .-.. .- --. ... .- -- ..- . .-.. -- --- .-. ... . .. ... -.-. --- --- .-.. -... -.-- - .... . .-- .- -.-- .. .-.. .. -.- . -.-. .... . . ...
 
</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
         as we see in description this is morse code and can decode by this code in this <a href="https://cybersecctf.github.io/blog/2024/googlectf/beginners-quest/1837/0/writeup1.md">writeup</a>
 <pre>
#python
import sys
import re

flag = "-   . ..   ....-   -.   ---   ....-   -   ⸺   ....-   -.   -   ..   .. ."

american_morse_dict = {
    '.-': 'A',
    '-...': 'B',
    '-.-.': 'C',
    '-..': 'D',
    '.': 'E',
    '..-.': 'F',
    '--.': 'G',
    '....': 'H',
    '..': 'I',
    '.---': 'J',
    '-.-': 'K',
    '.-..': 'L',
    '--': 'M',
    '-.': 'N',
    '---': 'O',
    '.--.': 'P',
    '--.-': 'Q',
    '.-.': 'R',
    '...': 'S',
    '-': 'T',
    '..-': 'U',
    '...-': 'V',
    '.--': 'W',
    '-..-': 'X',
    '-.--': 'Y',
    '--..': 'Z',
    '.----': '1',
    '..---': '2',
    '...--': '3',
    '....-': '4',
    '.....': '5',
    '-....': '6',
    '--...': '7',
    '---..': '8',
    '----.': '9',
    '-----': '0',
    '.-.-.-': '.',
    '--..--': ',',
    '..--..': '?',
    '.----.': "'",
    '-.-.--': '!',
    '-..-.': '/',
    '-.--.': '(',
    '-.--.-': ')',
    '.-...': '&',
    '---...': ':',
    '-.-.-.': ';',
    '-...-': '=',
    '.-.-.': '+',
    '-....-': '-',
    '..--.-': '_',
    '.-..-.': '"',
    '...-..-': '$',
    '.--.-.': '@',
    '⸺': 'L'  # Replace with the appropriate Morse code for 'L'
}

if len(sys.argv) > 1:
    flag = sys.argv[1]

flag = re.split(r'\s+', flag)
decoded_flag = ''

for code in flag:
    if code in american_morse_dict:
        decoded_flag += american_morse_dict[code]
    else:
        decoded_flag += code

print(decoded_flag)#remove flag{}
</pre>
 with morse code as  prameters
and get ftext FLAGSAMUELMORSEISCOOLBYTHEWAYILIKECHEES that have flag inside it.    
    
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">flag{SAMUELMORSEISCOOLBYTHEWAYILIKECHEES}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for  convert morse code to english and american style text</p>
</body>
</html>


