def get_words(text):
    words = []
    word = ""
    for symbol in text:
        if symbol.isalpha():
            word += symbol
        elif word:
            words.append(word)
            word = ""
    return words

def delete_repeats(list):
    result = []
    for element in list:
        if element not in result:
            result.append(element)
    return result

with open("text.txt", "r") as file:
    text = file.read()

words = get_words(text)

words = list(map(lambda x: x.upper(),words))
counters = []
for word in words:
    counters.append([word,words.count(word)])
   
counters = delete_repeats(counters)
counters.sort(key = lambda x: x[1], reverse = True)

max = counters[0][1]
i = 0
while counters[i][1] == max:
    print(counters[i][0])
    i += 1
    



