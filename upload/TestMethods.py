import unittest
from .ImageToText import ImageToText


class TestMethods(unittest.TestCase):

    # check for adjacent character value
    def test_extract_value_from_the_same_line(self):
        text_local = ['Sodium 100', 'Sodium 200', 'Sodium 300']
        val_local = 0
        attribute = 'Sodium'
        output = '100'
        self.assertEqual(ImageToText.extract_value(self, text_local, val_local, attribute), output)

    # check for next line character value
    def test_extract_value_from_next_line(self):
        text_local = ['Vitamin D Vitamin', '200', '300']
        val_local = 0
        attribute = 'VitaminD'
        output = '200'
        self.assertEqual(ImageToText.extract_value(self, text_local, val_local, attribute), output)

    # check for next line character value
    def test_extract_value_with_symbol(self):
        text_local = [['Vitamin D Vitamin A', '> 200 Value > 20', '300 Value > 30'],
                      ['Vitamin D Vitamin A', '* 400 Value > 40', '500 Value > 50'],
                      ['Vitamin D Vitamin A', '< 600 Value > 60', '700 Value > 70']]
        val_local = 0
        attribute = 'VitaminD'
        output = ['200', '400', '600']
        for i in range(len(text_local)):
            self.assertEqual(ImageToText.extract_value(self, text_local[i], val_local, attribute), output[i])

    def test_extract_value_from_different_indexes(self):
        text_local = [['Sodium 100', 'Sodium 200', 'Sodium 300'],
                      ['Sodium 100', 'Sodium 200', 'Sodium 300'],
                      ['Sodium 100', 'Sodium 200', 'Sodium 300']]
        output = ['100', '200', '300']
        val_local = [0, 1, 2]
        attribute = 'Sodium'
        # check for modified character
        for i in range(len(text_local)):
            self.assertEqual(ImageToText.extract_value(self, text_local[i], val_local[i], attribute), output[i])

    def test_error_case_no_value_same_line(self):
        text_local = ['Magnesium Sodium']
        val_local = 0
        attribute = 'Sodium'
        output = 'N/A'
        self.assertEqual(ImageToText.extract_value(self, text_local, val_local, attribute), output)

    def test_error_case_no_value_next_line(self):
        text_local = ['Sodium Magnesium', 'Value: absolute', 'Value: 300']
        val_local = 0
        attribute = 'Sodium'
        output = 'N/A'
        self.assertEqual(ImageToText.extract_value(self, text_local, val_local, attribute), output)


if __name__ == '__main__':
    unittest.main()