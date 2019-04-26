import unittest

'''
Module containing iterable data structure, a sort method and a filter method.
'''

'''
Class containing an iterable data structure
'''
class My_iterable_data_structure:
    def __init__(self):
        self._data = []

    def __next__(self):
        if self._index < len(self._data):
            self._index += 1
            return self._data[self._index]
        else:
            raise StopIteration

    def __iter__(self):
        self._index = 0
        return iter(self._data)

    def __delitem__(self, key):
        if 0 <= key < len(self._data):
            del self._data[key]
        else:
            raise My_iterable_data_structure_exception("Index out of range!")

    def __setitem__(self, key, value):
        if 0 <= key < len(self._data):
            self._data[key] = value
        else:
            raise My_iterable_data_structure_exception("Index out of range!")

    def __len__(self):
        return len(self._data)

    def __getitem__(self, key):
        if 0 <= key < len(self._data):
            return self._data[key]
        else:
            raise My_iterable_data_structure_exception("Index out of range!")

    def __reversed__(self):
        return reversed(self._data)

    def __str__(self):
        return str(self._data)

    def append(self, item):
        self._data.append(item)

    def remove(self, item):
        self._data.remove(item)

'''
Gnome sort function and filter.
'''

def gnome_sort(a_list, function_for_comparison=lambda a: a):
    position = 0
    while position < len(a_list):
        if position == 0 or function_for_comparison(a_list[position]) >= function_for_comparison(a_list[position - 1]):
            position += 1
        else:
            a_list[position], a_list[position - 1] = a_list[position - 1], a_list[position]
            position -= 1

def filter(a_list, function_for_filter):
    filtered_list = []
    for item in a_list:
        if function_for_filter(item) == True:
            filtered_list.append(item)
    return filtered_list

'''
Exception for this iterable data structure class
'''
class My_iterable_data_structure_exception(Exception):
    pass

'''
Unittests for the iterable data structure class
'''

class Test_my_iterable_data_structure(unittest.TestCase):

    def setUp(self):
        self.values = My_iterable_data_structure()
        self.values.append(1)
        self.values.append(2)
        self.values.append(3)
        self.list = [[1, 2], [0, 0], [10, 10], [4, 1]]

    def tearDown(self):
        self.values = None
        self.list = None

    def test_append_and_remove(self):
        self.values.append(4)
        self.assertEqual(len(self.values), 4)
        self.values.append(5)
        self.values.append(6)
        self.assertEqual(len(self.values), 6)
        self.assertEqual(self.values[1], 2)
        self.values.remove(2)
        self.assertEqual(len(self.values), 5)
        self.assertEqual(self.values[1], 3)

    def test_iter(self):
        index=1
        for value in self.values:
            self.assertEqual(value, index)
            index += 1

    def test_gnome_sort(self):
        gnome_sort(self.list, lambda a: a[0] + a[1])
        self.assertEqual(self.list, [[0,0], [1, 2], [4, 1], [10, 10]])
        self.values.append(0)
        self.values.append(-3)
        gnome_sort(self.values)
        self.assertEqual(str(self.values), "[-3, 0, 1, 2, 3]")

    def test_filter(self):
        filtered_list = filter(self.list, lambda a: (a[0] + a[1]) % 2 == 0)
        self.assertEqual(filtered_list, [[0, 0], [10, 10]])
        self.values.append(4)
        self.values.append(5)
        self.values.append(6)
        filtered_iterable_structure = filter(self.values, lambda a: a % 2 != 0)
        self.assertEqual(filtered_iterable_structure, [1, 3, 5])