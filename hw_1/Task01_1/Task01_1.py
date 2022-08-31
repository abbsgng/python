def is_correct(string):
    for symbol in string:
        if symbol != '0' and symbol != '1':
            return False 
    return True

string = input("Input the string\n")
counter = 0

if is_correct(string):
    for symbol in string:
       if symbol == '0':
        counter += 1
    print(counter if counter < len(string) - counter else  len(string) - counter)
else: 
    print("Invalid string")


