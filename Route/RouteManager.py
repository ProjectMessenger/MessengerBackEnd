from . import routes
from flask import request

@routes.route("/")
def Hello():
	return "Hello World!"

@routes.route("/messenger/v1.0.0/send/<uploaderName>", methods=['POST'])
def MessageSend(uploaderName):
	print uploaderName, ": ", request.data
	return "Ok"
	