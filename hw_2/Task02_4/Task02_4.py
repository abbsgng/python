
def first_digit(number: int):
    while number > 9:
        number //= 10
    return number

def length(number: int):
    count = 0
    while number:
        count+=1
        number //= 10
    return count

def is_palindrome(number: int):
    if number == 0:
        return True
    if first_digit(number) != number % 10:
        return False
    return is_palindrome(number % 10 ** (length(number) - 1) // 10) # doesn't work

def reverse(number: int):
    new = 0
    while number:
        new += (number % 10)
        new *= 10
        number //= 10
    return new // 10

number = int(input("Enter the number:\n"))

def palindroms():
    i = 0
    while True:
        yield i * 10 ** length(i) + reverse(i)
        i+=1

for i in palindroms():
    if i > number: break
    print(i)