from flask import Flask
app = Flask(__name__)

@app.route('/api/v1/possibleMoves/<position>')
def possible_moves(position):
    return position