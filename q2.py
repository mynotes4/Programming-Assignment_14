"""Question 2:
Write a program to compute the frequency of the words from the input. The output should output
after sorting the key alphanumerically.
Suppose the following input is supplied to the program:
New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
Then, the output should be:
2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1
"""
def frequency(s):
    s = s.split(' ')
    d = { }
    for i in s:
        d[i] = d.get(i,0) + 1
    return print_dict(d)

def print_dict(d):
    for i in sorted(list(d.keys())):
        print(i,":",d[i])

s = input("Enter Input ")
frequency(s)

