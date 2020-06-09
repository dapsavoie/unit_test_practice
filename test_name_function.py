import unittest

from name_function import get_formatted_name


class Test(unittest.TestCase):
    def test_first_last_name(self):
        """Do names like 'Tupac Shakur' work?"""

        formatted_name = get_formatted_name('tupac', 'shakur')
        self.assertEqual(formatted_name, 'Tupac Shakur')

    def test_first_last_middle_name(self):
        """Do names like Martin Luther King work?"""
        formatted_name = get_formatted_name('Martin', 'king', 'luther')
        self.assertEqual(formatted_name, 'Martin Luther King')


if __name__ == '__main__':
    unittest.main()