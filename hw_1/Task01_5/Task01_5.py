def gcd(number1, number2):
    if(not number1 or not number2):
        return number1 if number1 > number2 else number2
    if(number1 == number2):
        return number1
    if number1 > number2:
        number1%=number2
    else: 
        number2%=number1
    return gcd(number1, number2)



number1 = int(input("Input number\n"))
number2 = int(input("Input number\n"))
print(f'{number1} и {number2} являются взаимно простыми' if gcd(number1, number2) == 1
      else f'{number1} и {number2} не являются взаимно простыми')
