# Morse Code Dictionary
MORSE_CODE_DICT = {
    'A': '.-',     'B': '-...',   'C': '-.-.', 
    'D': '-..',    'E': '.',      'F': '..-.',
    'G': '--.',    'H': '....',   'I': '..',
    'J': '.---',   'K': '-.-',    'L': '.-..',
    'M': '--',     'N': '-.',     'O': '---',
    'P': '.--.',   'Q': '--.-',   'R': '.-.',
    'S': '...',    'T': '-',      'U': '..-',
    'V': '...-',   'W': '.--',    'X': '-..-',
    'Y': '-.--',   'Z': '--..',
    '1': '.----',  '2': '..---',  '3': '...--',
    '4': '....-',  '5': '.....',  '6': '-....',
    '7': '--...',  '8': '---..',  '9': '----.',
    '0': '-----',  ' ': '/'
}

# Reversing the dictionary for decoding
REVERSE_MORSE_CODE_DICT = {value: key for key, value in MORSE_CODE_DICT.items()}

def encode_to_morse(message):
    return ' '.join(MORSE_CODE_DICT.get(char.upper(), '?') for char in message)

def decode_from_morse(code):
    return ''.join(REVERSE_MORSE_CODE_DICT.get(char, '?') for char in code.split())

# Sample usage
if __name__ == "__main__":
    print("Morse Code Encoder & Decoder")
    choice = input("Choose [E]ncode or [D]ecode: ").strip().upper()
    
    if choice == 'E':
        text = input("Enter text to encode: ")
        morse = encode_to_morse(text)
        print("Morse Code:", morse)
    elif choice == 'D':
        morse = input("Enter Morse Code (use space between letters, '/' for space): ")
        text = decode_from_morse(morse)
        print("Decoded Text:", text)
    else:
        print("Invalid choice.")
