from datetime import datetime


def percentage(col1, col2) -> float:

    """
    Function to calaculate specific rate between 2 values

    Parameters
    ----------
    col1: float
    col2: float

    Returns
    -------
    float

    """
    return ((col1) / (col2) * 100)
    

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
    
    return date.isoformat()


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
