'''
    File name: InputHandler.py
    Author: Joao Costa
    Date created: 06/12/2019
    Date last modified: 06/12/2019
    Python Version: 3.7
'''
import argparse
import os
import json
global data_from_file


def is_valid_file(parser:  argparse.ArgumentParser, filepath):
    global data_from_file

    if(not fileExist(filepath)):
        return is_valid_file(parser, askForNewFile())


    data_from_file = getDataFromFile(filepath)
    if(len(data_from_file) <= 0):
        return is_valid_file(parser, askForNewFile())

    return data_from_file

def askForNewFile() -> str:
    """
    prompts the user to enter a path to the valid file
    :return: path to a file
    """
    return input("Insert path to file to parse: ")

def fileExist(file_path: str) -> bool:
    """
    check if the file entered by the user exists
    :param file_path:
    :return bool:
    """
    if not os.path.exists(file_path):
        print("The file %s does not exist!" % file_path)
        return False

    return True

def getDataFromFile(filepath: str) -> list:
    """
    Get data from the file entered by the user and validates if the file contain the correct format
    :param file_path:
    :return list:
    """
    data = []
    have_content = False
    with open(filepath) as fp:
        line = fp.readline()
        while line:
            have_content = True
            try:
                data.append(json.loads(line.strip()))
                line = fp.readline()

            except json.decoder.JSONDecodeError as execption:
                print("The file %s contains files that are not in the correct JSON format" % filepath)
                data = []
                break

    if(not have_content):
        print("The file %s do not have content" % filepath)

    return data


def parseInput(argv):
    """
    parse the input inserted by the user
    :param argv:
    :return:
    """

    #parse --input_file
    parser = argparse.ArgumentParser(description="Parses a stream of events and produces an aggregated output")
    parser.add_argument("-i", "--input_file", dest="data", required=True,
                        help="input file with data from translation",
                        type=lambda x: is_valid_file(parser, x))
    # parse --window_size
    parser.add_argument("-w", "--window_size", dest="window_size", required=True,
                        help="window size to calculate average translation duration", type=int)

    return parser.parse_args(argv[1:])



