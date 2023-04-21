# import pyfiglet module
import pyfiglet

# generate key
def generateKey(string, key):
    key = list(key)
    if len(string) == len(key):
        return (key)
    else:
        for i in range(len(string) -len(key)):
            key.append(key[i % len(key)])
    return ("".join(key))

# encrypt the text
def cipherText(string, key):
    cipher_text = []
    for i in range(len(string)):
        x = (ord(string[i]) + ord(key[i])) % 26
        x += ord('A')
        cipher_text.append(chr(x))
    return ("".join(cipher_text))
