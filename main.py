from keyword import iskeyword
import re

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

if __name__ == "__main__":
	print("Variables : " + str(findVariableNames("test.py")))
	print("Functions : " + str(findFunctionNames("test.py")))