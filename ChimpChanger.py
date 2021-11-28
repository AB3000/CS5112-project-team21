
from random import *

###################################################################
def change_chimp_c_and_g(txt): 
    
    new_string = "" 
    
    for letter in txt: 
        if letter == 'G':
            new_string = new_string + 'C'
        elif letter == 'C':
            new_string = new_string + 'G'
        else:
            new_string = new_string + letter
            
    with open('Chimp_c_and_g.txt', 'w', newline='') as file:
        file.write(new_string)

###################################################################
def change_chimp_random_letters(txt):
    
    trigger = 8
    new_string = ""
    choices = ['D', 'X', 'P', 'W', 'S', 'E', 'Q', 'Z', 'K', 'L']
    
    for letter in txt:
        random1 = randint(1,10)
        random2 = randint(0,9)
        if random1 == trigger:
            new_string = new_string + choices[random2]
        else:
            new_string = new_string + letter
            
    with open('Chimp_random.txt', 'w', newline='') as file:
        file.write(new_string)  
#####################################################################        
def chimp_triple(txt):
    
    new_string = txt + txt + txt
    
    with open('Chimp_triple.txt', 'w', newline='') as file:
        file.write(new_string)    
    
#############################################################
def chimp_A_then_Cs(txt):
    
    new_string = 'A'
    
    for letter in txt[1:]:
        new_string = new_string + 'C'
    
    with open('Chimp_A_then_Cs.txt', 'w', newline='') as file:
        file.write(new_string)    
#################################################################
def chimp_Cs_then_A(txt):

    new_string = ''
    
    for letter in txt[:-1]:
        new_string = new_string + 'C'
        
    new_string = new_string + 'A'
    
    with open('Chimp_Cs_then_A.txt', 'w', newline='') as file:
        file.write(new_string)  
        
#################################################################

def chimp_little_substrings(txt):
    
    choices = ['A', 'B', 'C', 'D', 'E']
    new_string = ''
    x = 0
    
    for letter in txt:
        choice = x % 5
        new_string = new_string + choices[choice]
        x = x + 1
        
    with open('Chimp_little_substrings.txt', 'w', newline='') as file:
        file.write(new_string)     


##############################################################

###################################################################
def change_chimp_all_letters(txt):
    
    new_string = ""
    choices = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N'
    , 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
    for letter in txt:
        print("letter")
        random_letter = randint(0,25)
        new_string += choices[random_letter]
            
    with open('Chimp_all_letters.txt', 'w', newline='') as file:
        file.write(new_string)  
##################################################################### 


file = open('chimpanzee.txt', 'r')
txt = file.read()

#change_chimp_c_and_g(txt[40:])

#change_chimp_random_letters(txt[40:])

#chimp_triple(txt[40:])

#chimp_A_then_Cs(txt[40:])

#chimp_Cs_then_A(txt[40:])

#chimp_little_substrings(txt[40:])

change_chimp_all_letters(txt)








#modified_string = txt.replace('C', 'G')
#return modified_string



