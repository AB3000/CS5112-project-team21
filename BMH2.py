# Boyer Moore String Search implementation in Python
# Ameer Ayoub <ameer.ayoub@gmail.com>

# Generate the Bad Character Skip List
def generateBadCharShift(term):
    skipList = {}
    for i in range(0, len(term)-1):
        skipList[term[i]] = len(term)-i-1
    return skipList

# Generate the Good Suffix Skip List
def findSuffixPosition(badchar, suffix, full_term):
    for offset in range(1, len(full_term)+1)[::-1]:
        flag = True
        for suffix_index in range(0, len(suffix)):
            term_index = offset-len(suffix)-1+suffix_index
            if term_index < 0 or suffix[suffix_index] == full_term[term_index]:
                pass
            else:
                flag = False
        term_index = offset-len(suffix)-1
        if flag and (term_index <= 0 or full_term[term_index-1] != badchar):
            return len(full_term)-offset+1

def generateSuffixShift(key):
    skipList = {}
    buffer = ""
    for i in range(0, len(key)):
        skipList[len(buffer)] = findSuffixPosition(key[len(key)-1-i], buffer, key)
        buffer = key[len(key)-1-i] + buffer
    return skipList

# Actual Search Algorithm
def BMSearch(source, pattern):
    goodSuffix = generateSuffixShift(pattern)
    badChar = generateBadCharShift(pattern)
    i = len(pattern) - 1
    while i < len(source)-1:
        j = 0
        while j < len(pattern) and pattern[len(pattern) - j - 1] == source[i - j - 1]:
            j += 1
        if j == len(pattern):
            #pattern has been found here
            #can be replaced by a counter
            return i - len(pattern)
        else:
            t = badChar.get(source[i - j - 1])
            if t is None:
                t = 6
            k = goodSuffix.get(j)
            if k is None:
                k = 0

            d1 = t - j

            i += max(d1, k)
    return -1

if __name__ == "__main__":
    #block = "This is a simple example"
    #print "This is an example search on the string \"", block, "\"."
    #print "ple  :", BMSearch(block, "ple ")
    #print "example :", BMSearch(block, "example")
    #print "simple :", BMSearch(block, "simple")
    #print " imple :", BMSearch(block, " imple")
    
    file = open('chimpanzee.txt', 'r')
    txt = file.read()
    pat = "GCATACGC"
    
    print(BMSearch(txt, pat))