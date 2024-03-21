alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
text = input("Type your message: ").lower()
shift = int(input("Type the shift number: "))

def encrepted (text, shift):
    encrepted_message = ""
    for letter in text:
        i = alphabet.index(letter)
        p = i+shift
        n_p = alphabet[p]
        encrepted_message += n_p
    print (f"the encrepted message is {encrepted_message}")
def decreted (text, shift):
    decreted_message = ""
    for letter in text:
        i = alphabet.index(letter)
        p = i-shift
        n_p = alphabet[p]
        decreted_message += n_p
    print (f"the decreted message is {decreted_message}")
    
if direction == "encode":
    encrepted(text, shift)
elif direction == "decode":
    decreted(text, shift)
else:
    print("invalid input")