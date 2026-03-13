import sys
sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")

a = int(input())
b = int(input())
c = int(input())
if b - c - a < 0:
    print("N")
else:
    print("Y", b - c - a)
