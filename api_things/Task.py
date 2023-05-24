from flask_restful import Resource
import logging as logger

class Task(Resource):

    def get(self):
        logger.debug("Get some bruh")
        return {"message" : "Get some bruh"}, 200

    def post(self):
        logger.debug("post some bruh")
        return {"message" : "post some bruh"}, 200

    def put(self):
        logger.debug("put some bruh")
        return {"message" : "put some bruh"}, 200

    def delete(self):
        logger.debug("delete some bruh")
        return {"message" : "delete some bruh"}, 200