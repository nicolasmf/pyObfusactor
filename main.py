from ast import Return
import re

def findFunctionNames(file):
	function_names = []
	for _, line in enumerate(open(file)):
		for name in re.findall(r"(?<=def ).+(?=\()", line):
			function_names.append(name)
	return function_names

if __name__ == "__main__":
	print(findFunctionNames("test.py"))