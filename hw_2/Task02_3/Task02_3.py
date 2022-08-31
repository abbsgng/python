def factorials(number:int):
    if number == 1:
        factorial = 1
    else:
        i = yield from factorials(number - 1)
        factorial = number * i
    yield factorial
    return factorial

number = int(input("Enter the number:\n"))

for i in factorials(number):
    print(i)
