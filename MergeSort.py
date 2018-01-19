# MergeSort
# an example of the output of this file can be found in MergeResult.txt

import random

counter = 0 # keeping track of number of comparisons

''' merge sort script '''

def merge_sort(lst):
    global counter
    if len(lst) <= 1:
        counter += 1   # increment counter when we divide array in two
        return lst
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return merge(left, right)

def merge(left, right):
    global counter
    merged = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            counter += 1
            merged.append(left[i])
            i+=1
        else:
            merged.append(right[j])
            j+=1
    counter += 1
    merged += left[i:]
    merged += right[j:]
    return merged


lines = [line.rstrip('\n') for line in open('words.txt')] # reading each words and stripping the lines.
total = len(lines)
print(total)

''' All below this is to test on various inputs '''

''' Testing on 10 words '''
print('-------------')
print('Testing on 10 words')
print('10 words sorted')
tenWords = lines[0:10]
merge_sort(tenWords)
print('number of comparisons:', counter)
print('10 words reversed')
tenWordsReversed = list(reversed(tenWords))
merge_sort(tenWordsReversed)
print('number of comparisons:', counter)
print('10 words random')
# generating a random number and using it as the index start of my 10 words random array
tenRndm = random.randint(0,80000)
tenWordsRandom = lines[tenRndm:tenRndm+10] # start from that index to the next ten words
random.shuffle(tenWordsRandom) # shuffle the array in random order
merge_sort(tenWordsRandom)
print('number of comparisons:', counter)
print('-------------')
print('')

'''Testing on 30 words '''

print('-------------')
print('Testing on 30 words')
print('30 words sorted')
thirtyWords = lines[0:30]
merge_sort(thirtyWords)
print('number of comparisons:', counter)
print('30 words reversed')
thirtyWordsReversed = list(reversed(thirtyWords))
merge_sort(thirtyWordsReversed)
print('number of comparisons:', counter)
print('30 words random')
# generating a random number and using it as the index start of my 30 words random array
thirtyRndm = random.randint(0,80000)
thirtyWordsRandom = lines[thirtyRndm:thirtyRndm+30] # start from that index to the next thirty words
random.shuffle(thirtyWordsRandom) # shuffle the array in random order
merge_sort(thirtyWordsRandom)
print('number of comparisons:', counter)
print('-------------')
print('')

'''Testing on 100 words '''

print('-------------')
print('Testing on 100 words')
print('100 words sorted')
hundredWords = lines[0:100]
merge_sort(hundredWords)
print('number of comparisons:', counter)
print('100 words reversed')
hundredWordsReversed = list(reversed(hundredWords))
merge_sort(hundredWordsReversed)
print('number of comparisons:', counter)
print('100 words random')
# generating a random number and using it as the index start of my 100 words random array
hundredRndm = random.randint(0,80000)
hundredWordsRandom = lines[hundredRndm:hundredRndm+100] # start from that index to the next hundred words
random.shuffle(hundredWordsRandom) # shuffle in random order
merge_sort(thirtyWordsRandom)
print('number of comparisons:', counter)
print('-------------')
print('')

'''Testing on 300 words '''

print('-------------')
print('Testing on 300 words')
print('300 words sorted')
threeHundredWords = lines[0:300]
merge_sort(threeHundredWords)
print('number of comparisons:', counter)
print('300 words reversed')
threeHundredWordsReversed = list(reversed(threeHundredWords))
merge_sort(threeHundredWordsReversed)
print('number of comparisons:', counter)
print('300 words random')
# generating a random number and using it as the index start of my 300 words random array
threehundredRndm = random.randint(0,80000)
threeHundredWordsRandom = lines[threehundredRndm:threehundredRndm+300] # start from that index to the next 300 words
random.shuffle(threeHundredWordsRandom) # shuffle in random order
merge_sort(threeHundredWordsRandom)
print('number of comparisons:', counter)
print('-------------')
print('')

'''Testing on 1000 words'''

print('-------------')
print('Testing on 1000 words')
print('1000 words sorted')
thousandWords = lines[0:1000]
merge_sort(thousandWords)
print('number of comparisons:', counter)
print('1000 words reversed')
thousandWordsReversed = list(reversed(thousandWords))
merge_sort(thousandWordsReversed)
print('number of comparisons:', counter)
print('1000 words random')
# generating a random number and using it as the index start of my 1000 words random array
thousandRndm = random.randint(0,80000)
thousandWordsRandom = lines[thousandRndm:thousandRndm+1000] # start from that index to the next 1000 words
random.shuffle(thousandWordsRandom) # shuffle randomly
merge_sort(thousandWordsRandom)
print('number of comparisons:', counter)
print('-------------')
print('')

'''Testing on 3000 words'''

print('-------------')
print('Testing on 3000 words')
print('3000 words sorted')
threeThousandWords = lines[0:3000]
merge_sort(threeThousandWords)
print('number of comparisons:', counter)
print('3000 words reversed')
threeThousandWordsReversed = list(reversed(threeThousandWords))
merge_sort(threeThousandWordsReversed)
print('number of comparisons:', counter)
print('3000 words random')
# generating a random number and using it as the index start of my 3000 words random array
threeThousandRndm = random.randint(0,77000) # not 80000 here because total # of words is 81000~ so we don't want to go beyond that index-wise
threeThousandWordsRandom = lines[threeThousandRndm:threeThousandRndm+3000] # start from that index to the next 1000 words
random.shuffle(threeThousandWordsRandom)
merge_sort(threeThousandWordsRandom)
print('number of comparisons:', counter)
print('-------------')
print('')

'''Testing on 10000 words '''

print('-------------')
print('Testing on 10000 words')
print('10000 words sorted')
tenThousandWords = lines[0:10000]
merge_sort(tenThousandWords)
print('number of comparisons:', counter)
print('10000 words reversed')
tenThousandWordsReversed = list(reversed(tenThousandWords))
merge_sort(tenThousandWordsReversed)
print('number of comparisons:', counter)
print('10000 words random')
# generating a random number and using it as the index start of my 10000 words random array
tenThousandRndm = random.randint(0,70000) # again not 80000 because we don't want to go beyond the total # of words index-wise
tenThousandWordsRandom = lines[threeThousandRndm:threeThousandRndm+10000] # start from that index to the next 1000 words
random.shuffle(tenThousandWordsRandom)
merge_sort(tenThousandWordsRandom)
print('number of comparisons:', counter)
print('-------------')
print('')

''' Testing on all words '''

print('-------------')
print('Testing on all words')
print('all words sorted')
allWords = lines[0:len(lines)]
merge_sort(allWords)
print('number of comparisons:', counter)
print('all words reversed')
allWordsReversed = list(reversed(allWords))
merge_sort(allWordsReversed)
print('number of comparisons:', counter)
print('all words random')
random.shuffle(allWords)
merge_sort(allWords)
print('number of comparisons:', counter)
print('-------------')