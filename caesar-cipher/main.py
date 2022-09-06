from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

def caesar(typeEn,text,shift):
    finalText=''
    if typeEn == 'encode' or typeEn == 'decode':
        if typeEn == 'decode' :
            shift *= -1
        for char in text :
            if char in alphabet:
                p = alphabet.index(char)
                newP = p + shift
                finalText += alphabet[newP]
        print(f"Here's the {typeEn}d result: {finalText}")
    else:
        print('Wrong Type of crypt')
        
        
    
should_end = False  
  
while True :
    
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift=shift%26
    caesar(direction,text,shift)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        print("Goodbye")
        break
