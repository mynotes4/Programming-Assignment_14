"""Question 1:
Define a class with a generator which can iterate the numbers, which are divisible by 7,
between a given range 0 and n."""

class Iterate:

	def __init__(self,n):
		self.n = n

	def iterate(self):
		l = []
		for i in range(1, self.n + 1):
			if i % 7 == 0:
				l.append(i)
		return l


n = int(input("Enter nth value "))
for i in Iterate(n).iterate():
	print(i)
