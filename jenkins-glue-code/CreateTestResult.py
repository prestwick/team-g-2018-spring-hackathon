import requests
import json
import os

r = requests.post('http://hack-g.amer.corp.natinst.com/nitestmonitor/v1/results', json = {"results":[{ "fileIds":[], "keywords": [ "2018springhackathon" ], "programName":"InsightCM Build", "startTime": "2018-3-23T:11:04:05.111Z", "status": {"statusType":"RUNNING", "statusName":"Running"}, "systemId":"2349F6E4-B0D9-4527-8638-FA8BFA0F5B41", "updatedAt":"2018-3-23T:11:04:05.111Z"}]}, auth=("admin", "hack-g"))

if r.status_code == 201:
	file_path = "C:/ProgramData/Hackathon/resultId.txt"
	directory = os.path.dirname(file_path)
	try:
		idFile = open(file_path, 'w')
	except IOError:
		if not os.path.exists(directory):
			os.makedirs(directory)
		idFile = open(file_path, 'w')
	
	idFile.write(r.json()['results'][0]['id'])
	idFile.close()
