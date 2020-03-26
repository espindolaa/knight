from models.algebraicPosition import AlgebraicPosition

def getValidPositions(algebraicPosition):
    matrix = getDefaultMatrix()
    column = getMatrixColumnFromAlgebraic(algebraicPosition)
    row = getMatrixRoxFromAlgebraic(algebraicPosition)
    numberOfMoves = getNumberOfMoves()

    possibleMovesWithDuplicates = findPossibleMoves(matrix, column, row, numberOfMoves)
    possibleMoves = set([item for sublist in possibleMovesWithDuplicates for item in sublist])
    possibleMovesAlgebraic = getAlgebraicSetFromIndexSet(possibleMoves)
    return possibleMovesAlgebraic

def findPossibleMoves(board, column, row, amoutOfMoves):
    positions = []
    possibleMovements = getPossibleMovements()

    for movement in possibleMovements:
        newColumn = column + movement[0]
        newRow = row + movement[1]
        if(isInsideBoard(newColumn, newRow)):
            positions.append((newColumn, newRow))
    
    if(amoutOfMoves == 1):
        return positions

    nextPositions = []
    for pos in positions:
        nextPositions.append(findPossibleMoves(board, pos[0], pos[1], amoutOfMoves - 1))
    return nextPositions

def isInsideBoard(column, row):
    return column >= 0 and column <= 7 and row >= 0 and row <= 7

def getMatrixColumnFromAlgebraic(algebraicPosition):
    return AlgebraicPosition.columnToInteger(algebraicPosition.column) - 1

def getMatrixRoxFromAlgebraic(algebraicPosition):
    return algebraicPosition.row - 1

def getAlgebraicValueFromMatrixValue(matrixValue):
    return matrixValue + 1

def getPossibleMovements():
    return [(2, -1), (2, 1), (1, -2), (1, 2), (-2, -1), (-2, 1), (-1, -2), (-1, 2)]

def getAlgebraicSetFromIndexSet(indexSet):
    algebraicSet = set()
    for entry in indexSet:
        column = AlgebraicPosition.integerToColumn(getAlgebraicValueFromMatrixValue(entry[0]))
        row = getAlgebraicValueFromMatrixValue(entry[1])
        algebraicSet.add((column, row))
    return algebraicSet

def getDefaultMatrix():
    cols_count = rows_count = 8
    return [[0 for x in range(cols_count)] for x in range(rows_count)] 

def getNumberOfMoves():
    return 2