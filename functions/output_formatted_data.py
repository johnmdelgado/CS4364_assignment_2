'''
FileName: format_input.py
Author: John Delgado
Created Date: 10/28/2021
Version: 1.0 Initial Development
'''
from functions import load_config as lc
import sys
import os
from pathlib import Path
from datetime import datetime
config = lc.load_config()


def output_data(data_to_output):

    if config["output_settings"]["output_to_terminal"]:
        dict_to_formatted_table(data_to_output)
    if config["output_settings"]["output_to_file"]:
        output_to_file(data_to_output)


def dict_to_formatted_table(data_to_output):
    headers = get_headers(data_to_output[0])
    output_headers = "| {:<20} | {:<20} |".format(headers[0], headers[1])
    print(output_headers)
    print("| {:<20} | {:<20} |".format(
        generate_divider(20), generate_divider(20)))
    for row in data_to_output:
        if not None:
            print("| {:<20} | {:<20} |".format(
                row["Original Word"], row["Token Type"]))


def get_headers(dict_to_get_headers_from):
    headers = []
    for key in dict_to_get_headers_from.keys():
        headers.append(key)
    return headers


def generate_divider(column_width):
    divider = ""
    for i in range(column_width):
        divider += "-"
    return divider


def output_to_file(data_to_output):
    now = (datetime.now().strftime("%d%m%YT%H%M%S"))
    filename = "Output_Data_{}.txt".format(now)
    filepath = config["output_settings"]["output_dir"] + filename

    output_file = str(Path(__file__).resolve().parents[1]) + filepath
    # test if path exists
    if not os.path.exists(output_file):
        os.makedirs(str(Path(__file__).resolve(
        ).parents[1]) + config["output_settings"]["output_dir"])
    try:
        # open the file read
        sys.stdout = open(output_file, "w")
        dict_to_formatted_table(data_to_output)
        # close our open file
        sys.stdout.close()
        # return the set
    except FileNotFoundError as fnf:
        print("Stop words file does not exist at {}. \n {}".format(
            filepath, fnf))
