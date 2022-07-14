"""
Question 6:
Please write a binary search function which searches an item in a sorted list.
The function should return the index of element to be searched in the list.
"""
def str_list(a):
    l = []
    a = a.split(" ")
    for i in a :
        l.append(int(i))
    return l


def binarySearch(a,n):
    l= 0
    a = str_list(a)
    u = len(a) - 1
    while l < u :
        m = (u + l)//2
        if n == a[m]:
            return m
        elif n > a[m]:
            l = m + 1
        else:
            u = m - 1
    return "No Element Found"

a = input("Enter sorted list of integers\n eg. 1 2 3 4 5\nEnter ")
n = int(input("Enter Element of search "))
print("Element Found at index :",binarySearch(a,n))