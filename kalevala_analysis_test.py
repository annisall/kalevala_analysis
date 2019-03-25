import unittest
import kalevala_analysis as kaleva
from collections import Counter

class kalevalaTest(unittest.TestCase):
    def test_clean_line_removes_ending_space(self):
        self.assertEqual(kaleva.clean_line('foobar '), 'foobar')

    def test_clean_line_removes_starting_space(self):
        self.assertEqual(kaleva.clean_line(' foobar'), 'foobar')

    def test_clean_line_removes_both_spaces(self):
        self.assertEqual(kaleva.clean_line(' foobar '), 'foobar')

    def test_clean_line_removes_newlines(self):
        self.assertEqual(kaleva.clean_line('foobar\n\n'), 'foobar')

    def test_clean_line_lowercase(self):
        self.assertEqual(kaleva.clean_line('FooBar'), 'foobar')

    def test_remove_punctuations_basic(self):
        self.assertEqual(kaleva.remove_punctuations(['my name is Bond, James Bond!']), ['my name is Bond James Bond'])

    def test_remove_punctuations_escaped(self):
        self.assertEqual(kaleva.remove_punctuations(['my name is O\'Malley, Thomas O\'Malley!']), ['my name is OMalley Thomas OMalley'])

    def test_combine_and_tokenize_two_sentences(self):
        self.assertEqual(kaleva.combine_and_tokenize(['This is number one', 'This is number two', 'This is number three']), 
            ['This', 'is', 'number', 'one', 'This', 'is', 'number', 'two','This', 'is', 'number', 'three'])

    def test_count_metrics(self):
        self.assertEqual(kaleva.calculate_metrics([('first poem', ['This is the end', 'hold your breath', 'and count to ten']), 
            ('second poem', ['This is the way the world ends', 'This is the way the world ends', 'This is the way the world ends', 'Not with a bang but a whimper'])]),
             [('first poem', 3, 11), ('second poem', 4, 28)])

    def test_word_frequency_two_sentences(self):
        self.assertEqual(kaleva.word_frequency([('first poem', ['this', 'is', 'the', 'way', 'the', 'world', 'ends']), 
            ('second poem', ['not', 'with', 'a', 'bang', 'but', 'a', 'whimper'])]),
             [('first poem', Counter({'the': 2,'this':1, 'is': 1, 'way': 1, 'world':1, 'ends': 1})),
              ('second poem', Counter({'a': 2, 'not': 1, 'with': 1, 'bang': 1, 'but': 1, 'whimper': 1}))])




if __name__ == '__main__':
    unittest.main()
