"""
Question 5:
Please write a program to compress and decompress the string "hello world!hello world!hello
world!hello world!".
"""
import zlib

s = "hello world!hello world!hello world!hello world!".encode()
sc = zlib.compress(s)
print("Compressed String : " ,sc)
print("Decompressed string " , zlib.decompress(sc))