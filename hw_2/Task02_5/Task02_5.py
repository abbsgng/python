alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def to_decimal(number, system: '2-36'):
   decimal, i = 0, 0
   length = len(number)
   for digit in number:
       if digit in alphabet[10:]:
           decimal += (ord(digit) - ord('A') + 10) * system ** (length - i - 1)
           i += 1
       else:
           decimal += int(digit) * system ** (length - i - 1)
           i += 1
   return decimal

def change_notation(number, current_system, new_system):
   number = to_decimal(number, current_system)
   if number < new_system:
        return alphabet[number]
   else:
        return change_notation(str(number // new_system), 10, new_system) + alphabet[number % new_system]


number = input('Enter the number:\n')
print(change_notation(number, 16, 2))