from collections import OrderedDict
import sys

#all necesary methods

def makeDict(dataList):
	"""Create dictionary from list of data """
	dictionary = {}
	
	for i in range(0,len(dataList)):
		name, idNum = dataList[i].split(' ')
		dictionary[idNum] = name

	return dictionary

def resultDict(dict1, dict2):
	"""Create new dictionary with name and surname 
	that have equal id's as in previous two """
	dictionary = {}

	# big O, O(n) coplexity, where n is the number of elements in dict1
	for key,value in dict1.items():
		if dict2[key]:
			nameSurname = value + ' ' + dict2[key]
			dictionary[key] = nameSurname
			nameSurname = '' 

	return dictionary

def sortingDict(d):
	"""Sort dictionary using sorted list, by id"""

	dictionary = OrderedDict()
	sortedList = sorted(d)

	for i in range(0,len(sortedList)):
		dictionary[sortedList[i]] = d[sortedList[i]]

	return dictionary

def printToFile(d, new):
	"""Print key and values from last 
	dictionary (sorted) to new file"""

	for key,value in d.items():
		line = value + ' ' + key + '\n'
		new.write(line)
		line = ''


if __name__ == "__main__":

	#store name of file
	pathFirst = 'file1.txt'
	pathSecond = 'file2.txt'

	#open, read, close both files

	try:
		file_first = open(pathFirst, 'r')
	except IOError:
		print("Could not read file:", pathFirst)
		sys.exit()
	else: 
		#read, split string, close file
		string_first = file_first.read()
		list_first = string_first.split('\n')
		dictFirst = makeDict(list_first)
		file_first.close()

	try:
		file_second = open(pathSecond, 'r')
	except IOError:
		print("Could not read file:", pathSecond)
		sys.exit()
	else:
		string_second = file_second.read()
		list_second = string_second.split('\n')
		file_second.close()

	#pass through both list of strings simultaniously and check if each element of first list
	#has the same id number as the second list
	#better way is to store each element of list in dictionary so we could easily compare values (id-s)

	dictFirst = makeDict(list_first)
	dictSecond = makeDict(list_second)
	dictResult = resultDict(dictFirst, dictSecond)
	sortedDictResult = sortingDict(dictResult)

	#store name of new file
	new_path = 'fileNew.txt'

	# write to new file
	try:
		file_new = open(new_path, 'w')
	except IOError:
		print("Could not write to file:", new_path)
		sys.exit()
	else:
		printToFile(sortedDictResult, file_new)
		file_new.close()



