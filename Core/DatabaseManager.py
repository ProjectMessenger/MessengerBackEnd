import pymysql
from Utils import JsonDataConverter

def GetCrawledDataList():
	databaseConnection = pymysql.connect(host='stories3.iptime.org', user='KoreanArmy', 
										 password='toortoor%^%', db='KoreanArmy', charset='utf8')
	dataCursor = databaseConnection.cursor(pymysql.cursors.DictCursor)
	sqlQuery = "select * from NoticeData;"
	dataCursor.execute(sqlQuery)
	
	dataRows = dataCursor.fetchall()
	
	noticeDataList = []
	
	for indexOfDataRow in dataRows:
		eachNoticeData = [indexOfDataRow['noticeId'], indexOfDataRow['title'], indexOfDataRow['url'], indexOfDataRow['writer'], str(indexOfDataRow['uploadDate'])]
		noticeDataList.append(eachNoticeData)
	
	jsonConvertedNoticeString = JsonDataConverter.GetNoticeDataList(noticeDataList)
	print jsonConvertedNoticeString
	return jsonConvertedNoticeString