# TODO-1: Import and print the logo from art.py when the program starts.
import art
print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# TODO-2: What happens if the user enters a number/symbol/space?


def caesar(original_text, shift_amount, encode_or_decode):
    output = ""
    for x in range(len(original_text)):

        if original_text[x].isalpha() == True:

            idx = alphabet.index(text[x])

            if encode_or_decode == "encode":
                encIdx = idx + abs(shift)
                if encIdx > 25:
                    encIdx = encIdx % 26  # 25 - 1

            elif encode_or_decode == "decode":
                encIdx = idx - abs(shift)
                if encIdx < 0:
                    encIdx = encIdx % 26

            encChar = alphabet[encIdx]
            output = output + encChar

        elif original_text[x].isalpha() == False:
            output = output + original_text[x]

    print(f"Here is the {encode_or_decode}d result: {output}")
    return output


# TODO-3: Can you figure out a way to restart the cipher program?



continueRun = True
while(continueRun == True):

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'. \n")
    if restart.lower() == "yes":
        continueRun = True
    elif restart.lower() == "no":
        continueRun = False



