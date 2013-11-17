import random
import math

#generate the list of all possible solutions (also in list form)
def sievecreator(col, num):
    guess, sieve=[], []
        
    permutations=col**num
    
    for p in range(0,permutations):
        sieve.append([])
        for i in range(0,num):
            sieve[p].append(1)
  
    for i in range(1,permutations):      
        sieve[i]=list(sieve[i-1])
        sieve[i].append(sieve[i].pop()+1)
        for j in range(len(sieve[i])-1,-1,-1):
            if sieve[i][j]>col:
                sieve[i][j-1]=sieve[i][j-1]+1
                sieve[i][j]=1
             
    return sieve

#counts reds and whites for a given guess compared to the solution
def checker(correct, guess):
    reds, whites=0,0
    whiteguess, whitecorrect=[], []

    for i in range(0, len(correct)):
        if correct[i]==guess[i]:
            reds+=1
        else:
            whiteguess.append(guess[i])
            whitecorrect.append(correct[i])
    
    for w in range(0, len(whitecorrect)):
        if whitecorrect[w] in whiteguess:
            whites+=1
            whiteguess.remove(whitecorrect[w])
       
    if reds<len(correct):
        result=[False, reds, whites]
    else:
        result=[True, reds, whites]                
    return result
    
def start(numberofcolors, numberofslots, listofpegs):
    #colors = int(raw_input("Enter the number of colors: "))
    colors=numberofcolors
    #numslots = int(raw_input("Enter the number of slots: "))
    numslots=numberofslots
    slots=[]

    for i in range(0, numslots):
        #slots.append(int(raw_input("Enter the color value of slot " + str(i) + ": ")))
        slots.append(listofpegs[i])
            
    possibilities=sievecreator(colors, numslots)
    tries=tearitapart(possibilities, slots)
    print ("The computer beat you in " + str(tries) + " tries!")
    
    return tries

def tearitapart(possibilities, slots):
    done=False
    count=0
    while not done:
        maxcolors=0
    
        for p in range(0,len(possibilities)):
            if len(set(possibilities[p]))>maxcolors:
                guessindex=p
                maxcolors=len(set(possibilities[p]))
    
        previous=possibilities[guessindex]
        result = checker(slots, previous)
        deleteindex=[]
        possibilities.remove(previous)
        print previous
        print ("Right Color Right Location: " + str(result[1]))
        print ("Right Color Wrong Location: " + str(result[2]))
    
        for p in range(0, len(possibilities)):
            redcount=0
            whitecount=0
            whitecopy=list(possibilities[p])
            for i in range(0, len(previous)):
                if previous[i]==possibilities[p][i]:
                    redcount+=1
                if previous[i] in whitecopy:
                    whitecount+=1
                    whitecopy.remove(previous[i])
            whitecount=whitecount-redcount
        
            if redcount<>result[1] or whitecount<>result[2]:
                deleteindex.append(p)
        for d in range(len(deleteindex)-1,-1,-1):
            del possibilities[deleteindex[d]]
        
        count+=1
        done=result[0]

    return count
