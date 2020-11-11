import unittest
from unittest import mock

import myLibrary


class Test_myLibrary(unittest.TestCase):

    def test_inputInt(self):
        """
        Test that inputInt() only accepts integers that are in bounds
        """
        inputs = (
            'not an int',
            '-100',
            '100',
            '1.0',
            '5',
        )
        with mock.patch('builtins.input', side_effect=inputs):
            self.assertEqual(myLibrary.inputInt('', -10, 10), 5)

    def test_inputFloat(self):
        """
        Test that inputFloat() will only accept floats
        """
        with mock.patch('builtins.input', side_effect=('not a float', '5.5')):
            self.assertEqual(myLibrary.inputFloat(''), 5.5)

    def test_inputNonZeroFloat(self):
        """
        Test that inputNonZeroFloat() will only accept non-zero floats
        """
        with mock.patch('builtins.input', side_effect=('0', '5.5')):
            self.assertEqual(myLibrary.inputNonZeroFloat(''), 5.5)

    def test_bubble(self):
        """
        Tests that bubble() can actually sort a list
        """
        l = [5, 4, 3, 2, 1]
        myLibrary.bubble(l)
        self.assertEqual(l, [1, 2, 3, 4, 5])

    def test_calculateY(self):
        """
        Tests if calculateY() can do basic maths
        """
        with mock.patch('builtins.print', lambda s: self.assertEqual(s, 'Where x = 2, y = 10')):
            myLibrary.calculateY(2, 3, 4)

    def test_testLab1(self):
        """
        """

        # Asserts that x always equals y
        def testOutput(s):
            l = s.split()
            self.assertEqual(l[3][:-1], l[6])

        inputs = (
            1, 0,  # These ensure that x should always equal y
            11,  # Arbitrary value for x
        )
        with mock.patch('builtins.input', side_effect=inputs):
            with mock.patch('builtins.print', testOutput):
                myLibrary.testLab1()

    def test_chartList(self):
        """
        Tests chartList() by checking each line of the output when given a list of all digits 0-9
        """
        # Collects up all the output lines
        outputs = []
        def captureOutput(s):
            outputs.append(s)

        # Capture that output
        with mock.patch('builtins.print', captureOutput):
            myLibrary.chartList([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

        # Header and footer, really shouldn't be wrong ;)
        self.assertEqual(outputs[0], '| 0 1 2 3 4 5 6 7 8 9')
        self.assertEqual(outputs[-1], '| 0 1 2 3 4 5 6 7 8 9')

        # Checks the actual 'bars' of the chart
        for n, s in enumerate(outputs[1:-1]):
            self.assertEqual(s, '|-' + ('--' * n) + 'X')

    def test_linear(self):
        """
        Test linear() with simple values for m & c, not much to go wrong really
        """
        self.assertEqual(myLibrary.linear(2, 3), -1.5)

    def test_quadSolver(self):
        """
        Test quadSolver() with a solvable and 'unsolvable' quadratic
        """
        # Solvable
        self.assertEqual(myLibrary.quadSolver(1, 5, 6), [-2, -3])

        # Unsolvable
        with mock.patch('builtins.print', lambda _: None):  # lambda eats print() calls nomnom
            self.assertIsNone(myLibrary.quadSolver(1, 4, 6))

        # TODO: Could check that an actual error is printed, though really it could take any form

    def test_getUser(self):
        """
        Tests getUser() by feeding it a few numbers and checking they come out cleanly in the returned list
        """
        inputs = ('1', '2', '3', '4', '5')
        with mock.patch('builtins.input', side_effect=inputs):
            self.assertEqual(myLibrary.getUser(5), [1, 2, 3, 4, 5])

    def test_getAv(self):
        """
        Tests that getAv() can correctly calculate mean & median of lists, of odd & even length.
        Uses the fibonacci sequence for the lists, because why not.
        """
        self.assertEqual(myLibrary.getAv([1, 1, 2, 3, 5]), [12/5, 2])
        self.assertEqual(myLibrary.getAv([1, 1, 2, 3, 5, 8]), [20/6, 5/2])

    def test_slicer(self):
        """
        Tests slicer with mean > median, median > mean, and median == mean
        """
        # Mean > median
        self.assertEqual(myLibrary.slicer([1, 2, 3, 4, 10]), [10, 4, 3, 2, 1])
        # Median > mean & median == mean
        self.assertEqual(myLibrary.slicer([1, 2, 3, 4, -10]), [2, 4])
        self.assertEqual(myLibrary.slicer([1, 2, 3, 4, 5]), [2, 4])


if __name__ == '__main__':
    unittest.main()
