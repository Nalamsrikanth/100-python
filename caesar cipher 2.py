alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def cipher(message, num, direction):
    crypt_word = ''
    if direction =="decode":
        num *= -1
    for letter in message:
        if letter in alphabets:
            index_letter = alphabets.index(letter)
            position = index_letter + num
            new_word = alphabets[position]
            crypt_word += new_word
        else:
            crypt_word += letter

    print(crypt_word)
should_continue = True
while should_continue:
    to_do = input("enter do you want to encode or decode\n")
    text = input("enter the message:\n").lower()
    shift = int(input("enter how many shifts:\n"))
    shift_num = shift % 26
    cipher(text, shift_num, to_do)
    do_again =input("do you want to do again")
    if do_again =='yes':
        should_continue = True
    elif do_again =='no':
        should_continue = False


