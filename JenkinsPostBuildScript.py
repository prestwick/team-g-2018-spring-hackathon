import os

file_path = "C:/ProgramData/Hackathon/testfile.txt"
directory = os.path.dirname(file_path)

try:
	hworld = open(file_path)
except IOError:
	if not os.path.exists(directory):
		os.makedirs(directory)
	hworld = open(file_path, 'w+')

hworld.write("Hello World")
hworld.close()
