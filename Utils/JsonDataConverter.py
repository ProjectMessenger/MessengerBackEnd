import json
from Utils import Logger
from Setting import DefineManager

def ServerStatusMessage(processStatus):
	return json.dumps({'Status':processStatus})

def GetClientSendToServerMessage(jsonMessageData):
	Logger.PrintLogMessage("JsonDataConverter", "GetClientSendToServerMessage", "json data: " + jsonMessageData, DefineManager.LOG_LEVEL_DEBUG)
	clientUploadedData = json.load(jsonMessageData.read())
	return [clientUploadedData['to'], clientUploadedData['message']]

def GetClientReceiveFromServerMessage(listOfMessageData):
	return json.dumps(listOfMessageData)

def GetNoticeDataList(noticeDataList):
	return json.dumps(noticeDataList)