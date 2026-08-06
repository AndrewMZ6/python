# A pangram is a sentence that contains every single letter of the alphabet at least once.
# For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram,
# because it uses the letters A-Z at least once (case is irrelevant).

# Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.

not_a_pangram = (
    "hello this is my python testing sentence, and it is definitely not a pangram!"
)
pangram_for_sure = "The quick, brown fox jumps over the lazy dog!"
alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]


def is_pangram(sentence: str) -> bool:

    words: list = sentence.split()

    for word in words:
        letters: list = list(word)
        for letter in letters:
            if letter in alphabet:
                alphabet.remove(letter)

    return not alphabet


print(is_pangram(not_a_pangram))
# False
print(is_pangram(pangram_for_sure))
# True
