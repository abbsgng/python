alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def from_decimal_integer(number, system):
    module_number = abs(number)
    result = alphabet[module_number % system] 
    while module_number >= system :
        module_number = module_number // system
        result += alphabet[module_number % system] 
    return  ('-' if number < 0 else '') + result[::-1] 
    
def from_decimal_fractional(fractional, system, accuracy=10) :
    result = ''
    while accuracy :
        fractional *= system
        fractional = round(fractional, accuracy)
        result += str(alphabet[int(fractional)])
        fractional -= int(fractional)
        accuracy -= 1
    return result
      
def change_notation(number, current_system, new_system):
    if '.' in number :
        number, fractional = map(str, number.split('.'))
        number = int(number, current_system)
        number = from_decimal_integer(number, new_system)
        result_fractional = 0
        k = current_system
        for i in fractional:
            result_fractional += alphabet.index(i) / k
            k *= current_system
        result_fractional = from_decimal_fractional(result_fractional, new_system)
        return number + '.' + result_fractional
    else :
        return from_decimal_integer(int(number, current_system), new_system)
   
number = '0.96875'

print(change_notation(number,10,2))
    
    

