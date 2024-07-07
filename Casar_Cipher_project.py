alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def encryption(plain_text,shift):
    cipher_text = ""
    for char in plain_text:
        if char in alphabets:
            position = alphabets.index(char)
            new_position = (position+shift_key)%26
            cipher_text += alphabets[new_position]
        else:
            cipher_text += char
    print(f"here's the text after encryption {cipher_text}")
def decryption(cipher_text,shift):
    plain_text = ""
    for char in cipher_text:
        if char in alphabets:
            position = alphabets.index(char)
            new_position = (position-shift_key)%26
            plain_text += alphabets[new_position]
        else:
            plain_text += char
    print(f"here's the text after decryption {plain_text}")

wanna_end=False
while not wanna_end:
    what_to_do=input("type 'encrypt' for encryption and 'decrypt' for decryption:\n")
    text=input("type a message:\n").lower()
    shift_key=int(input("type a key:\n"))
    if what_to_do=='encrypt':
         encryption(plain_text=text,shift=shift_key)
    elif what_to_do=='decrypt':
        decryption(cipher_text=text,shift=shift_key)
    play_again=input("enter 'yes' if you wanna play or 'no' to exit:\n")
    if play_again=='no':
        wanna_end=True
        print("have a nice day,bye!")