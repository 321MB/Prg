def one_to_sum(n):
    """Sum all integer values from 1 to n
    """
    if n==0:
        return 0
    else:    
        return one_to_sum(n-1) +n

assert one_to_sum(0) == 0
assert one_to_sum(1) == 1 
assert one_to_sum(3) == 6   # 3 + 2 + 1
assert one_to_sum(5) == 15  # 5 + 4 + 3 + 2 + 1

def sum_list(L):
    """Sum all values in L
    """
    if L == []:
        return 0
    else:
        return sum_list(L[:-1]) + L[-1]

assert sum_list([2, 6, 9]) == 17
assert sum_list([4]) == 4
assert sum_list([]) == 0

def mult_of_five(n):
    """Return a list containing the first n multiples of 5
    """
    L=[]
    if n==0:
        return L
    else:
        x = 5*n
        print("werk ", L, x)
        L.append(x)
        return mult_of_five(n-1)

def power_n(b, n):
    """Return base b to the power of n
    """
    #debug
    #print("-"*10)
    #print("n is ",n)
    #print("b is ",b)
    #print("-"*10) 

    #code
    if n == 0 and b!=0:
        return 1
    elif n!=0 and b==0:
        return 0
    elif n == 0 and b == 0:
        return 1
    else:
        return power_n(b,n-1) * b 

assert power_n(0, 0) == 1
assert power_n(0, 1) == 0
assert power_n(1, 1) == 1
assert power_n(2, 2) == 4
assert power_n(2, 3) == 8
assert power_n(3, 2) == 9


def double_letters(s):
    """Double all letters in s
    """
    if len(s) == 0:
        return ""
    else:
        return s[0]*2 + double_letters(s[1:])

assert double_letters("hi") == "hhii"
assert double_letters("hello") == "hheelllloo"


def no_x(s):
    """Return s with all x's removed 
    """
    if len(s) == 0:
        return ""
    elif s[0] == "x":
        return "" + no_x(s[1:])
    elif s[0] != "x":
        return s[0] + no_x(s[1:])

     
assert no_x("x1xx2x3") == "123"
assert no_x("xxx") == ""

def all_star(s):
    """Returns string s with all characters separated by *
    """
    if len(s) == 0:
        return ""
    elif len(s) == 1:
        return s[0]+all_star(s[1:])
    else:
        return s[0]+"*"+all_star(s[1:])

assert all_star("hello") == "h*e*l*l*o"
assert all_star("hi") == "h*i"
assert all_star("") == ""



def divisible_by(n, L):
    """Return a list with values in L divisible by n
    """

    if len(L) == 0:
        return []
    elif L[0] % n == 0:
        return [L[0]] + divisible_by(n, L[1:]) 
    else:
        return divisible_by(n, L[1:])


def starts_with(s, L):
    """Return all strings in L which start with s
    """
    x = len(s)    
    if len(L)==0:
        return []
    
    elif L[0][0:x] == s:
        return [L[0]] + starts_with(s, L[1:])
   
    else:
    
        return starts_with(s,L[1:]) 

assert starts_with("a", []) == []
assert starts_with("a", ["bbc", "brits", "omroep"]) == []
assert starts_with("a", ["abc", "cde", "aha", "abba"]) == ["abc", "aha", "abba"]
assert starts_with("ab", ["abc", "cde", "aha", "abba"]) == ["abc", "abba"]
assert starts_with("abc", ["abc", "cde", "aha", "abba"]) == ["abc"]
assert starts_with("abcd", ["abc", "cde", "aha", "abba"]) == []

def end_x(s):
    """Returns s with all x's moved to the end
    """
    if len(s) == 0:
        return ""
    elif s[0] == "x":
        return end_x(s[1:]) + s[0]
    elif s[0] != "x":
        return s[0] + end_x(s[1:])

output = end_x("abxyz")
