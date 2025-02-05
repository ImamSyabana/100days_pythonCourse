alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.

def decrypt(decryptTxt , nShift):

# TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
#  by the shift amount and print the decrypted text.
    output = ""
    for x in range(len(decryptTxt)):
        idx = alphabet.index(decryptTxt[x])
        encIdx = idx - abs(nShift)
        if encIdx < 0:
            encIdx = encIdx % 26
        normChar = alphabet[encIdx]
        output = output + normChar


    print(output)
    return output

# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.
def caesar(direction, text, shift):
    output = ""
    for x in range(len(text)):
        idx = alphabet.index(text[x])

        if direction == "encode":
            encIdx = idx + abs(shift)
            if encIdx > 25:
                encIdx = encIdx % 26 # 25 - 1

        elif direction == "decode":
            encIdx = idx - abs(shift)
            if encIdx < 0:
                encIdx = encIdx % 26

        encChar = alphabet[encIdx]
        output = output + encChar

    print(output)
    return output


def encrypt(ogText, nShift):
    output = ""
    for x in range(len(ogText)):
        idx = alphabet.index(ogText[x])
        encIdx = idx + abs(nShift)
        if encIdx > 25:
            encIdx = encIdx % 26 # 25 - 1
        encChar = alphabet[encIdx]
        output = output + encChar

    print(output)
    return output


caesar(direction = direction,  text=text, shift=shift)

