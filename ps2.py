###### this is the second .py file ###########

####### write your code here ##########



import random
import math

count =0  # Variable to count the user within circle
user_count=input("Enter number of users") # Taking the no of user 
for points in range(user_count):
	(x,y)=(random.random()*2- 1, random.random()*2-1)
	#print(x,y)
	dist1=math.pow(x,2)
	dist2=math.pow(y,2)
	dist=dist1+dist2
	dist=math.pow(dist,0.5)  # calculate the distance from the bts
	if dist<=1:
		count += 1
		continue
#print count
perc=count/float(user_count)*100  # calculate the percentage
print "The percentage of user in the circle area :",perc




























