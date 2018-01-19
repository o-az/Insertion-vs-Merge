import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import math

lines = [line.rstrip('\n') for line in open('words.txt')]

n = [10,30,100,300,math.pow(10,3),3*math.pow(10,3),math.pow(10,4),87314]
x = []
for i in n:
	x.append(math.log2(i)) # changing each in to log base 2

mergeResult = [34,53,82,212,271,386,901,1101,1216,2994,3594,5195,12125,14125,
               20431,43258,49258,70382,154989,174989,254116,1127233,1301861,2128330]

insertionResult = [9,54,35,29,464,264,100,5048,2426,300,45148,22476,1000,500498,
                   248592,3000,4501498,2244778,10000,50004998,24928746,87314,3811910947,1900942064]

# the below is list slicing to get 6 lists to apply the tests
sortedMerge = mergeResult[::3]
reversedMerge = mergeResult[1::3]
randomMerge = mergeResult[2::3]

sortedInsertion = insertionResult[::3]
reversedInsertion = insertionResult[1::3]
randomInsertion = insertionResult[2::3]

# line 1 is for sorted merge
x = [round(x,2) for x in x]
y = sortedMerge

# line 2 is for reversed merge
y2 = reversedMerge

# line 3 is for random merge
y3 = randomMerge

# line 4 is for sorted insertion
y4 = sortedInsertion

# line 5 is for reversed insertion
y5 = reversedInsertion

# line 6 is for random insertion
y6 = randomInsertion


plt.figure(figsize=(14,7))
plt.title("Plot 2:\n log(n) × nc/n\n note: 1e9 = One Billion")
plt.plot(x, y, label = 'Merge Sort sorted')
plt.plot(x, y2, label = 'Merge Sort reversed')
plt.plot(x, y3, label = 'Merge Sort random')
plt.plot(x, y4, label = 'Insertion Sort sorted')
plt.plot(x, y5, label = 'Insertion Sort reversed')
plt.plot(x, y6, label = 'Insertion Sort random')
plt.xlabel("log n")
plt.ylabel("nc/n")
plt.legend()
plt.show()
