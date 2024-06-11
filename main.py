import random
list = ["H", "T"]
listB = []
i = 0

listA = ["H", "H", "H"]

total = 10000
for _ in range(total):
    listB += random.choice(list)

s = "".join(x for x in listB)
#print(s)
o = "".join(x for x in listA)
#print(o)

x = 0
while x < len(s):
    if o in s[x:x+3]:
        #print("x2", x)
        #print("x", x, s[x:x+3])
        x += 3  # Increase x by 3 to skip the next few elements
        i += 1
    else:
        x += 1  # Only increment x by 1 to move to the next element

op = float(i/total)
print(f"chances of a streak(6*H) in 10k tries are ",op,"%")
