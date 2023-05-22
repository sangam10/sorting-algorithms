
class BubbleSort:
    # initialized constructor
    def __init__(self,items):
        self.items =items

    # sorting
    def sort(self):
        # copy items from constructor
        items = self.items.copy()
        # travel through given list
        for i in range(len(items)):
            for j in range(len(items)-i-1):
                if items[j] > items[j+1]:
                    items[j],items[j+1] = items[j+1],items[j]
        return items
