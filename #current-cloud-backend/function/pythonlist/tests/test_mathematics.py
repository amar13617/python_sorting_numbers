import unittest
from ..src.index import handler


class Test_Mathematics(unittest.TestCase):
    def setUp(self):
        super().setUp()

    def test_sum(self):
        output = handler({"operation": "find_sum", "data1": [1, 2, 3]}, None)
        self.assertEqual(output["find_sum"],6)

    def test_average(self):
        output = handler({"operation": "find_average", "data1": [1, 2, 3]}, None)
        self.assertEqual(output["average"],2)
        output = handler({"operation": "find_average", "data1": []}, None)
        self.assertEqual(output["average"],0)
        self.assertListEqual([1] , [1])

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')
    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_positive(self):
        firstValue = "geeks"
        secondValue = "geeks"
        message = "First value and second value are not equal !"
        self.assertEqual(firstValue, secondValue, message)
    
    def test_square(self):
        output = handler({"operation": "find_square", "data1": [2,3,4,5]}, None)
        self.assertEqual(output["find_square"],[4,9,16,25])
    
    def test_multiply(self):
        output = handler({"operation": "find_multiply", "data1": [1, 2, 3, 4]}, None)
        self.assertEqual(output["multiply_list"],24)

    def test_maximum(self):
        output = handler({"operation": "find_maximum", "data1": [2,3,4,5,1,7,23,10]}, None)
        self.assertEqual(output["find_maximum"], 23)
    def test_minimum(self):
        output = handler({"operation": "find_minimum", "data1": [2,3,4,5,1,7,23,10]}, None)
        self.assertEqual(output["find_minimum"], 1)

    def test_prime(self):
        output = handler({"operation": "find_prime", "data1": [2,5,7,23]}, None)
        self.assertListEqual(output["prime_number"], [2,5,7,23])


    def test_second_maximum(self):
        output = handler({"operation": "second_largest", "data1": [2,3,4,5,1,7,23,10]}, None)
        self.assertEqual(output["second largest"], 10)
        
    
    
    
    
        
    
    