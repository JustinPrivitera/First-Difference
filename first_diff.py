#!/usr/bin/python3
import sys

default_context = "0" # specifies how many lines prior you wish to view
# -1 prints the entire file before the difference, 0 prints nothing, and all other numbers print as many lines
default_lines = "-n" # -n means no lines, -l means print line numbers, -s means only print line number of difference

def first_diff(infile1, infile2, context = default_context, lines = default_lines):
	file1 = open(infile1, "r")
	file2 = open(infile2, "r")

	fileText1 = string_token(file1.read(), "\n")
	fileText2 = string_token(file2.read(), "\n")

	found = False
	i = 0
	while i < len(fileText1) and i < len(fileText2):
		if fileText1[i] != fileText2[i]:
			print_diff(infile1, infile2, fileText1,fileText2, i, int(context), lines)
			found = True
			break
		i += 1

	if not found:
		print_diff(infile1, infile2, fileText1, fileText2, -i, int(context), lines)

	file1.close()
	file2.close()

def print_diff(infile1, infile2, fileText1, fileText2, line, context, lines):
	if line < 0:
		line *= -1
		if len(fileText1) > len(fileText2):
			print_context(fileText1, line, context, lines)
			if lines == "-l" or lines == "-s":
				print(infile1 + ":" + str(line) + " > " + fileText1[line] + "\n" + infile2 + ":exceeded length")
			else:
				print(infile1 + ": " + fileText1[line] + "\n" + infile2 + ":exceeded length")
		elif len(fileText1) < len(fileText2):
			print_context(fileText1, line, context, lines)
			if lines == "-l" or lines == "-s":
				print(infile1 + ":exceeded length\n" + infile2 + ":" + str(line) + " > " + fileText2[line])
			else:
				print(infile1 + ":exceeded length\n" + infile2 + ": " + fileText2[line])
	else:
		print_context(fileText1, line, context, lines)
		if lines == "-l" or lines == "-s":
			print(infile1 + ":" + str(line) + " > " + fileText1[line])
			print(infile2 + ":" + str(line) + " > " + fileText2[line])
		else:
			print(infile1 + ": " + fileText1[line])
			print(infile2 + ": " + fileText2[line])
	
def print_context(fileText, line, context, lines):
	if context == -1:
		i = 0
	else:
		i = line - context
		if i < 0:
			i = 0
	while i < line:
		if lines == "-l":
			print(str(i) + " > " + fileText[i])
		else:
			print(fileText[i])
		i += 1

def string_token(line, spliterator, mode = 's'): # mode 's' = standard, mode 'f' = full
	splitTokens = list(spliterator)
	wordList = []

	j = 0
	for i in range(0, len(line)):
		if line[i] in splitTokens:
			wordList.append(line[j : i]) # adds words to the list
			j = i + 1
			if mode == 'f':
				wordList.append(line[i])
		if i == len(line) - 1:
			wordList.append(line[j : i + 1]) # adds the final word to the list
	
	i = 0
	length = len(wordList)
	# while i < length:
	# 	if '' == wordList[i]:
	# 		del wordList[i] # removes null strings from the list
	# 		i -= 1
	# 		length -= 1
	# 	i += 1

	return wordList

if len(sys.argv) == 3:
	first_diff(sys.argv[1], sys.argv[2])
elif len(sys.argv) == 4:
	first_diff(sys.argv[1], sys.argv[2], sys.argv[3])
elif len(sys.argv) == 5:
	first_diff(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
else:
	print("usage: ./first_diff.py <file1> <file2> <[context]> <[lines]>")
