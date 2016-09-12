###### this is the first .py file ###########
####### write your code here ##########

import sys
from collections import Counter
#print str(sys.argv)
i=1
j=len(sys.argv)  #calculate the length of the input

#s=[]
#while (i<j):
#	var=sys.argv[i]
#	a=''.join(sorted(var))
#	s.append(a)



#i=1
lent=[]
while (i<j):
	lent.append(sys.argv[i])  # Append the all argument in a list
	#print sys.argv[i]
	i=i+1

s=" "
seq=lent
inputstring= s.join(seq)  #Make a single string of given input


list1=Counter(inputstring.split()).most_common()

print "most frequent word and frequency:",list1[0]
print "Second most frequent word and frequency:",list1[1]
print "Third most frequent word and frequency:",list1[2]


