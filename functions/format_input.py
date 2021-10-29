'''
FileName: format_input.py
Author: John Delgado
Created Date: 10/28/2021
Version: 1.0 Initial Development
'''
from functions import load_config as lc
from functions import load_stop_words as lsw
from functions import porter_stemmer as ps
import re


def format_input(input_to_process):
    print("Formatting Input...")
    cleaned_input = clean_input(input_to_process)
    tokenized_input = tokenize_input(cleaned_input)
    evaluated_tokens = evaluate_tokens(tokenized_input)
    return evaluated_tokens


def get_stop_words():
    # load the config containing our filepaths and default values
    config = lc.load_config()
    # load stop words
    stop_words = lsw.load_stop_words(
        config["filepaths"]["stop_word_filepath"])
    return stop_words


def tokenize_input(input_to_tokenize):
    # first let's split the strings by whitespace to tokenize them
    list_of_words = input_to_tokenize.split()
    return list_of_words


def clean_input(input_to_clean):
    # The first thing we are going to do is to remove all special characters
    # This regex will search for any special character and punctuation and remove them
    # This does not remove apostrophe's as they will be considered words in our case
    special_characters_regex = "[-()\"#/@;:<>{}`+=~|.!?,]"
    first_cleaned_input = re.sub(
        special_characters_regex, "", input_to_clean)
    # Now that we've removed the special characters, Let's convert all our words to lowercase
    second_cleaned_input = first_cleaned_input.lower()
    # Return our cleaned input
    return second_cleaned_input


def evaluate_tokens(tokens_to_evaluate):
    # This is going to return a dictionary with the evaluation
    # 'article’ if the token is an article(i.e.,a,an,the),
    # ‘stopword’ if the token is a stop word,
    # otherwise, write the stemmed version of the token.
    words_that_are_articles = {"a", "an", "and", "the"}
    stop_words = get_stop_words()
    stemmer = ps.PorterStemmer()
    evaluated_tokens = []
    for token in tokens_to_evaluate:
        if token in stop_words:
            evaluation = "Stop Word"
        if token in words_that_are_articles:
            evaluation = "Article"
        else:
            evaluation = stemmer.stem(token, 0, len(token)-1)
        evaluated_token = {
            "Original Word": token,
            "Token Type": evaluation
        }
        evaluated_tokens.append(evaluated_token)
    return evaluated_tokens
