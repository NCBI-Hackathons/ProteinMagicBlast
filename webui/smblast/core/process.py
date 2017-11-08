import json
import os
import subprocess
import sys

class Process(object):
	def __init__(self, id):
		super(Process, self).__init__()
		self.id = id

	def __workingDir(self):
		return 'temp/' + self.id		

	def __resultFilePath(self):
		return self.__workingDir() + '/result.json'		

	def __statusFilePath(self):
		return self.__workingDir() + '/status.json'		

	def __scriptFilePath(self):
		return 'magic/magic.py'		

	def __logFilePath(self):
		return self.__workingDir() + '/log.txt'		

	def Run(self, srr, protein):
		os.makedirs(self.__workingDir())

		log = open(self.__logFilePath(), 'a')

		subprocess.Popen([
				sys.executable, 
				self.__scriptFilePath(),
				srr,
				protein,
				self.__resultFilePath(),
				self.__statusFilePath(),
			],
			stdout=log, 
			stderr=log);

	def GetProgress(self):
		try:
			with open(self.__statusFilePath()) as dataFile:    
				progress = json.load(dataFile)

				return progress
		except FileNotFoundError:
			progress = { 
				'progress': 0, 
				'status': "Initializing...",
				'finished': False 
			}
			return progress

	def GetResult(self):
		pass

	def GetLog(self):
		with open(self.__logFilePath()) as logFile:    
			return logFile.read()

	def GetResult(self):
		with open(self.__resultFilePath()) as resultFile:    
			return resultFile.read()
