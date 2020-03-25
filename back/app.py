from flask import Flask, jsonify
from models.algebraicPosition import AlgebraicPosition
from services.chessService import getValidPositions

app = Flask(__name__)

@app.route('/api/v1/possibleMoves/<position>')
def possible_moves(position):
    if (len(position) != 2) :
        raise ValueError("Only positions in Algebraic Notation are accepted. (e.g. B3)")
    algebraicPosition = AlgebraicPosition(position[0], int(position[1]))
    return jsonify(getValidPositions(algebraicPosition))
