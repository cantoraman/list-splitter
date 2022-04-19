# test_list_splitter.py

import imp
import unittest

from os.path import dirname, join

list_splitter = imp.load_source('list_splitter', join(dirname(__file__), 'list_splitter.py'))

class TestListSplitter(unittest.TestCase):

    def test_split_list_into_chunks(self):
        list_splitter_output = list_splitter.list_split([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3)
        self.assertEqual(list_splitter.list_split([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3), [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10]])
        self.assertEqual(list_splitter.list_split([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 4), [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10]])
        self.assertEqual(list_splitter.list_split([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5), [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
        self.assertEqual(list_splitter.list_split([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 6), [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10]])
        self.assertEqual(list_splitter.list_split([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 7), [[1, 2, 3, 4, 5, 6, 7], [8, 9, 10]])
        self.assertEqual(list_splitter.list_split([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 8), [[1, 2, 3, 4, 5, 6, 7, 8], [9, 10]])
        self.assertEqual(list_splitter.list_split([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 9), [[1, 2, 3, 4, 5, 6, 7, 8, 9], [10]])

if __name__ == '__main__':
    unittest.main()