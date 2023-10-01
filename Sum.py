file = "test01.txt"
mf = open(file, "rt")
sum = 0

with open(file) as mf:
    for i in mf:
        i = i.strip()
        nums = i.split(",")
        for a in nums:
            b = int(a)
            sum = sum + b

print(sum)