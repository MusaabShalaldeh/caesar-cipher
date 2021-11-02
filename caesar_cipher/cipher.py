import nltk
import re
import string

nltk.download('words', quiet=True)
nltk.download('names', quiet=True)

from nltk.corpus import words, names

word_list = words.words()
name_list = names.words()


def encrypt(message: str,key: int):
    if key >= 27:
        key = 1
    upper_offset = 65
    lower_offest = 97
    num_offset = ord("0")
    punctionation_offset = ord("!")
    words = message.split()
    cipher_words = []
    for word in words:
        cipher = ""
        for char in word:
            if char.isupper():
                cipher += chr((ord(char) + key - upper_offset) % 26 + upper_offset)
            elif char.islower():
                cipher += chr((ord(char) + key - lower_offest) % 26 + lower_offest)
            elif char.isnumeric():
                cipher += chr((ord(char) + key - num_offset) % 10 + num_offset)
            elif char in string.punctuation:
                cipher += chr((ord(char) + key - punctionation_offset) % 32 + punctionation_offset)
        cipher_words.append(cipher)

    return " ".join(cipher_words)



def decrypt(cipher,key):
    return encrypt(cipher, -key)

def crack(cipher: str):
    pass


if __name__ == "__main__":
    print(word_list)
    print(name_list)