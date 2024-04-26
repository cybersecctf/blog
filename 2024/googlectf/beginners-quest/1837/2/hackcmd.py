# Morse code dictionary
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----'
}

# Inverted Morse code dictionary for decoding
inverted_morse_code_dict = {value: key for key, value in morse_code_dict.items()}

# American Morse code dictionary
american_morse_code_dict = {
     '.-': 'A','-...': 'B','.. .': 'C','-..': 'D','.': 'E','.-.': 'F', '--.': 'G','....': 'H','..': 'I','-.-.': 'J','-.-': 'K','⸺': 'L','--': 'M','-.': 'N','. .': 'O','.....': 'P','..-.': 'Q','. ..': 'R','...': 'S','-': 'T','..-': 'U','...-': 'V',
    '.--': 'W','.-..': 'X','.. ..': 'Y','... .': 'Z','1': '.----', '2': '..---', '3': '...--','4': '....-', '5': '---', '6': '-....',  '7': '--...', '8': '---..','9': '----.', '0': '-----','.': '.-.-.-',',': '--..--','?': '..--..', '\'': '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-', '@': '.--.-.'
}

# Inverted American Morse code dictionary for decoding
inverted_american_morse_code_dict = {value: key for key, value in american_morse_code_dict.items()}

def text_to_morse(text, american=False):
    morse_dict = american_morse_code_dict if american else morse_code_dict
    return ' '.join(morse_dict.get(char.upper(), '?') for char in text)

def morse_to_text(morse, american=False):
    morse_dict = inverted_american_morse_code_dict if american else inverted_morse_code_dict
    return ''.join(morse_dict.get(code, '?') for code in morse.split())

def main():
    # Test text to Morse code conversion
    text = "HELLO WORLD"
    morse_international = text_to_morse(text)
    morse_american = text_to_morse(text, american=True)
    print("Text:", text)
    print("International Morse Code:", morse_international)
    print("American Morse Code:", morse_american)

    # Test Morse code to text conversion
    morse = "- . .. ....- -. --- ....- - ⸺ ....- -. - .. .. ."
    text_international = morse_to_text(morse)
    text_american = morse_to_text(morse, american=True)
    print("International Morse Code:", morse)
    print("Text:", text_international)
    print("Text (American Morse):", text_american)

if __name__ == "__main__":
    main()

