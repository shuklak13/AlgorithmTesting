import examples.insertion_sort
sort = examples.insertion_sort.insertion_sort

import unittest, random
MAX_LIST_LEN = 255
NUM_RAND_TESTS = 255

def random_list():
    num_tests = random.randrange(MAX_LIST_LEN)
    return [random.random() for r in range(num_tests)]

class TestSort(unittest.TestCase):
    def test(self):
        self.assertEqual(sort([]), [])
        print("successfully sorted empty list")

        self.assertEqual(sort([1]), [1])
        print("successfully sorted single-element list")
        self.assertEqual(sort([1, 2, 3]), [1, 2, 3])

        print("successfully sorted already-sorted list")

        self.assertEqual(sort([3, 2, 1]), [1, 2, 3])
        print("successfully sorted reverse-sorted list")

        for i in range(NUM_RAND_TESTS):
            self.assertTrue(self.is_sorted(sort(random_list())))
        print("successfully sorted", NUM_RAND_TESTS, "random lists")

    def is_sorted(self, lst):
        return all(lst[i] < lst[i+1] for i in range(len(lst)-1))

if __name__ == '__main__':
    unittest.main()