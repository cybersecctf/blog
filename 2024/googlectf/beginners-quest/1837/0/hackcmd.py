flag = "-   . ..   ....-   -.   ---   ....-   -   ⸺   ....-   -.   -   ..   .. ."
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