from datetime import datetime
import pandas as pd

def calculate_ctr(col1, col2) -> float:

    """
    Function to calaculate CTR

    Parameters
    ----------
    col1: float
    col2: float

    Returns
    -------
    float

    """
    return ((col1) / (col2) * 100)

def calculate_cpi(col1, col2) -> float:

    """
    Function to calaculate CPI

    Parameters
    ----------
    col1: float
    col2: float

    Returns
    -------
    float

    """
    return ((col1) / (col2))
    

def iso_date(date) -> datetime:

    """
    Function that convert str to datetime and specific format.

    Parameters
    ----------
    date: str

    Returns
    -------
    i: datetime (iso format)

    """

    date = datetime.strptime(date, '%Y.%m.%d')
    iso_date = datetime.isoformat(date)
    
    return datetime.fromisoformat(iso_date)


def convert_to_int(column) -> int:

    """
    Function that convert a value to int

    Parameters
    ----------
    column: str/float

    Returns
    -------
    int

    """

    return column.astype('int')

def read_csv(file_name) -> pd.DataFrame:

    """
    Function to read csv

    Parameters
    ----------
    column: str

    Returns
    -------
    DataFrame

    """
    df = pd.read_csv(file_name)

    return df
