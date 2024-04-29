# Python script dedicated to i/o operations

import pandas as pd

def read_csv(file_path0):
    """Creating Sale dataframes from csv file > file_path0 """
    try:
        return pd.read_csv(file_path0)
    except IOError as e:
        print('IO error: ' + e)


def generate_html_report(html_filename0, html_block0):
    """Function generate and save a single HTML page"""
    file = open(html_filename0, "w") 
    file.write(html_block0)
    file.close()