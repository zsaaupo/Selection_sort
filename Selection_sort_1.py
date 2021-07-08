"""
selection sort 1
"""
print(__doc__)

class SelectionSort():

    def selection_sort(self, list_01 = []):

        self.list_01 = list_01

        for i in range(len(list_01) - 1):

            minimum_value_index = i

            for j in range(i + 1, len(list_01)):

                if list_01[minimum_value_index] > list_01[j]:

                    minimum_value_index = j
                
            if i != minimum_value_index:

                temp = list_01[i]
                list_01[i] = list_01[minimum_value_index]
                list_01[minimum_value_index] = temp

obj_01 = SelectionSort()

obj_01.selection_sort([50, 95, 24, 58, 10, 57, 26])
print(obj_01.list_01)
