import time


def naiveSearching(pattern, text):
    lp = len(pattern)
    lt = len(text)
    count = 0
    index = []
    # the last few elements of the text cannot be matched anyway
    for i in range(lt-lp+1):
        found = True  # indicate the match
        for j in range(lp):
            if not text[i+j] == pattern[j]:  # mismatch
                found = False
                break
        if found:
            index.append(i)
            count += 1
    return count


text = "ABABDABACDABABCABAB"
pattern = "ABA"
# print(naiveSearching(pattern, text))

f = open('binary.txt', 'r')
text = f.read()
pattern = '10110101'

start = time.time()
print(naiveSearching(pattern, text))
end = time.time()
print("The elapsed time is " + str(end-start))


def calculateLPSArray(pattern):
    lps = [None] * len(pattern)
    i, j, lps[0] = 0, 1, 0
    while None in lps:
        if pattern[i] == pattern[j]:
            lps[j] = i+1
            i += 1
            j += 1
        else:
            if i == 0:
                lps[j] = 0
                j += 1
            if not i == 0:
                i = lps[i-1]
    return lps


def KMPSearch(pattern, text):
    lp = len(pattern)
    lt = len(text)
    count = 0
    lps = calculateLPSArray(pattern)
    i = 0
    j = 0

    while i < lt:  # iterate the pointer for the text
        # if single elements from text and pattern are matched
        if pattern[j] == text[i]:
            i += 1
            j += 1
            if j == lp:  # if the pointer is the length of pattern, the pattern is fully matched
                # note that j is out of the range of pattern because the pointer starts from 0
                # print("Found pattern at index " + str(i-j))
                count += 1
                j = lps[j-1]   # j is reset by the last value in the LPS array
        else:  # if mismatch
            if j == 0:  # first element from pattern doesn’t match, i is increased by one
                i += 1
            else:
                # or j is reset by the value of j-1 in the LPS array
                j = lps[j-1]
    return count


start = time.time()
print(KMPSearch(pattern, text))
end = time.time()
print("The elapsed time is " + str(end-start))
