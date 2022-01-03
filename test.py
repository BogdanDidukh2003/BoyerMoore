import unittest

from main import *


class TestBoyerMoore(unittest.TestCase):

    def setUp(self):
        self.template1 = "efer"
        self.input_string1 = "reference"
        self.template2 = "eferefer"
        self.input_string2 = "reference"
        self.template3 = "efereferefer"
        self.input_string3 = "reference"
        self.output1 = 1
        self.output2 = "No template in input string"
        self.output3 = "Template is too long"

    def testBoyerMoore(self):
        self.assertEqual(find_template_occurrence(self.template1, self.input_string1), self.output1)
        self.assertEqual(find_template_occurrence(self.template2, self.input_string2), self.output2)
        self.assertEqual(find_template_occurrence(self.template3, self.input_string3), self.output3)


if __name__ == "__main__":
    unittest.main()
