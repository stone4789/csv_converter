#! /usr/bin/env python3
"""
    A helper script for when data is mostly stored in exported excel files.
    Move to the directory/drive where data has been saved in XLSX or CSV files. Convert all XLSX into CSV and delete the old files afterwards.
"""


def main():
    import openpyxl
    import warnings

    warnings.filterwarnings("ignore")
    import glob
    import pandas as pd
    import os

    folder_path = # put string directory path for where the data's stored here
    os.chdir(folder_path)

    path = os.cwd()
    excel_files = glob.glob(os.path.join(path, "*.xlsx")) 


if "__name__" == "__main__":
    main()
