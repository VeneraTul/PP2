def unique_(list):
    uniq = []
    for elem in list:
        if elem not in uniq:
            uniq.append(elem)
    return uniq

list = [1, 2, 2, 3, 4, 4, 5]
print(unique_(list))