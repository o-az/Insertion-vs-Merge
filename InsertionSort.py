# Insertion Sort

# note: insertion sort takes a long time (10 mins appx.) to run on all words in reverse order
# and all words in random order

# # an example of the output of this file can be found in InsertionResult.txt

import random

lines = [line.rstrip('\n') for line in open('words.txt')]
# reading each words and stripping the lines.

def insertionSort(values):
    k = 0
    n = len(values) - 1
    comparisons = 0
    while k+1 <= n:
        i = k+1
        curr_val = values[i]
        comparisons += 1
        while i>0 and values[i-1] > curr_val:
            values[i] = values[i-1]
            i=i-1
            comparisons += 1
        values[i] = curr_val
        k = k + 1
    return 'number of comparisons', comparisons


''' All below this is to test on various inputs '''

''' Testing on 10 words '''
print('-------------')
print('Testing on 10 words')
print('10 words sorted')
print(insertionSort(lines[0:10]))
print('10 words reversed')
print(insertionSort(list(reversed(lines[0:10]))))
print('10 words random')
tenRndm = random.randint(0,80000)
randomTen = lines[tenRndm:tenRndm+10]
random.shuffle(randomTen)
print(insertionSort(randomTen))
print('-------------')

'''Testing on 30 words'''
print('-------------')
print('Testing on 30 words')
print('30 words sorted')
print(insertionSort(lines[0:30]))
print('30 words reversed')
print(insertionSort(list(reversed(lines[0:30]))))
print('30 words random')
thirtyRndm = random.randint(0,80000)
randomThirty = lines[thirtyRndm:thirtyRndm+30]
random.shuffle(randomThirty)
print(insertionSort(randomThirty))
print('-------------')
print('')

'''Testing on 100 words '''

print('-------------')
print('Testing on 100 words')
print('100 words sorted')
print(insertionSort(lines[0:100]))
print('100 words reversed')
print(insertionSort(list(reversed(lines[0:100]))))
print('100 words random')
hundredRndm = random.randint(0,80000)
randomHundred = lines[hundredRndm:hundredRndm+100]
random.shuffle(randomHundred)
print(insertionSort(randomHundred))
print('-------------')
print('')

'''Testing on 300 words '''

print('-------------')
print('Testing on 300 words')
print('300 words sorted')
print(insertionSort(lines[0:300]))
print('300 words reversed')
print(insertionSort(list(reversed(lines[0:300]))))
print('300 words random')
tHundredRndm = random.randint(0,80000)
randomTHundred = lines[tHundredRndm:tHundredRndm+300]
random.shuffle(randomTHundred)
print(insertionSort(randomTHundred))
print('-------------')
print('')

'''Testing on 1000 words '''

print('-------------')
print('Testing on 1000 words')
print('1000 words sorted')
print(insertionSort(lines[0:1000]))
print('1000 reversed')
print(insertionSort(list(reversed(lines[0:1000]))))
print('1000 words random')
kRndm = random.randint(0,80000)
randomK = lines[kRndm:kRndm+1000]
random.shuffle(randomK)
print(insertionSort(randomK))
print('-------------')
print('')

'''Testing on 3000 words'''

print('-------------')
print('Testing on 3000 words')
print('3000 words sorted')
print(insertionSort(lines[0:3000]))
print('3000 words reversed')
print(insertionSort(list(reversed(lines[0:3000]))))
print('3000 words random')
tkRndm = random.randint(0,70000)
randomtK = lines[tkRndm:tkRndm+3000]
random.shuffle(randomtK)
print(insertionSort(randomtK))
print('-------------')
print('')

'''Testing on 10000 words '''


'''Testing on 10000 words '''

print('-------------')
print('Testing on 10000 words')
print('10000 words sorted')
print(insertionSort(lines[0:10000]))
print('10000 words reversed')
print(insertionSort(list(reversed(lines[0:10000]))))
print('10000 words random')
thKRndm = random.randint(0,70000)
randomthK = lines[thKRndm:thKRndm+10000]
random.shuffle(randomthK)
print(insertionSort(randomthK))
print('-------------')
print('')

''' Testing on all words '''

print('-------------')
print('Testing on all words')
print('all words sorted')
print(insertionSort(lines[0:len(lines)]))
print('all words reversed')
print(insertionSort(list(reversed(lines[0:len(lines)]))))
print('all words random')
allWords = lines[0:len(lines)]
random.shuffle(allWords)
print(insertionSort(allWords))
print('-------------')