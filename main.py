from keyword import iskeyword
import random
import re
import string

def findFunctionNames(file):
	function_names = []
	for _, line in enumerate(open(file)):
		for name in re.findall(r"(?<=def )\w+(?=\()", line):
			function_names.append(name)
	return function_names

def findVariableNames(file):
	variable_names = []
	for _, line in enumerate(open(file)):
		regex = r"((\w+)(?=( ||\t)=( |)))|((?<=\()\w+(?=\)))|((?<=\()\w+(?=,))|((?<=, )\w+(?=,))|((?<=, )\w+(?=\)))|(\w+(?=, ))"
		for name in re.findall(regex, line):
			variable_names.append(list(filter((lambda x: x!='' and x!=' '), name))[0])
	return list(set(variable_names))

def createRandomString():
	letter = string.ascii_letters
	result_str = ''
	for i in range(random.randint(30,50)):
		result_str += random.choice(letter)
	return result_str

def createMap(names_list):
	name_map = { i : createRandomString() for i in names_list }
	return name_map

def obfuscate(name_map, code_file):

	with open(code_file, 'r') as file :
		filedata = file.read()

	filedata = deleteComments(filedata)
	filedata = replaceFromMap(name_map, filedata)
	filedata = deleteEmptyLines(filedata)

	with open('obfuscated.py', 'w') as file:
		file.write(filedata)

def deleteComments(filedata):

	filedata = re.sub('#.*', '', filedata)
	filedata = re.sub('\"\"\"[\s\S]*?\"\"\"', '', filedata)
	return filedata 

def replaceFromMap(name_map, filedata):

	for key, value in name_map.items():
		filedata = filedata.replace(key, value)

	return filedata

def deleteEmptyLines(filedata):

	lines = filedata.split("\n")

	non_empty_lines = [line for line in lines if line.strip() != ""]

	no_empty_lines = ""

	for line in non_empty_lines:
		no_empty_lines += line + "\n"

	return no_empty_lines


if __name__ == "__main__":
	print("Variables : " + str(findVariableNames("test.py")))
	print("Functions : " + str(findFunctionNames("test.py")))
	print(createRandomString())
	print(createMap(findVariableNames("test.py") + findFunctionNames("test.py")))
	name_map = createMap(findVariableNames("test.py") + findFunctionNames("test.py"))
	obfuscate(name_map, "test.py")