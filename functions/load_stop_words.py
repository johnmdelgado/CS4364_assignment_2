'''
FileName: load_stop_words.py
Author: John Delgado
Created Date: 10/28/2021
Version: 1.0 Initial Development
'''

from pathlib import Path


def load_stop_words(stop_words_file_path):
    # import stop words from the file
    print("Loading stop words")
    stop_word_file = Path(__file__).parent / stop_words_file_path
    print("Loading from: {}".format(stop_word_file))
    try:
        # open the file read in the stop words
        stop_words_file = open(stop_words_file_path, "r")
        # now do a split to convert it into a list
        stop_words = (stop_words_file.read()).split()
        # now that we have a list, we'll convert it to a set to remove duplicate values
        # this should increase performance when there are large amounts of data to compare
        # or there are many duplicates added to this list
        stop_words = set(stop_words)
        # close our open file
        stop_words_file.close()
        # return the set
        return stop_words
    except FileNotFoundError as fnf:
        print("Stop words file does not exist at {}. \n {}".format(
            stop_word_file, fnf))
