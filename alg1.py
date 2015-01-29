"""
Jonathan Flessner, Christopher Sanford, Erin Marshall
20-October-2014
CS325 Project 2
"""

from random import randint

#from two arrays, find the sum of any two suffixes closest to zero
def alg1(s, t):
	#store sum of suffixs in arrays
	sumS = suffSum(s, len(s))
	sumT = suffSum(t, len(t))
	ansArr = findCtZ(sumS, sumT)
	return ansArr

#from an array, returns an array of the sum of every suffix in the given array
def suffSum(array, length):
	sumArray = []
	i = 0
	while i < length:
		curSum = sum(array[i:length])
		sumArray.append(curSum)
		i += 1
	return sumArray

#compares two arrays returned from suffSum and finds the pair closest to zero
#returns the place in each array this was found and the sum closest to zero 
def findCtZ(ss, st):
	i = 0
	j = 0
	ctz = ss[i] + st[j]
	iSum = i
	jSum = j
	while i < len(ss):
		while j < len(st):
			temp = ss[i] + st[j]
			if abs(temp) < abs(ctz):
				ctz = temp
				iSum = i
				jSum = j
			j += 1
		i += 1
		j = 0
	rtrnLst = []
	rtrnLst.extend((iSum, jSum, ctz))
	return rtrnLst



#generate random number array
def genArray(num):
	randArr = []
	for i in range(num):
		randArr.append(randint(-999,999))	#generate nums from -999 to 999 inclusive
	return randArr

#main
num = 100
s = genArray(num)
t = genArray(num)

ctz = alg1(s, t)
print ctz[2]


