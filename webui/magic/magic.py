import json
import os
from shutil import copyfile
import sys
import time

outputFilePath = sys.argv[3]
statusFilePath = sys.argv[4]

def writeStatus(status):
	with open(statusFilePath, 'w') as outfile:
		json.dump(status, outfile)

try:
	sleepTime = 1

	writeStatus({ 'progress': 0, 'status': 'Doing things...', 'finished': False })
	time.sleep(sleepTime)

	writeStatus({ 'progress': 10, 'status': 'Starting...', 'finished': False })
	time.sleep(sleepTime)

	writeStatus({ 'progress': 15, 'status': 'Starting...', 'finished': False })
	time.sleep(sleepTime)

	writeStatus({ 'progress': 20, 'status': 'Doing things...', 'finished': False })
	time.sleep(sleepTime)

	writeStatus({ 'progress': 25, 'status': 'Doing things...', 'finished': False })
	time.sleep(sleepTime)

	writeStatus({ 'progress': 35, 'status': 'Doing things...', 'finished': False })
	time.sleep(sleepTime)

	writeStatus({ 'progress': 40, 'status': 'Doing things...', 'finished': False })
	time.sleep(sleepTime)

	writeStatus({ 'progress': 45, 'status': 'Doing things...', 'finished': False })
	time.sleep(sleepTime)

	writeStatus({ 'progress': 55, 'status': 'Doing things...', 'finished': False })
	time.sleep(sleepTime)

	writeStatus({ 'progress': 65, 'status': 'Almost done...', 'finished': False })
	time.sleep(sleepTime)

	writeStatus({ 'progress': 80, 'status': 'Almost done...', 'finished': False })
	time.sleep(sleepTime)

	writeStatus({ 'progress': 100, 'status': 'Almost done...', 'finished': False })
	time.sleep(sleepTime)

	writeStatus({ 'progress': 100, 'status': 'Almost done...', 'finished': True })

	scriptPath = os.path.dirname(os.path.realpath(__file__))
	sampleOutputPath = scriptPath + "/blastx.json.example"
	copyfile(sampleOutputPath, outputFilePath)

except Exception as e:
	writeStatus({ 'progress': 100, 'status': 'Error', 'finished': True, 'error': True })
	raise e
