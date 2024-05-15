
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("enter do you want to encode or decode\n")
text = input("enter the message:\n").lower()
shift = int(input("enter how many shifts:\n"))

def encrypt(message, num):
    encrypt_word = ''
    for letter in message:
        index_letter = alphabets.index(letter)
        position = index_letter + num
        new_word = alphabets[position]
        encrypt_word += new_word
    print(encrypt_word)

def decrypt():
    decrypt_word = ''
    for letter in message:
        index_letter = alphabets.index(letter)
        position = index_letter - num
        new_word = alphabets[position]
        decrypt_word += new_word
    print(decrypt_word)
if direction =="encode":
    encrypt(text, shift)
elif direction =="decode":
    decrypt(text, shift)