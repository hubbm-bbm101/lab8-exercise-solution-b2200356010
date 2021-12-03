import sys
dic = {}
with open(sys.argv[1], "r") as data:
    for line in data:
        x = line.split(":")
        y = x[1].split(",")
        dic[x[0]] = y
a = sys.argv[2]
a = a.split(",")
for x in range(len(a)):
    try:
        print(f"Name:{a},University:{dic[a[x]][1]},{dic[a[x]][2]}\n")
    except KeyError:
        print(f"NO RECORD OF {a}")
