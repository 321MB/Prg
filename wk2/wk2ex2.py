from re import M


def dbl(x):
    """Returns twice the argument

    Spam is great, and dbl("spam") is better!

    :param x: The value to double
    :type x: int, float or string
    :rtype: int, float or string
    """
    return 2 * x


def tpl(x):
    """Returns thrice the argument

    :param x: The value to triple
    :type x: int, float or string
    :rtype: int, float or string
    """
    return 3 * x


def sq(x):
    """Returns the square of the argument

    :param x: The value to square
    :type x: int or float
    :rtype: int orfloat
    """
    return x * x


def interp(low, hi, fraction):
    """
    fraction of where between low and hi you are
    """

    return (hi - low) * fraction + low


def checkends(s):
    """
    sets s in a list and checks first and last in hte list if they match
    """

    lst = []

    for letter in s:
        lst.append(letter)

    print(lst)

    if lst[0:1] == lst[-1:]:
        return True
    if lst[0:1] != lst[-1:]:
        return False


def flipside(s):
    """flips 2 halfs of s

    Keyword arguments:
    s:  string to be flipes
    Return: s front half behind back half
    """
    x = len(s) // 2
    lst = []
    for letter in s:
        lst.append(letter)
    flip = lst[x:] + lst[:x]
    flipped = "".join(flip)
    return flipped


def convert_from_seconds(s):
    """calculates the days hours minutes and seconds from amount of seconds s"""
    days = s // (24 * 60 * 60)  # Het aantal dagen
    s = s % (24 * 60 * 60)  # Het restant
    hours = s // (60 * 60)
    s = s % (60 * 60)
    minutes = s // 60
    s = s % 60
    seconds = s
    return [days, hours, minutes, seconds]
