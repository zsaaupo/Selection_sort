"""
Selection sort
"""
print(__doc__)

list_01 = [9, 8, 7, 6, 5, 4, 3, 2, 1]

for i in range(len(list_01) - 1):

    sort_index = i

    for j in range(i + 1, len(list_01)):

        if list_01[j] < list_01[sort_index]:
            sort_index = j
    
    if sort_index != i:

        temp = list_01[i]
        list_01[i] = list_01[sort_index]
        list_01[sort_index] = temp


print(list_01)