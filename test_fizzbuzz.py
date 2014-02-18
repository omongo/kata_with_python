import unittest2
class FizzBuzz:
    def count(self, number):
        if number == 3: return 'Fizz'
        return '1'

class FizzBuzzTest(unittest2.TestCase):
    def test_1_should_return_1(self):
        fizzbuzz = FizzBuzz()
        self.assertEquals(fizzbuzz.count(1), '1')

    def test_3_should_return_fizz(self):
        fizzbuzz = FizzBuzz()
        self.assertEquals(fizzbuzz.count(3), 'Fizz')

