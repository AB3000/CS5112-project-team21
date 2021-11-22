

"""
Brute force algorithm that searches for patten in block of text.
Prints all matching starting indices where pattern is found. 
Pulled from https://www.geeksforgeeks.org/naive-algorithm-for-pattern-searching/ 
"""
def brute_force_search(pat, txt):
    M = len(pat)
    N = len(txt)
 
    # A loop to slide pat[] one by one */
    for i in range(N - M + 1):
        j = 0
         
        # For current index i, check
        # for pattern match */
        while(j < M):
            if (txt[i + j] != pat[j]):
                break
            j += 1
 
        if (j == M):
            print("Pattern found at index ", i)


if __name__ == "__main__":
    file = open('chimpanzee.txt', 'r')
    text = file.read()
    pattern = "GCATACGC"
    brute_force_search(pattern, text)

