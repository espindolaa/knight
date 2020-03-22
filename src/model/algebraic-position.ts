export class AlgebraicPosition {
    column: string;
    row: number;

    constructor(column: string, row: number) {
        if(!this._areParamsValid(column, row)) {
            throw "Invalid arguments for algebraic notation";
        }
        this.column = column;
        this.row = row;
    }

    private _areParamsValid(column: string, row: number): boolean {
        return this._isColumnValid(column) && this._isRowValid(row);
    }

    private _isColumnValid(column: string): boolean {
        if (column.length === 1) {
            return this._isColumnPositionValid(column);
        }
        return false;
    }

    private _isColumnPositionValid(column: string): boolean {
        const upperCaseACode = 65;
        const upperCaseHCode = 72;
        const lowerCaseACode = 97;
        const lowerCaseHCode = 104;
        const columnCode = column.charCodeAt(0);
        return (columnCode >= upperCaseACode && columnCode <= upperCaseHCode)
            || (columnCode >= lowerCaseACode && columnCode <= lowerCaseHCode);
    }

    private _isRowValid(row: number): boolean {
        return row >= 1 && row <=8;
    }
 }