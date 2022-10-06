# Voorbeeldopgave lists, resultaat: [2, 7, 5, 9]
# [start:stop:step]
e = [2, 7, 1]
pi = [3, 1, 4, 1, 5, 9]

# answer 0: [2, 7, 5, 9]
answer0 = e[0:2] + pi[-2:]
print(answer0)

# opgave 1: [7, 1]
answer1 = e[-2:]
print(answer1)

# opgave 2: [1, 1, 2]
answer2 = pi[1:2] + pi[1:2] + e[0:1]
print(answer2)

# opgave 3: [1, 4, 1, 5, 9]
answer3 = pi[1:]
print(answer3)

# opgave 4: [1, 2, 3, 4, 5]
answer4 = e[-1::-2] + pi[0:5:2]
print(answer4)


# Oefeningen met strings

h = "hanze"
s = "hogeschool"
g = "groningen"

# Opgave 5:  'hoi' maken
answer5 = s[0:2] + g[4]
print(answer5)

# opgave 6: schoenen
answer6 = s[4:8] + g[-2:] * 2
print(answer6)

# opgave 7: anzeogeschool
answer7 = h[1:] + s[1:]
print(answer7)

# opgave 8: gnagnahahahahaha
answer8 = g[-3:-5:-1] + h[1] + g[-3:-5:-1] + h[1] * 5
print(answer8)

# opgave 9: legonoego
answer9 = s[-1] + s[-7:-10:-1] + g[-6:-8:-1] + s[-7:-10:-1]
print(answer9)

# opgave 10: leggings
answer10 = s[-1] + g[-2:-4:-1] + g[0:1] + g[4:7] + s[4]
print(answer10)
