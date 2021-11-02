import nltk
import re
import string

nltk.download('words', quiet=True)
nltk.download('names', quiet=True)

from nltk.corpus import words, names

word_list = words.words()
name_list = names.words()


def encrypt(message: str,key: int):
    """"
    A function that takes in a text and key then returns a cipher thats encryped following caesar's encyption.

    input: string, int

    output: string
    """
    alphabets = [string.ascii_lowercase, string.ascii_uppercase, string.punctuation,string.digits]
    def shift_alphabet(alphabet):
        return alphabet[key:]+alphabet[:key]
    
    shifted_alphabets = tuple(map(shift_alphabet, alphabets))
    final_alphabet = "".join(alphabets)
    final_alphabet_shifted = "".join(shifted_alphabets)
    table = str.maketrans(final_alphabet, final_alphabet_shifted)
    return message.translate(table)


def decrypt(cipher,key):
    """"
    A function that takes in a cipher text and key then returns a decrypted cipher using the key it was encrypted with.

    input: string, int

    output: string
    """
    return encrypt(cipher, -key)


def count_words(text):
    """"
    A function that takes in a string and returns how many real english worlds it found in that string.

    input: string

    output: int
    """
    words = text.split()
    word_count = 0
    for i in words:
        clean_word = re.sub(r'[^A-Za-z]', ' ', i)
        if clean_word.lower() in word_list or clean_word in name_list:
            word_count += 1
    return word_count

def crack(cipher: str):
    """"
    A function that takes in a cipher string and returns it decrypted without the need of a key.

    input: string

    output: string
    """
    text = ''
    for i in range(26):
        total_words = decrypt(cipher, i)
        word_count = count_words(total_words)
        ratio = word_count / len(total_words.split())
        percentage = int(ratio * 100)
        if percentage > 50:
            text += total_words
    return text


if __name__ == "__main__":
    print(word_list)
    print(name_list)