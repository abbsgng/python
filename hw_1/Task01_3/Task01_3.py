def sum_digits(number, comparator):
    sum = 0
    for element in number:
        if comparator(element):
            sum+=int(element)
    return sum

number = input("Input the number\n")
print(sum_digits(number, lambda element: element != '.'))