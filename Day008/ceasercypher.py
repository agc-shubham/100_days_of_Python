import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(art.logo)


def ceaser(text,shift,direction):
    direction.lower()
    if(direction=="decode"):
        shift *=-1
    Echars = ""
    for char in text:
        if(char in alphabet):
            iIndex = alphabet.index(char)
            iIndex += shift
            iIndex %= 26
            Echars += alphabet[iIndex]
        else:
            Echars += char
    print(f"The {direction}d text is {Echars}")

while(True):
    shouldContinue = input("Do you want to encrypt or decrypt a message\t Yes or No \n")
    if(shouldContinue.lower()=="no"):
        break
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    ceaser(text,shift,direction)
