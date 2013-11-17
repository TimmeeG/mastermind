import mastermind

a=6
b=6
numtests=a**b
totaltries=0
maxtries=0
maxtest=[]

testsieve=mastermind.sievecreator(a,b)

for num in range(0, numtests):
    numtries=mastermind.start(a,b,testsieve[num])
    totaltries=totaltries+numtries
    if numtries>maxtries:
        maxtries=numtries
        maxtest=[]
        maxtest.append(testsieve[num])
    elif numtries==maxtries:
        maxtest.append(testsieve[num])
        
averagetries=totaltries/float(numtests)

print ("The average number of tries was " + str(averagetries) + "!")
print ("The maximum numer of tries was " + str(maxtries) + "!")
print ("The hardest solutions to find are:")
print maxtest
