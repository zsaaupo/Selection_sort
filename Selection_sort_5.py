"""
Selection Sort 5
"""
print(__doc__)

class SelectionSort5:

    def __init__(self, list_05):
        self.list_05 = list_05

    def selection_sort(self):

        for i in range(len(self.list_05) - 1):

            max_value_index = i

            for j in range(i+1, len(self.list_05)):

                if self.list_05[max_value_index] < self.list_05[j]:

                    max_value_index = j

        if i != max_value_index:

            selected_index = self.list_05[i]
            self.list_05[i] = self.list_05[max_value_index]
            self.list_05[max_value_index] = selected_index

        return self.list_05

object_05 = SelectionSort5([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(object_05.selection_sort())