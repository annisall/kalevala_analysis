from os import listdir
from os.path import isfile, join
import string
from collections import Counter
import pprint
from collections import defaultdict
import numpy as np

transtbl = str.maketrans('', '', string.punctuation)

""" Removes spaces at the beginning and end, removes newlines and makes everything lower case """
def clean_line(line):
    return line.rstrip('\n').strip().lower()

""" Removes punctuations from list of lines """
def remove_punctuations(lines):
    return list(map(lambda line: line.translate(transtbl), lines))

""" Checks if given object is empty """
def is_empty(line):
    return line

def get_poem(file_path):
    with open(file_path) as poemfile:
        return list(filter(is_empty, map(clean_line, poemfile.readlines())))

""" Joins list elements with space and then splits sentences into single words 
Input: list of sentences,
output: list of words in all sentences given as input """
def combine_and_tokenize(poem):
    return ' '.join(poem).split()

""" Returns tuple containing name of file (poem), number of (nonempty) rows in a poem 
and how many words there are in a poem.
Input: (name, list of lines in a poem)
output: (name, number of lines, number of words)"""
def calculate_metrics(poems):
    return list(map(lambda poem: (poem[0], len(poem[1]), len(combine_and_tokenize(poem[1]))), poems))

""" Find all files under specified folder and read them 
Input: path to directory containing data files (poems)
output: list of tuples (name, list of (nonempty) lines in poems)"""
def read_files(directory_path):
    file_names = (file for file in listdir(directory_path) if isfile(join(directory_path, file)) and '.txt' in file)
    poems = list(map(lambda name: (name, get_poem(join(directory_path, name))), file_names))
    return poems

def combine_and_tokenize_all_poems(poems):
    return list(map(lambda poem: (poem[0], combine_and_tokenize(poem[1])), poems))

""" Calculates word frequencies in all poems 
input: list of tuples (name, list of (nonempty) lines in poems) 
output: list of tuples (name, {word:count}) where word is word occurring in poem and count 
is the number it occurs """
def word_frequency(poems):
    return list(map(lambda poem: (poem[0], Counter(poem[1])), poems))

""" Filters words that occur only once """
def filter_rare_items(word_freqs):
    return {word: freq for word, freq in word_freqs.items() if freq > 1}

""" Iterates over a poem and appends indexes of recurrences into a list.
 param poem: list of words,freq words: {word: count}
 returns {word: [list of indexes]} """
def find_word_indeces(poem, freq_words):
    occurrences_list = defaultdict(list)
    for index, word in enumerate(poem):
        if(word in freq_words):
            occurrences_list[word].append(index)
    return occurrences_list

""" poems: tuple (name, list of words)
 frequent items: (name: {word:count}) """
def map_indeces_to_poems(poems, frequent_items):
    return map(lambda poem: (poem[0], find_word_indeces(poem[1], frequent_items[poem[0]])), poems)

"""calculate sum of distances for all words in a poem"""
def calculate_avg_distances(words):
    return {word: (np.sum(np.diff(freq))/(len(freq)-1)) for word, freq in words.items()}

"""dict {nimi: {word: list of indexes}}"""
def avg_dists_across_poems(poems):
    return {name: calculate_avg_distances(words) for name, words in poems.items()}

def print_poems(poems):
    for poem in poems:
        print('Name: {0}, poem: {1}'.format(poem[0], poem[1]))

def pretty_print_metrics(metrics):
    print('Metrics:')
    for poem in metrics:
        print('Name: {0}, number of lines: {1}, number of words: {2}'.format(poem[0], poem[1], poem[2]))

def map_with_function(function_name, iterable_object):
    return map(lambda poem: (poem[0], function_name(poem[1])), iterable_object)

if __name__ == '__main__':
    poems_list = read_files('data')
    metrics = calculate_metrics(poems_list)

    #pretty_print_metrics(metrics)

    cleaned_poems = list(map_with_function(remove_punctuations, poems_list))

    poem_lists = combine_and_tokenize_all_poems(cleaned_poems)

    freqs = word_frequency(poem_lists)
    #print('Word counts:')
    #pprint.pprint(freqs)

    frequent_items = dict(map_with_function(filter_rare_items, freqs))

    indeces=dict(map_indeces_to_poems(poem_lists, frequent_items))

    print('Average waiting times')
    pprint.pprint(avg_dists_across_poems(indeces))
