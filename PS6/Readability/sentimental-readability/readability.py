from cs50 import get_string
import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize

def main():
    text = get_string("Enter text: ")
    letters = count_letters(text)
    words = len(text.split())
    sentences = len(sent_tokenize(text))

    avg_letters = (letters * 100) / words
    avg_sentences = (sentences * 100) / words
    x = ((0.0588 * avg_letters) -(0.296 * avg_sentences)) - 15.8

    coleman_liau(x)

def count_letters(text):
    counter = 0
    for element in range(0, len(text)):
        if text[element].isalpha():
            counter += 1

    return counter

def coleman_liau(x):
    if x < 1:
        print("Before Grade 1")
    elif x > 1 and x < 16:
        x = round(x)
        print(f"Grade {x}")
    else:
        print("Grade 16+")

main()