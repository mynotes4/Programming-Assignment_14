"""
Question 4:
Please write a program to generate all sentences where subject is in ["I", "You"] and verb is
in ["Play", "Love"] and the object is in ["Hockey","Football"].
"""

l = []
l1 = ["I", "You"]
l2 = ["Play", "Love"]
l3 = ["Hockey","Football"]

for i in l1:
    for j in l2:
        for k in l3:
            l.append([i,j,k])

for i in l:
    print(' '.join(i))

