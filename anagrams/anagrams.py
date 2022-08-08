def anagrams(word: str) -> str:

    """
    Function that uses the WORD.LST file to return
    anagrams of the word given.

    Parameters
    ----------
    i : str

    Returns
    -------
    i: str

    """

    words_list = [w.rstrip() for w in open('WORD.lst.txt')]

    anagrams = [alt for alt in words_list if sorted(word) == sorted(alt)]

    return anagrams

if __name__ == "__main__":
    print(anagrams("train"))
    print('--')
    print(anagrams('drive'))
    print('--')
    print(anagrams('python'))