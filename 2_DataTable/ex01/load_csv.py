import os
import pandas as pd


def load(path: str) -> pd.DataFrame:
    '''
    [LOAD] checks the format (CSV) and path of a specified file,
    then loads the data set and returns it as a tabular format.
    '''
    try:
        if path[-4:] != ".csv":
            raise AssertionError("File format not supported.")
        if not os.path.exists(path):
            raise AssertionError(f"{path}: no such file.")

        data = pd.read_csv(path)
        print(f"Loading dataset of dimensions {data.shape}")
        return data

    except AssertionError as e:
        print(f"AssertionError: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
