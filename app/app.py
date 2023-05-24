# from flask import Flask, jsonify, request
# import logging as logger
# from api_things import *


# logger.basicConfig(level="DEBUG")

# app = Flask(__name__)

# if __name__ == '__main__':
#     logger.debug("Starting the Application and it smells")
    
#     app.run(host="0.0.0.0", port=5000, debug = True)


from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

fakedb = {
    1:{'urmom' : "not stacy's"},
    2:{'wow' : "that smells"},
    3:{'flower' : "smells but like not in the same way"},
    4:{'poo' : "not stacy's"},
}

class Items(Resource):
    def get(self):
        return fakedb
    

class Item(Resource):
    def get(self, pk):
        return fakedb[pk]
    
api.add_resource(Items, '/')
api.add_resource(Item, '/<int:pk>')

if __name__ == '__main__':
    app.run(debug=True)