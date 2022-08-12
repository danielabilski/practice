import logging
logging.basicConfig(level=logging.NOTSET)

def thousands_with_commas(i: int) -> str:

    """
    Function that takes an integer and
    returns a string with the number with commas every 3 digits.

    Parameters
    ----------
    i: int

    Returns
    -------
    i: str

    """

    i = "{:,}".format(i)
    logging.info(i)
    
    return i


if __name__ == '__main__':

    assert thousands_with_commas(1234) == '1,234'
    assert thousands_with_commas(123456789) == '123,456,789'
    assert thousands_with_commas(12) == '12'
