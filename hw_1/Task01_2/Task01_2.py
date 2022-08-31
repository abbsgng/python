string = input("Input the string\n")
symbol = input("Input the symbol\n")

print(f'Буква {symbol} встречается в строке {string}' if symbol in string
      else f'Буква {symbol} не встречается в строке {string}')
