from . import routes
from flask import request
from Utils import JsonDataConverter

@routes.route("/")
def Hello():
	return "Hello World!"

@routes.route("/messenger/v1.0.0/send/<uploaderName>", methods=['POST'])
def MessageSend(uploaderName):
	print uploaderName, ": ", JsonDataConverter.GetClientSendToServerMessage(request.data)
	return "Ok"
	
@routes.route("/messenger/v1.0.0/receive/<downloaderName>", methods=['GET'])
def MessageReceive(downloaderName):
	testReturnMessage = "{'Error': 'Not available right now.'}"
	print downloaderName, ": ", request.args.get('lastReceiveMessageDate')
	return testReturnMessage