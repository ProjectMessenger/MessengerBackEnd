import pymysql
from Utils import JsonDataConverter

def GetCrawledDataList():
	databaseConnection = pymysql.connect(host='stories3.iptime.org', user='KoreanArmy', 
										 password='toortoor%^%', db='KoreanArmy', charset='utf8')
	dataCursor = databaseConnection.cursor(pymysql.cursors.DictCursor)
	sqlQuery = "select * from NoticeData limit 10;"
	dataCursor.execute(sqlQuery)
	
	dataRows = dataCursor.fetchall()
	
	noticeDataList = []
	count = 0
	
	for indexOfDataRow in dataRows:
		eachNoticeData = {"NoticeId" : indexOfDataRow['noticeId'], "Title" :  indexOfDataRow['title'], "Url" : indexOfDataRow['url'], "Writer" : indexOfDataRow['writer'], "UploadDate" : str(indexOfDataRow['uploadDate'])}
		noticeDataList.append(eachNoticeData)
		# noticeDataList[count] = eachNoticeData
		# count += 1
	
	jsonConvertedNoticeString = JsonDataConverter.GetNoticeDataList(noticeDataList)
	print jsonConvertedNoticeString
	return jsonConvertedNoticeString