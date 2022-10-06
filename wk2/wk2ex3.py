from tkinter import N
from tkinter.messagebox import RETRY


def leng(s):
    """leng returns the length of s
    Argument: s, which can be a string or list
    """
    if s == "" or s == []:  # als lege string of lege lijst
        return 0
    else:
        return 1 + leng(s[1:])


def mylen(s):
    if s == "":
        return 0
    else:
        return 1 + mylen(s[1:])


test = mylen("hoi")
print("test is", test)


def mult(n, m):

    """mult returns the product of its two arguments

    Arguments: n and m are both integers

    Return value: the result of multiplying n and m

    """
    if n == 0 or m == 0:
        return 0
    elif m == 1:
        return n
    elif n == 1:
        return m
    elif n < 0:
        return


# test
assert mult(6, 7) == 42
assert mult(6, -7) == -42
assert mult(-6, 7) == -42
assert mult(-6, -7) == 42
assert mult(6, 0) == 0
assert mult(0, 7) == 0
assert mult(0, 0) == 0


def flipside(s):
    """flipside swaps s's sides
    Argument s: a string
    """
    x = len(s) // 2
    return s[x:] + s[:x]


#
# Tests
#
assert flipside("zijkant") == "kantzij"
assert flipside("huiswerk") == "werkhuis"
assert flipside("flipside") == "sideflip"
assert flipside("az") == "za"
assert flipside("a") == "a"
assert flipside("") == ""


def dot(L, K):
    if (
        len(L) != len(K) or L == [] or K == []
    ):  # len(L and K) not the same or L or K = []  return 0.0
        return 0.0
    elif len(L) != 0 or len(K) != 0:  # list length not 0
        return L[0] * K[0] + dot(L[1:], K[1:])  # ret


#
# Tests
#
assert dot([5, 3], [6, 4]) == 42.0
assert dot([1, 2, 3, 4], [10, 100, 1000, 10000]) == 43210.0
assert dot([5, 3], [6]) == 0.0
assert dot([], [6]) == 0.0
assert dot([], []) == 0.0


def ind(e, L):
    if e in L:  # check if e is in L
        if e == L[0]:  # if e is in possition 0 return 0
            return 0
        else:
            return 1 + ind(e, L[1:])  # coounts position till e is found
    if e not in L:
        return len(L)  # returns length of L if no e in L

    #


# Tests
#
assert ind(42, [55, 77, 42, 12, 42, 100]) == 2
assert ind(42, list(range(0, 100))) == 42
assert ind("hoi", ["hallo", 42, True]) == 3
assert ind("hoi", ["oh", "hoi", "daar"]) == 1
assert ind("i", "team") == 4
assert ind(" ", "nader onderzoek") == 5


def letter_score(let):
    """1:adeinorst
    2:ghl
    3:bcmp
    4:jkuvw
    5:f
    6:z
    8:xy
    10:q
    per punten zijn de letters verdeelt
    """
    if let in "adeinorst":
        return 1
    elif let in "ghl":
        return 2
    elif let in "bcmp":
        return 3
    elif let in "jkuvw":
        return 4
    elif let == "f":
        return 5
    elif let == "z":
        return 6
    elif let in "xy":
        return 8
    elif let == "q":
        return 10
    else:
        return 0


def scrabble_score(s):

    if len(s) == 0:
        return 0
    else:

        return scrabble_score(s[1:]) + letter_score(s[0])


#
# Tests
#
assert scrabble_score("quotums") == 24
assert scrabble_score("jacquet") == 24
assert scrabble_score("pyjama") == 20
assert scrabble_score("abcdefghijklmnopqrstuvwxyz") == 84
assert scrabble_score("?!@#$%^&*()") == 0
assert scrabble_score("") == 0


def one_dna_to_rna(c):
    """Converts a single-character c from DNA nucleotide
    to complementary RNA nucleotide
    """
    if c == "A":

        return "U"
    elif c == "C":

        return "G"
    elif c == "G":

        return "C"
    elif c == "T":

        return "A"
    else:
        return ""


def transcribe(s):
    if len(s) == 0:
        return ""
    else:
        #    return transcribe(s[1:]) + one_dna_to_rna(s[0]) #waarom werkt dit niet?
        return one_dna_to_rna(s[0]) + transcribe(s[1:])  # waarom dit werkt idk


#
# Tests
#
assert transcribe("ACGTTGCA") == "UGCAACGU"
assert transcribe("ACG TGCA") == "UGCACGU"  # De spatie verdwijnt
# assert transcribe('GATTACA')  == 'CUAAUGU' # CUAAUGU
assert transcribe("hanze") == ""  # Andere tekens verdwijnen
assert transcribe("") == ""
