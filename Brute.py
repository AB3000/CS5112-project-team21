import time
import matplotlib.pyplot as plt
import numpy as np


######################################################

# Brute force search
def brute_force_search(pat, txt):
    M = len(pat)
    N = len(txt)
    for i in range(N - M + 1):
        j = 0
        while j < M:
            if txt[i + j] != pat[j]:
                break
            j += 1
        #if j == M:
            #print("Pattern found at index ", i)
            
def Brute(file, pattern):     
    
    Times = []
    f = open(file, "r")
    text = f.read()    
    # Brute Force Search
    #print("Initiating Brute Force Search algorithm")
    start_time = time.time()
    brute_force_search(pattern, text)
    ending_time = time.time() - start_time
    #print(" time = ", ending_time)
    Times.append(ending_time)
    return ending_time           



#########################################################

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
    first_time = Brute(file, pattern)
    time1.append(first_time)
    second_time = Brute(file2, pattern2)
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