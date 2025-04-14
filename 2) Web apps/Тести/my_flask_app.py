import flask
from flask import Flask, jsonify

app = Flask(__name__)

users_db = {
    'user1': {'name': 'Alice', 'role': 'admin'},
    'user2': {'name': 'Bob', 'role': 'user'}
}

@app.route('/api/users/<username>', methods = ['GET'])
def get_user(username):
    user = users_db.get(username)


    if user:
        return jsonify({'username': username, 'data': user}), 200
    return jsonify({'error': 'User not found'}), 404
if __name__ == '__main__':
    app.run(debug=True)