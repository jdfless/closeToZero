"""
Jonathan Flessner, Christopher Sanford, Erin Marshall
20-October-2014
CS325 Project 2
"""

from random import randint

def alg2(s, t):
	#store sum of suffixs in arrays
	sumS = suffSum(s, len(s))
	sumT = suffSum(t, len(t))
	#flip the sign of all values in sumT
	sumT[:] = [i*-1 for i in sumT]
	#check if two similar numbers - if so return
	dupCheck = set(sumS).intersection(sumT)
	#if dupCheck is true then ctz = 0
	#here the value single is the single item that will be positive in sumS, negative in sumT(orig)
	#that makes the sum of the suffices zero		
	if dupCheck:						
		single = dupCheck.pop()
		#use sumS.index(single) and sumT.index(single) to find index in list
		return 0

	A = sumS + sumT
	#print A
	A.sort()
	#print A
	i = 1
	j = 0
	smallDiff = 1998 						#1998 is largest possible ctz value 999 - -999
	while i < len(A):
		if A[i] in sumS and A[j] in sumT:
			diff = A[i] - A[j]
			if diff < smallDiff:
				smallDiff = diff
				place = i
		elif A[i] in sumT and A[j] in sumS:
			diff = A[i] - A[j]
			if diff < smallDiff:
				smallDiff = diff
				place = i
		i += 1
		j += 1

	return smallDiff

#from an array, returns an array of the sum of every suffix in the given array
def suffSum(array, length):
	sumArray = []
	i = 0
	while i < length:
		curSum = sum(array[i:length])
		sumArray.append(curSum)
		i += 1
	return sumArray

#generate random number array
def genArray(num):
	randArr = []
	for i in range(num):
		randArr.append(randint(-999,999))	#generate nums from -999 to 999 inclusive
	return randArr

#main
num = 10
s = genArray(num)
t = genArray(num)

print alg2(s, t)