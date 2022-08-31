def odd_honest():
    i = 0
    while True:
        i+=1
        yield (i, 'нечет' if i % 2 else 'чет')

number = int(input("Enter the number:\n"))

for i in odd_honest():
    if i[0] > number: break
    print(i)