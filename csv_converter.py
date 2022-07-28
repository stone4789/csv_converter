#! /usr/bin/env python3

"""
    A helper script for when data is mostly stored in exported excel files.
    Move to the directory/drive where data has been saved in XLSX or CSV files. Convert all XLSX into CSV and delete the old files afterwards.
"""


def main():
    import glob
    import openpyxl
    import os
    import pandas as pd
    import warnings
    warnings.filterwarnings("ignore")

    folder_path = # put string directory path for where the data's stored here
    os.chdir(folder_path)

    path = os.cwd()
    excel_files = glob.glob(os.path.join(path, "*.xlsx")) 

    for excel in excel_files:
        if "$" not in excel:
            out = excel.split(".")[0] + ".csv"
            df = pd.read_excel(excel, engine="openpyxl")
            df.to_csv(out)
    
    if os.getcwd() == folder_path:
        for excel in excel_files:
            os.remove(excel)
        else:
            return "The file does not exist"

if "__name__" == "__main__":
    main()
