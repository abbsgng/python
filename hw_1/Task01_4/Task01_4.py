def is_prime(number):
    if number == 1:
        return False
    i = 2
    while i < number :
        if number % i == 0:
            return False
        i+=1
    return True

number = int(input("Input the number\n"))
sum, i = 0, 1

while i <= number:
    if number % i == 0:
        sum = sum + i if is_prime(i) else sum
        number/=i
    i+=1
print(sum if sum else "Простых делитей нет")
