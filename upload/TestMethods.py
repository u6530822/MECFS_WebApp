import unittest
from .ImageToText import ImageToText


class TestMethods(unittest.TestCase):

    attributes_list = ['Sodium', 'Potassium', 'Chloride', 'Bicarbonate', 'Urea', 'Creatinine', 'eGFR', 'T.Protein',
                       'Albumin', 'ALP', 'Bilirubin', 'GGT', 'AST', 'ALT', 'HAEMOGLOBIN', 'RBC', 'PCV', 'MCV', 'MCHC',
                       'RDW', 'wcc', 'Neutrophils', 'Lymphocytes', 'Monocytes', 'Eosinophils', 'Basophils', 'PLATELETS',
                       'ESR', 'Req. No.', 'Ref. Range', 'Lab No.', 'PTH', 'Vitamin D']

    # check for adjacent character value
    def test_extract_value_from_the_same_line(self):
        for i in range(len(self.attributes_list)):
            text = self.attributes_list[i] + " " + str(i)
            text_local = [text, 'This is line two', 'This is line three']
            val_local = 0
            if self.attributes_list[i] == 'Req. No.':
                attribute = 'ReqNo'
            elif self.attributes_list[i] == 'Ref. Range':
                attribute = 'RefRange'
            elif self.attributes_list[i] == 'Lab No.':
                attribute = 'LabNo'
            elif self.attributes_list[i] == 'Vitamin D':
                attribute = 'VitaminD'
            else:
                attribute = self.attributes_list[i]
            output = str(i)
            self.assertEqual(ImageToText.extract_value(self, text_local, val_local, attribute), output)

    # check for next line character value
    def test_extract_value_from_next_line(self):

        for i in range(len(self.attributes_list)):
            text = self.attributes_list[i] + " " + "No value"
            text_local = [text, str(i), 'This is line three']
            val_local = 0
            if self.attributes_list[i] == 'Req. No.':
                attribute = 'ReqNo'
            elif self.attributes_list[i] == 'Ref. Range':
                attribute = 'RefRange'
            elif self.attributes_list[i] == 'Lab No.':
                attribute = 'LabNo'
            elif self.attributes_list[i] == 'Vitamin D':
                attribute = 'VitaminD'
            else:
                attribute = self.attributes_list[i]
            output = str(i)
            self.assertEqual(ImageToText.extract_value(self, text_local, val_local, attribute), output)

    # check for next line character value
    def test_extract_value_with_symbol_same_line(self):
        text_local = [['Vitamin D > 200 Value > 20', '300 Value > 30'],
                      ['Vitamin D * 400 Value > 40', '500 Value > 50'],
                      ['Vitamin D < 600 Value > 60', '700 Value > 70']]
        val_local = 0
        attribute = 'VitaminD'
        output = ['200', '400', '600']
        for i in range(len(text_local)):
            self.assertEqual(ImageToText.extract_value(self, text_local[i], val_local, attribute), output[i])

    # check for next line character value
    def test_extract_value_with_symbol_next_line(self):
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

    def test_error_case_imperfect_attribute_recognition(self):
        text_local = ['Vitamin Db', '100', 'This is line three']
        val_local = 0
        attribute = 'VitaminD'
        output = 'N/A'
        self.assertEqual(ImageToText.extract_value(self, text_local, val_local, attribute), output)


def suite():

    test_suite = unittest.TestSuite()

    test_suite.addTests(

        unittest.TestLoader().loadTestsFromTestCase(TestMethods)

    )

    return test_suite


if __name__ == '__main__':

    unittest.TextTestRunner(verbosity=2).run(suite())
