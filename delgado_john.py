import sys
from functions import format_input as fi
from functions import load_input as li
from functions import output_formatted_data as ofd

if __name__ == '__main__':
    # load input
    input_to_format = li.load_input()
    # format input
    formatted_data = fi.format_input(input_to_format)
    # output the data
    ofd.output_data(formatted_data)
