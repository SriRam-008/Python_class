from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class CSK(Resource):
    list = []

    def get(self):
        return {"players": CSK.list}

    def post(self):
        data = request.get_json() 
        player = data.get('player') 
        CSK.list.append(player)
        return {"message": f"Player {player} added successfully!"}, 
    def delete(self):
        data = request.get_json()
        player = data.get('player')
        CSK.list.remove(player)  # Simply removes the player (no checks or exception handling)
        return {"message": f"Player {player} removed successfully!"}, 200


api.add_resource(CSK, '/csk')

if __name__ == '__main__':
    app.run(debug=True)

