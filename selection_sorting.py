class SelectionSort:
    # initialized constructor
    def __init__(self,array):
        self.items = array

    # copy array items
    def copy(self):
        return self.items.copy()

    # sort function
    def sort(self):
        items = self.copy()
        if len(items) == 0:
            return None
        for i in range(len(items)):
            min_idx = i

            for j in range(i+1,len(items)):
                if items[min_idx] > items[j]:
                    min_idx = j
            # swap
            items[i],items[min_idx] = items[min_idx],items[i]
        return items
