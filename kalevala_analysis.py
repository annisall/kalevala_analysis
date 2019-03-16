from os import listdir
from os.path import isfile, join
import string
from functools import reduce
from collections import Counter
import pprint

transtbl=str.maketrans('', '', string.punctuation)

def clean_line(line):
	return line.rstrip('\n').strip()

def remove_punctuations(lines):
	return list(map(lambda line: line.translate(transtbl), lines))

def is_empty(line):
	return line

def get_poem(file_path):
	with open(file_path) as poemfile:
		return list(filter(is_empty, map(clean_line, poemfile.readlines())))

def word_count(poem):
	return list(map(lambda line: len(line.split()), poem))

def count_metrics(poems):
	return list(map(lambda poem: (poem[0],len(poem[1]), sum(word_count(poem[1]))), poems))

def read_files(directory_path):
	file_names=[file for file in listdir(directory_path) if isfile(join(directory_path, file)) and '.txt' in file]
	poems=list(map(lambda name: (name, get_poem(join(directory_path, name))), file_names))
	return poems

def flatten_poems(poems):
	return list(map(lambda poem: (poem[0], ' '.join(poem[1]).split()), poems))

def word_frequency(poems):
	return list(map(lambda poem: (poem[0], Counter(poem[1])), poems))

def print_poems(poems):
	for poem in poems:
		print('Name: {0}, poem: {1}'.format(poem[0], poem[1]))

def pretty_print_frequencies(poem):
	print('Name of the poem: {0}'.format(poem[0]))
	pprint.pprint(poem[1])



poems_list=read_files('data')
metrics=count_metrics(poems_list)
cleaned_poems=list(map(lambda poem: (poem[0], remove_punctuations(poem[1])), poems_list))

flattened=flatten_poems(cleaned_poems)

freqs=(word_frequency(flattened))


