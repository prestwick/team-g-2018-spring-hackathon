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
		"status": { "statusType":"FAILED", "statusName":"Failed" }, 
		"systemId":"2349F6E4-B0D9-4527-8638-FA8BFA0F5B41", 
		"updatedAt": timestamp
	},
	"replace":True
}

r = requests.put('http://hack-g.amer.corp.natinst.com/nitestmonitor/v1/results/' + id, json = jsonData, auth=("admin", "hack-g"))