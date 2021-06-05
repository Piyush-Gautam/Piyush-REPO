# Python program to implement Morse Code Translator

"""
VARIABLE KEY
'morse_code' -> 'stores the morse translated form of the english string'
'english_from_morse_code' -> 'stores the english translated form of the morse string'
'citext' -> 'stores morse code of a single character'
'i' -> 'keeps count of the spaces between morse characters'
'not_morse' -> 'stores the string to be encoded or decoded'
"""

# Dictionary representing the morse code chart
MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}


# Function to encrypt the string
# according to the morse code chart
def encrypt(not_morse):
    morse_code = ''
    for letter in not_morse:
        if letter != ' ':
            morse_code += MORSE_CODE_DICT[letter] + ' '
        else:
            morse_code += ' '

    return morse_code


# Function to decrypt the string
# from morse to english
def decrypt(morse):

    morse += ' '
    english_from_morse_code = ''
    citext = ''
    for letter in morse:
        # checks for space
        if (letter != ' '):
            # counter to keep track of space
            i = 0
            # storing morse code of a single character
            citext += letter
        else:
            # if i = 1 that indicates a new character
            i += 1

            # if i = 2 that indicates a new word
            if i == 2:
                english_from_morse_code += ' '
            else:
                # accessing the keys using their values (reverse of encryption)
                english_from_morse_code += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT
                                                              .values()).index(citext)]
                citext = ''

    return english_from_morse_code


# Hard-coded driver function to run the program
def main():
    # not_morse = input("please enter text to convert to morse_code")
    # result = encrypt(not_morse.upper())
    # print (result)

    morse = ".--. .. -.-- ..- ... .... --. .- ..- - .- -- "
    result = decrypt(morse)
    print(result)


# Executes the main function
if __name__ == '__main__':
    main()
