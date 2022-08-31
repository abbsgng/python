def is_prime(number):
    if number == 1:
        return False
    i = 2
    while i < number:
        if not number % i:
            return False
        i+=1
    return True

def prime():
    i = 2
    while True:
        if is_prime(i):
            yield i
        i+=1

number = int(input("Enter the number:\n"))

for i in prime():
    if i > number: break
    print(i)