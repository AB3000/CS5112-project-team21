import time
import matplotlib.pyplot as plt
import numpy as np


#########################################################

# Rabin Karp Code:
def search(pat, txt, q):
    starting_indexes = []
    M = len(pat)
    N = len(txt)
    i = 0
    j = 0
    p = 0
    t = 0
    h = 1
    for i in range(M - 1):
        h = (h * d) % q

    for i in range(M):
        p = (d * p + ord(pat[i])) % q
        t = (d * t + ord(txt[i])) % q

    for i in range(N - M + 1):
        if p == t:
            for j in range(M):
                if txt[i + j] != pat[j]:
                    break
            j += 1
            if j == M:
                starting_indexes.append(str(i))
        if i < N - M:
            t = (d * (t - ord(txt[i]) * h) + ord(txt[i + M])) % q
            if t < 0:
                t = t + q
    return starting_indexes

def Rabin(text, pattern):
    f = open(text, "r")
    text = f.read()    
    # Rabin-Karp algorithm
    #print("Initiating Rabin-Karp algorithm")
    starting_time = time.time()
    q = 101
    result = search(pattern, text, q)
    ending_time = time.time() - starting_time
    #print(result, " time = ", ending_time)
    #print(" time = ", ending_time)
    #Times.append(ending_time)
    
    return ending_time




def CalculateD(file):
    f = open(file, "r")
    text = f.read()
    List = []
    for i in text:
        if i not in file:
            List.append(i)
    return len(List)

#######################################################

time1 = []
time2 = []

# if needed -- make sure to change the output print lines 
# from file or file2 variable to something concrete if you use this
f2 = open("Chimp_Cs.txt", "r")
Cpattern = f2.read()

repeats = 25

##Execute the code here
file = "Chimp_A_then_Cs.txt"
pattern = "AC"
file2 = "Chimp_A_then_Cs.txt"
pattern2 = "CA"
d = CalculateD(file)
for r in range(repeats):
    first_time = Rabin(file, pattern)
    time1.append(first_time)
    second_time = Rabin(file2, pattern2)
    time2.append(second_time)     

    

#file2 = "Chimp_little_substrings.txt"
#file2= "Chimp_not_found.txt"
#file2= "Chimp_random.txt"
#file2= "Chimp_spaces.txt"
#file2= "Chimp_special_chars.txt"
#file2= "Chimp_triple.txt"
#file2= "Chimp_A_then_Cs.txt"
#file2= "Chimp_bytes.txt"
#file2= "Chimp_c_and_g.txt"
#file2= "Chimp_Cs_then_A.txt"
#file2= "Chimp_newlines.txt"
#file2 = "abcde.txt"
#d = CalculateD(file2)

time1total = 0
time2total = 0

for s in range(repeats):
    time1total = time1total + time1[s]
    time2total = time2total + time2[s]
    print(time1[s], "     ", time2[s])
    
avg_time1 = time1total / repeats
avg_time2 = time2total / repeats

difference = avg_time2 - avg_time1
percent = (difference / avg_time1) * 100

if difference > 0:
    percent_moniker = "% increase"
else: 
    percent_moniker = "% decrease"

print("\n\n\n\n\n")
#print("Difference between searching for ", pattern, " in ", file, " and Cpattern in ", file2, "\n", \
print("Difference between searching for ", pattern, " in ", file, " and ", pattern2, " in ", file2, "\n", \
      "average time1 = ", avg_time1, "   average time2 = ", avg_time2, "\n", \
      "average difference = ", difference, "  average percentage = ", round(percent,2), percent_moniker)