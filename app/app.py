from flask import Flask, jsonify, request
import logging as logger



logger.basicConfig(level="DEBUG")

app = Flask(__name__)

if __name__ == '__main__':
    logger.debug("Starting the Application and it smells")
    from api_things import *
    app.run(host="0.0.0.0", port=5000, debug = True)