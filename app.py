from flask import Flask, jsonify, request
import logging as logger


logger.basicConfig(level="DEBUG")

app = Flask(__name__)