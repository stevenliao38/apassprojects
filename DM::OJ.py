import sys
sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")

n = int(input())
l = []
g = []
e = []
c = 0
for i in range(n):
   a = input()
   l.append(a)
if "S" not in l:
    print(1)
elif "P" not in l:
    print(l.count("S") - 1)
else:
    l.append('X')
    for i in range(n):
       if l[i + 1] == l[i]:
           c += 1
       else:
           c += 1
           g.append(l[i] + str(c))
           c = 0

    for i in range(1, len(g)-1):
      if g[i-1][0] == g[i+1][0]:
          if g[i] == "P1":
              e.append(1 + int(g[i-1][1:]) + int(g[i+1][1:]))
    for i in range(len(g)):
        if "S" in g[i]:
            e.append(int(g[i][1:]) + 1)
    print(max(e))
