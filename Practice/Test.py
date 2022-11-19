def ex_one(m):
    ''' calculates e=mc**2
    '''
    c = 299792458 #m/s
    e = m*c**2
    return e
def ex_two(p):
    grade = []
    if p >=90:
        grade + ['A']
        
    elif p >=80:
        grade + ['B']
        
    elif p >=70:
        grade + ['C']
        
    elif p >=60:
        grade + ["D"]
        
    else:
        grade + ["E"]


def ex_three(words):
    lengths = [len(x) for x in words if x > "HANZE" and x < "TENTAMEN"]
    return lengths


# ex_four
def manhatten(x, y):
    if x < 0 or y < 0:
        return 0
    elif x == 0 or y == 0:
        return 1
    else:
        return manhatten(x - 1, y) + manhatten(x, y - 1)
    