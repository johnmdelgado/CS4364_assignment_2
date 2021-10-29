'''
FileName: load_input.py
Author: John Delgado
Created Date: 10/28/2021
Version: 1.0 Initial Development
'''

import sys
from functions import load_config as lc


def load_input():
    print("Loading Input...")
    # check if input is being passed in. If not use the default file from the config
    if not sys.stdin.isatty():
        print("Input provided from command line. Reading...")
        input_to_process = (sys.stdin).read()
    else:
        # load the config containing our filepaths and default values
        config = lc.load_config()
        print("No file provided through command line using default file from: {}".format(
            config["filepaths"]["input_file_filepath"]))
        input_to_process_path = config["filepaths"]["input_file_filepath"]
        input_to_process = input_from_file(input_to_process_path)

    # Here we will check if the input that we are receiving is empty or Null.
    test_empty(input_to_process)

    # Return the input so that we can process it
    return input_to_process


def input_from_file(file_path):
    try:
        # open the file read
        input_file = open(file_path, "r")
        # read the input
        input_to_process = (input_file.read())
        # close our open file
        input_file.close()
        # return the input
        return input_to_process
    except FileNotFoundError as fnf:
        print("Input file does not exist at {}. \n {}".format(
            file_path, fnf))


def test_empty(input_to_test):
    # If empty terminate the program, because there is nothing to process
    if (input_to_test is None) or ((len(input_to_test.strip()) == 0)):
        print("Input is empty. Nothing to Process.")
        sys.exit()
