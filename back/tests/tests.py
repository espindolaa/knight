import sys
import unittest
sys.path.append("..")

from models.algebraicPosition import AlgebraicPosition
from services.chessService import *

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
    
class TestChessService(unittest.TestCase):

    def test_should_get_row_from_algebraic(self):
        position = AlgebraicPosition('A', 1)
        index = getMatrixRoxFromAlgebraic(position)
        self.assertEqual(0, index)

    def test_should_get_column_from_algebraic(self):
        position = AlgebraicPosition('A', 1)
        index = getMatrixColumnFromAlgebraic(position)
        self.assertEqual(0, index)

    def test_should_be_inside_board(self):
        column = 1 
        row = 1
        isInside = isInsideBoard(column, row)
        self.assertTrue(isInside)

    def test_column_should_be_smaller_than_board(self):
        column = -1
        row = 1
        isInside = isInsideBoard(column, row)
        self.assertFalse(isInside)

    def test_column_should_be_bigger_than_board(self):
        column = 10
        row = 1
        isInside = isInsideBoard(column, row)
        self.assertFalse(isInside)

    def test_row_should_be_smaller_than_board(self):
        column = 1
        row = -1
        isInside = isInsideBoard(column, row)
        self.assertFalse(isInside)

    def test_row_should_be_bigger_than_board(self):
        column = 1
        row = 10
        isInside = isInsideBoard(column, row)
        self.assertFalse(isInside)

    def test_should_get_possible_moves_A1(self):
        possibleMoves = set([('D', 4), ('A', 3), ('C', 5), ('E', 1), ('D', 2), ('C', 1), ('A', 5), ('E', 3), ('B', 4), ('A', 1)])
        position = AlgebraicPosition('A', 1)
        result = getValidPositions(position)
        self.assertEqual(possibleMoves, result)

    def test_should_get_possible_moves_A8(self):
        possibleMoves = set([('D', 5), ('E', 8), ('E', 6), ('B', 5), ('C', 4), ('A', 4), ('A', 8), ('A', 6), ('D', 7), ('C', 8)])
        position = AlgebraicPosition('A', 8)
        result = getValidPositions(position)
        self.assertEqual(possibleMoves, result)

    def test_should_get_possible_moves_H1(self):
        possibleMoves = set([('H', 1), ('G', 4), ('F', 1), ('H', 3), ('D', 3), ('E', 2), ('D', 1), ('F', 5), ('H', 5), ('E', 4)])
        position = AlgebraicPosition('H', 1)
        result = getValidPositions(position)
        self.assertEqual(possibleMoves, result)

    def test_should_get_possible_moves_H8(self):
        possibleMoves = set([('E', 5), ('G', 5), ('E', 7), ('H', 8), ('F', 8), ('D', 8), ('F', 4), ('H', 4), ('H', 6), ('D', 6)])
        position = AlgebraicPosition('H', 8)
        result = getValidPositions(position)
        self.assertEqual(possibleMoves, result)

    def test_should_get_possible_moves_D4(self):
        possibleMoves = set([('A', 3), ('B', 8), ('C', 7), ('F', 4), ('C', 3), ('G', 3), ('E', 5), ('G', 7), ('E', 1), ('A', 5), ('H', 6), ('A', 1), ('D', 4), ('C', 5), ('H', 2), ('D', 8), ('C', 1), ('G', 1), ('G', 5), ('E', 7), ('F', 8), ('D', 2), ('E', 3), ('H', 4), ('A', 7), ('B', 4), ('D', 6)])
        position = AlgebraicPosition('D', 4)
        result = getValidPositions(position)
        self.assertEqual(possibleMoves, result)


if __name__ == '__main__':
    unittest.main()