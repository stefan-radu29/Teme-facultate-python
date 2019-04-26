class Bag:
    # creates a new, empty Bag
    def __init__(self):
        # theta(1)
        self.__elements = []
        self.__frequency = []

    # adds a new element to the Bag
    def add(self, e):
        #O(n)
        for index in range(0, len(self.__elements)):
            if self.__elements[index] == e:
                self.__frequency[index] += 1
                return
        self.__elements.append(e)
        self.__frequency.append(1)

    # removes one occurrence of an element from a Bag
    # returns True if an element was actually removed (the Bag contained the element e), or False if nothing was removed
    def remove(self, e):
        #O(n)
        for index in range(0, len(self.__elements)):
            if self.__frequency[index] == 1 and self.__elements[index] == e:
                self.__elements.pop(index)
                self.__frequency.pop(index)
                return True
            elif self.__frequency[index] > 1 and self.__elements[index] == e:
                self.__frequency[index] = self.__frequency[index] - 1
                return True
        return False

    # searches for an element e in the Bag
    # returns True if the Bag contains the element, False otherwise
    def search(self, e):
        #O(n)
        if e in self.__elements:
            return True
        return False

    # counts and returns the number of times the element e appears in the bag
    def nrOccurrences(self, e):
        #O(n)
        for index in range(0, len(self.__elements)):
            if self.__elements[index] == e:
                return self.__frequency[index]
        return 0

    # returns the size of the Bag (the number of elements)
    def size(self):
        #theta(n)
        size = 0
        for frequency in self.__frequency:
            size = size + frequency
        return size

    # returns True if the Bag is empty, False otherwise
    def isEmpty(self):
        #theta(1)
        if len(self.__elements) == 0:
            return True
        return False

    # returns a BagIterator for the Bag
    def iterator(self):
        #theta(1)
        return BagIterator(self)

class BagIterator:
    # creates an iterator for the Bag b, set to the first element of the bag, or invalid if the Bag is empty
    def __init__(self, b):
        #theta(1)
        self.__iterate_elements = b._Bag__elements
        self.__iterate_frequencies = b._Bag__frequency
        self.__current_index = 0
        self.__current_frequency = 1


    # returns True if the iterator is valid
    def valid(self):
        #theta(1)
        return self.__current_index < len(self.__iterate_elements) and self.__current_frequency <= self.__iterate_frequencies[self.__current_index]

    # returns the current element from the iterator.
    # throws ValueError if the iterator is not valid
    def getCurrent(self):
        #theta(1)
        if self.valid() is False:
            raise ValueError("invalid iterator")
        else:
            return self.__iterate_elements[self.__current_index]

    # moves the iterator to the next element
    # throws ValueError if the iterator is not valid
    def next(self):
        #theta(1)
        if self.valid() is False:
            raise ValueError("invalid iterator")
        else:
            if self.__current_frequency < self.__iterate_frequencies[self.__current_index]:
                self.__current_frequency += 1
            else:
                self.__current_index += 1
                self.__current_frequency = 1

    # sets the iterator to the first element from the Bag
    def first(self):
        #theta(1)
        self.__current_index = 0
        self.__current_frequency = 1