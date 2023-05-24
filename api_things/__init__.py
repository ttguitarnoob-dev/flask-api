from flask_restful import Api
from .Task import Task

from app.app import app

restServer = Api(app)

restServer.add_resource(Task, "/api/v1.0/task")