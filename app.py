from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class PingPong(Resource):
    def get(self):
        return {"message": "pong"}, 200

api.add_resource(PingPong, '/ping')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
