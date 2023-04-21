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

# decrypt the encrypted text
def originalText(cipher_text, key):
    orig_text = []
    for i in range(len(cipher_text)):
        x = (ord(cipher_text[i]) - ord(key[i]) + 26) % 26
        x += ord('A')
        orig_text.append(chr(x))
    return ("".join(orig_text))

# print output
if __name__ == "__main__":
    string = input("What is the message? ")
    output_str = ""
    keyword = input("What is the keyword? ")
    output_str = ""
    key = generateKey(string, keyword)
    cipher_text = cipherText(string, key)
    print("Cipher Text : ", cipher_text)
    print("Plain Text : ", originalText(cipher_text, key))
# change font to "doh"
    result = pyfiglet.figlet_format(cipher_text, font="doh")
    print(result)
