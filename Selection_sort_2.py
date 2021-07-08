"""
Selection sort 2
"""
print(__doc__)

class SelectionSort2():

    def selection_sort_2(self, list_2):

        self.list_2 = list_2

        for i in range(len(list_2) - 1):

            curry = i

            for j in range(i+1, len(list_2)):
                
                if list_2[curry] > list_2[j]:
                    curry = j

            if i != curry:

                selected_index = list_2[i]
                list_2[i] = list_2[curry]
                list_2[curry] = selected_index

obj_2 = SelectionSort2()
obj_2.selection_sort_2([5, 8, 9, 6, 1, 2, 4, 3])
print(obj_2.list_2)
