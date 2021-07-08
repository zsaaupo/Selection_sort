"""
selection sort 3
"""
print(__doc__)

class SelectionSort3():

    def selection_sort(self, list_03):

        for i in range(len(list_03) - 1):

            curry = i

            for j in range(i+1 , len(list_03)):

                if list_03[curry] > list_03[j]:

                    curry = j

            if i != curry:

                selected_index = list_03[i]
                list_03[i] = list_03[curry]
                list_03[curry] = selected_index

        return list_03

obj_03 = SelectionSort3()
print(obj_03.selection_sort([52, 42, 35, 26, 19, 10, 9, 5, 1]))
