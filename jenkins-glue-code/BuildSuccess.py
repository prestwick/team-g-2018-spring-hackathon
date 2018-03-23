import requests
import json
import os
import datetime

timestamp = datetime.datetime.utcnow().isoformat()
file_path = "C:/ProgramData/Hackathon/resultId.txt"
idFile = open(file_path, 'r')
id = idFile.read()

jsonData = { 
	"result": {
		"fileIds":[], 
		"id": id,
		"keywords": [ "2018springhackathon" ], 
		"programName":"InsightCM Build", 
		"properties": {
			"currentStatus": os.environ['JOB_BASE_NAME']
		},		
		"status": { "statusType":"PASSED", "statusName":"Passed" }, 
		"systemId":"icmr6build", 
		"updatedAt": timestamp
	},
	"replace":True
}

r = requests.put('http://hack-g.amer.corp.natinst.com/nitestmonitor/v1/results/' + id, json = jsonData, auth=("admin", "hack-g"))