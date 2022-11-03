# Programmeren I, Practicum 5
# Bestandsnaam: wk5ex1
# Naam:
# Probleemomschrijving: conversie binair <-> decimaal

def is_odd(x):
    """
    checks if x is odd or not
    """
    
    if x % 2 == 0 :
        return False
    else:
        return True

assert not is_odd(42)
assert is_odd(43)

def num_to_binary(n):
    """Converts a value to binary."""
    if n == 0:
        # een lege string als basisgeval
        return '' 
    elif n % 2 == 1: # is n oneven?
        # neem dan de binaire waarde van de helft, met een 1 er achter
        return num_to_binary(n // 2) + '1'
    else:
        # neem anders de binaire waarde van de helft, met een 0 er achter
        return num_to_binary(n // 2) + '0'


assert num_to_binary(0) == ""
assert num_to_binary(42) == "101010"


def binary_to_num(s):
    """
    """
    
    if s == "":
        return 0

    # als het laatste cijfer een '1' is...
    elif s[-1] == "1":

        return 2*binary_to_num(s[:-1]) + 1

    else:  # laatste cijfer moet een '0' zijn
    
        return 2*binary_to_num(s[:-1]) + 0


assert binary_to_num("") == 0
assert binary_to_num("101010") == 42


def increment(s):
    n = binary_to_num(s)
    x = n + 1
    y = num_to_binary(x)
    fin = len(s)-len(y)
    final= "0"*fin + y
    return final

def count(s, n):
    """binary counter
    count n times starting at s
    """
    
    print(s)
    if n == 0:
        return #stop
    elif s == (len(s)*'1'):
        ss = len(s)*'0'
        return count(ss,n-1)
    else:
        ss = increment(s)
        return count(ss,n-1)

def num_to_ternary(n):
    if n == 0:
        # een lege string als basisgeval
        return '' 
    elif n % 3 == 2: 
        # devide by 3 and add 2
        return num_to_ternary(n // 3) + '2'
    elif n % 3 == 1:
        # devide by 3 and add 1 
        return num_to_ternary(n // 3) + '1'
    else:
        # devide n by 3 and add 0
        return num_to_ternary(n // 3) + '0'

def ternary_to_num(s):
    if s == '':
        return 0
    elif s[-1] == '2':
        return 3*ternary_to_num(s[:-1])+2
    elif s[-1] == '1':
        return 3*ternary_to_num(s[:-1])+1
    else:
        return 3*ternary_to_num(s[:-1])+0