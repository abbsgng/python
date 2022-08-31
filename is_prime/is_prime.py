def is_prime(number):
    if number == 1:
        return False
    i = 2
    while i < number:
        if not number % i:
            return False
        i+=1
    return True

