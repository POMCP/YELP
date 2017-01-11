'''This files loads data from the json files and stores them in dataframes. Additional funtion is to store the
dataframes to pickle files for further usage.'''
from Data_convert_json_csv import *


'''This function loads the data from the provided json file and the mentioned columns'''


def load_data(jsonfile_path, columns):
    """Convert a yelp dataset file from json to csv."""
    json_file = jsonfile_path
    csv_file = '{0}.csv'.format(json_file.split('.json')[0])
    read_and_write_file(json_file, csv_file, columns)