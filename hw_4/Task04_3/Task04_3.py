def get_words(text):
    words = set()
    word = ""
    for symbol in text:
        if symbol.isalpha():
            word += symbol
        elif word:
            words.add(word)
            word = ""
    return words

with open("text1.txt", "r") as file:
    text1 = file.read()

with open("text2.txt", "r") as file:
    text2 = file.read()

words1 = get_words(text1)
words2 = get_words(text2)

result = words1 & words2

print(result)