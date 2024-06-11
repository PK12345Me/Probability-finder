import random

i = 0

# Generate a list of 10,000 random choices between "H" and "T"
listA = ["H", "H", "H", "H", "H", "H"]

total = 10000
listB = [random.choice(["H", "T"]) for _ in range(total)]

# creates a pattern
s = "".join(x for x in listB)
o = "".join(x for x in listA)

#actual caculation
x = 0
while x < len(s):
    if o in s[x:x+6]:
        # Increase x by 6 to skip the next few elements
        x += 6
        # Increase i by 1 to record presence of the desired pattern
        i += 1
    else:
        # Only increment x by 1 to move to the next element
        x += 1

op = float(i/total)
print(f"chances of a streak(6*H) in 10k tries are {op:.6f} %")
