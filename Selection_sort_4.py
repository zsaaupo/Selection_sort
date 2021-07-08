"""
Selection Sort 4
"""
print(__doc__)

class SelectionSort4:

    def __init__(self, list_04):
        self.list_04 = list_04

    def selection_sort(self):

        for i in range(len(self.list_04) - 1):

            min_value_index_number = i

            for j in range(i+1, len(self.list_04)):

                if self.list_04[min_value_index_number] > self.list_04[j]:

                    min_value_index_number = j

            if i != min_value_index_number:

                selected_index = self.list_04[i]
                self.list_04[i] = self.list_04[min_value_index_number]
                self.list_04[min_value_index_number] = selected_index
        
        return self.list_04

object_04 = SelectionSort4([5, 8, 44, 77, 1, 2 ,0, 51 , 92, 110])

print(object_04.selection_sort())