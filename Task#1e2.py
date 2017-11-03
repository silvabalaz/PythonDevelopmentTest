from collections import OrderedDict
from itertools import zip_longest

#all necesary methods

def grouper(n, iterable, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx
    args = [iter(iterable)] * n
    print("+++",*zip_longest(fillvalue=fillvalue, *args))
    return zip_longest(fillvalue=fillvalue, *args)

def makeDict(dataList):
	"""Create dictionary from list of data """
	dictionary = {}
	
	for i in range(0,len(dataList)):
		name, idNum = dataList[i].split(' ')
		dictionary[idNum] = name

	return dictionary

def resultDict(dict1, dict2):
	"""Create new dictionary {id:name surname} with name and surname 
	that have equal id's in previous two """

	dictionary = {}
	# big O, O(n) coplexity, where n is the number of elements in dict1
	for key,value in dict1.items():
		if key in dict2.keys():
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

def printToFile(d,file_new):
	"""Print key and values from last 
	dictionary (sorted) to new file"""
	for key,value in d.items():
		line = value + ' ' + key + '\n'
		file_new.write(line)
		line = ''

def joinFiles(listOfFiles):
	'''Join data from multiple files of strings:
	   -name surname id- into new file'''
	try:
		complete = open('completeFile.txt', 'w')
	except IOError:
		print("Could not write to file:", 'completeFile.txt')
		sys.exit()
	else:
		dictionary = {}
		a = []
		for l in listOfFiles:
			#open
			currentFile = open(l,'r')
			#read
			currentString = currentFile.read()
			a = currentString.split(' ')
			name = a[0]
			surname = a[1]
			idNum = a[2].rstrip()
			dictionary[idNum] = name +' '+ surname
			sort = sortingDict(dictionary)
			printToFile(sort,complete)
			#close
			currentFile.close()
	complete.close()

if __name__ == "__main__":

	#chunk big files into small ones
	n = 1 #number of elements in each small file
	l1, l2 = [], []
	with open('file1.txt') as f:
	    for i, g in enumerate(grouper(n, f, fillvalue=None), 1):
	        with open('file_new_first{0}'.format(i * n), 'w') as fout:
	            fout.writelines(g)
	            l1.append('file_new_first{0}'.format(i * n))

	with open('file2.txt') as f:
	    for i, g in enumerate(grouper(n, f, fillvalue=None), 1):
	        with open('file_new_second{0}'.format(i * n), 'w') as fout:
	            fout.writelines(g)
	            l2.append('file_new_second{0}'.format(i * n))

	i = 0
	newList = []
	#open file
	for fileFirst in l1:
		for fileSecond in l2:
	
			pathFirst = fileFirst
			pathSecond = fileSecond

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
				list_first.pop()
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
				list_second.pop()
				dictSecond = makeDict(list_second)
				file_second.close()

			#pass through both list of strings simultaniously and check if each element of first list
			#has the same id number as the second list
			#better way is to store each element of list in dictionary so we could easily compare values (id-s)
	
			dictResult = resultDict(dictFirst, dictSecond)
			sortedDictResult = sortingDict(dictResult)
			
			if bool(sortedDictResult) != False:
				#write to new file
				i += 1
				new_path = 'fileNew{0}.txt'.format(i)
				newList.append(new_path)

				try:
					file_new = open(new_path, 'w')
				except IOError:
					print("Could not write to file:", new_path)
					sys.exit()
				else: 	
					printToFile(sortedDictResult,file_new)
					file_new.close()
		
	joinFiles(newList)