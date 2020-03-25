class AlgebraicPosition:
    def __init__(self, column, row):
        AlgebraicPosition.raiseIfArgumentsAreInvalid(column, row)
        self.column = column
        self.row = row
        
    def raiseIfArgumentsAreInvalid(column, row):
        if (not AlgebraicPosition.validateColumn(column) or not AlgebraicPosition.validateRow(row)):
            raise ValueError("Only positions in Algebraic Notation are accepted. (e.g. B3)")

    def validateColumn(column):
        if(len(column) != 1):
            return False
        charcode = ord(column)
        isValidLetter = (charcode >= 65 and charcode <= 72) or (charcode >= 97 and charcode <= 104)
        return isValidLetter

    def validateRow(row):
        try:
            return row >= 1 and row <= 8
        except TypeError:
            raise ValueError("Row needs to be a integer")

    def columnToInteger(column):
        if(not AlgebraicPosition.validateColumn(column)):
            raise ValueError("Invalid column")
        charcode = ord(column)
        if (charcode <= 72):
            return charcode - 64
        return charcode - 96

    def integerToColumn(value):
        column = chr(value + 64)
        if(AlgebraicPosition.validateColumn(column)):
            return column
        raise ValueError("Invalid column")
