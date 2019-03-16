from os import listdir
from os.path import isfile, join
import string
from functools import reduce

transtbl=str.maketrans('', '', string.punctuation)

def clean_line(line):
	return line.rstrip('\n').strip()

def remove_punctuations(line):
	return line[1].translate(transtbl)

def is_empty(line):
	return line

def get_poem(file_path):
	with open(file_path) as poemfile:
		return list(filter(is_empty, map(clean_line, poemfile.readlines())))

def clean_poems(poems):
	return list(map(lambda line: clean_line(line), poems))

def word_count(lines):
	
	#return list(reduce(lambda x, y: x+y, (map(foo, lines))))
	return list(map(lambda line: len(line.split()), lines))

def count_metrics(poems):
	return list(map(lambda poem: (poem[0],len(poem[1]), sum(word_count(poem[1]))), poems))



def read_files(directory_path):
	file_names=[file for file in listdir(directory_path) if isfile(join(directory_path, file)) and '.txt' in file]
	#poems=[get_poem(join(directory_path, name)) for name in file_names]
	poems=list(map(lambda name: (name, get_poem(join(directory_path, name))), file_names))
	return poems

poems_list=read_files('data')
metrics=count_metrics(poems_list)
for thing in metrics:
	print('Name: {0}, line count: {1}, word count: {2}'.format(thing[0], thing[1], thing[2]))
#print(list(map(lambda poem: (poem[0], sum(word_count(poem[1]))), poems_list)))

