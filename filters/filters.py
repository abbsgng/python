def filter(source, comparator):
    out = []
    for element in source:
        if comparator(element):
            out.append(element)
    return out

source = [1, 2, 12, 4, 3, 12, 17, 8, 5]
source = filter(source, lambda element: element > 12)
print(source)