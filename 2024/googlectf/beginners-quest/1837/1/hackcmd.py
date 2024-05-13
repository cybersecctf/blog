#python
import sys
american_morse_dict = {
    '.-': 'A',
    '-...': 'B',
    '.. .': 'C',
    '-..': 'D',
    '.': 'E',
    '.-.': 'F',
    '--.': 'G',
    '....': 'H',
    '..': 'I',
    '-.-.': 'J',
    '-.-': 'K',
    '⸺': 'L',
    '--': 'M',
    '-.': 'N',
    '. .': 'O',
    '.....': 'P',
    '..-.': 'Q',
    '. ..': 'R',
    '...': 'S',
    '-': 'T',
    '..-': 'U',
    '...-': 'V',
    '.--': 'W',
    '.-..': 'X',
    '.. ..': 'Y',
    '... .': 'Z',
}

# read text from 1.txt
file='message.txt'
if len(sys.argv)>1:
   file=sys.argv[1]
with open(file, 'rb') as f:
    text = f.read().decode('utf-8')

text = text.replace('/', "  /  ")
text = text.replace('{', "  {  ")
text = text.replace('}', "  }  ")
text = text.split('   ')

decoded_text = ''
for code in text:
    if code in american_morse_dict:
        decoded_text += american_morse_dict[code]
    else:
        decoded_text += code

decoded_text = decoded_text.replace('/', ' ')
decoded_text = decoded_text.replace(' {', '{')
decoded_text = decoded_text.replace('} ', '}')

print(decoded_text)
