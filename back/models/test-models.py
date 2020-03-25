import unittest
from algebraicPosition import AlgebraicPosition

class TestAlgebraicModel(unittest.TestCase):

    validColumn = 'A'
    invalidColumn = 'R'
    validRow = 1
    invalidRow = -1

    def test_should_create_algebraic(self):
        position = AlgebraicPosition(self.validColumn, self.validRow)
        self.assertIsInstance(position, AlgebraicPosition)
        self.assertEqual(self.validColumn, position.column)
        self.assertEqual(self.validRow, position.row)

    def test_should_fail_with_invalid_column(self):
        self.assertRaises(ValueError, lambda: AlgebraicPosition(self.invalidColumn, self.validRow))

    def test_should_fail_without_column(self):
        self.assertRaises(ValueError, lambda: AlgebraicPosition('', self.validRow))

    def test_should_fail_with_invalid_row(self):
        self.assertRaises(ValueError, lambda: AlgebraicPosition(self.validColumn, self.invalidRow))

    def test_should_fail_without_row(self):
        self.assertRaises(ValueError, lambda: AlgebraicPosition(self.validColumn, ''))

    def test_should_convert_to_column(self):
        column = AlgebraicPosition.integerToColumn(1)
        self.assertEqual(column, self.validColumn)

    def test_should_not_convert_invalid_integer(self):
        self.assertRaises(ValueError, lambda: AlgebraicPosition.integerToColumn(-1))

    def test_should_convert_to_integer(self):
        integer = AlgebraicPosition.columnToInteger(self.validColumn)
        self.assertEqual(1, integer)

    def test_should_not_convert_invalid_column(self):
        self.assertRaises(ValueError, lambda: AlgebraicPosition.columnToInteger(self.invalidColumn))


if __name__ == '__main__':
    unittest.main()