import os
from flask import Flask, jsonify
from models.algebraicPosition import AlgebraicPosition
from services.chessService import getValidPositions

app = Flask(__name__)

@app.route('/api/v1/possibleMoves/<position>')
def possible_moves(position):
    if (len(position) != 2) :
        raise ValueError("Only positions in Algebraic Notation are accepted. (e.g. B3)")
    algebraicPosition = AlgebraicPosition(position[0], int(position[1]))
    response = jsonify(list(getValidPositions(algebraicPosition)))
    if 'FLASK_ENV' in os.environ and os.environ['FLASK_ENV'] == 'development':
        response.headers.add('Access-Control-Allow-Origin', '*')
    return response
