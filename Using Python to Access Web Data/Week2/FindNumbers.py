import re

f = "regex_sum_1113514.txt"
fhandle = open(f)
sum = 0
count = 0

for line in fhandle:
    stuff = re.findall("[0-9]+", line)
    for num in stuff:
        sum = int(sum) + int(num)
        count = 1 + count

print("There are ",count , "values with a sum =", sum)

#print(sum([line for line in re.findall('[0-9]+',fhandle.read())]))
