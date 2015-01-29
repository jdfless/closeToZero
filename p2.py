"""
Jonathan Flessner, Christopher Sanford, Erin Marshall
24-October-2014
CS325 Project 2
"""

import math
from random import randint
from operator import itemgetter
import sys
import os.path
import time

def genArray(n):
	randomArray = []
	for z in range(n):
		randomArray.append(randint(minInt, maxInt))
	return randomArray

def alg3(A, low, mid, high):
	ctz = 999
	maxleft = low
	maxright = high

	b = []
	c = []
	bp = []
	cp = []

	#split array into b and c
	b = A[low:mid]
	c = A[mid:high+1]

	#create sum of suffices arrays bp and cp
	if len(b) > 0:	
		bp.append(b[-1])
		j = 0
		tot = bp[j]
		if abs(tot) < ctz:
			ctz = abs(tot)
			maxleft = mid-1
			maxright = mid-1
		i = len(b) - 2 				#-2 since we've already appended last value b[-1]
		while i >= 0:
			bp.append(b[i] + tot)
			j += 1
			tot = bp[j]
			if abs(tot) < ctz:
				ctz = abs(tot)
				maxleft = (mid-1)-j
				maxright = mid-1
			i -= 1
	#bp full, create cp
	if len(c) > 0:
		cp.append(c[0])
		j = 0
		tot = cp[j]
		if abs(tot) < ctz:
			ctz = abs(tot)
			maxleft = mid 			#was high for both
			maxright = mid
		i = 1
		while i < len(c):
			cp.append(c[i] + tot)
			j += 1
			tot = cp[j]
			if abs(tot) < ctz:
				ctz = abs(tot)
				maxleft = mid
				maxright = mid+i
			i += 1
	#cp full, check crossover ctz
	i = 0
	j = 0
	while i < len(cp):
		while j < len(bp):
			cur = cp[i] + bp[j]
			if abs(cur) < ctz:
				ctz = abs(cur)
				maxleft = (mid-1) - j
				maxright = mid+i
			j += 1
		i += 1
		j = 0
	return maxleft, maxright, ctz

def findCtZ3(A, low, high):
	if high == low:
		return low, high, abs(A[low]),		#base case with one element
	else:
		mid = int(math.floor(((low + high) / 2)))

		llow, lhigh, lctz = findCtZ3(A, low, mid)

		rlow, rhigh, rctz = findCtZ3(A, mid+1, high)

		clow, chigh, cctz = alg3(A, low, mid, high)

		if lctz <= rctz and lctz <= cctz:
			return llow, lhigh, abs(lctz)
			
		elif rctz <= lctz and rctz <= cctz:
			return rlow, rhigh, abs(rctz)
			
		else:
			return clow, chigh, abs(cctz)

def alg4(A, low, mid, high):
	ctz = 999
	b = []
	c = []
	bp = []
	cp = []
	maxleft = low
	maxright = high

	#split array into b and c
	b = A[low:mid]
	c = A[mid:high+1]

	#create sum of suffices arrays bp and cp
	if len(b) > 0:	
		bp.append(b[-1])
		j = 0
		tot = bp[j]
		if abs(tot) < ctz:
			ctz = abs(tot)
			maxleft = mid - 1
			maxright = mid - 1
		i = len(b) - 2 				#-2 since we've already appended last value b[-1]
		while i >= 0:
			bp.append(b[i] + tot)
			j += 1
			tot = bp[j]
			if abs(tot) < ctz:
				ctz = abs(tot)
				maxleft = (mid - 1) - j
				maxright = mid - 1
			i -= 1
	#bp full, create cp
	if len(c) > 0:
		cp.append(c[0])
		j = 0
		tot = cp[j]
		if abs(tot) < ctz:
			ctz = abs(tot)
			maxleft = mid
			maxright = mid
		i = 1
		while i < len(c):
			cp.append(c[i] + tot)
			j += 1
			tot = cp[j]
			if abs(tot) < ctz:
				ctz = abs(tot)
				maxleft = mid
				maxright = mid+i
			i += 1
	#cp full, check crossover ctz
	cp[:] = [i*-1 for i in cp]
	dupCheck = set(bp).intersection(cp)	#if there is a matching set now, ctz is 0 and can be returned
	if dupCheck:
		ctz = 0
		value = dupCheck.pop()
		maxleft = (mid-1) - bp.index(value)
		maxright = mid + cp.index(value)
		return maxleft, maxright, ctz
	ap = bp + cp
	temp = list(enumerate(ap))
	getval = itemgetter(1)
	apI = sorted(temp, key=getval)		#sorted with original indices
	ap.sort()
	i = 1
	j = 0
	if len(ap) == 1:
		print ap
	while i < len(ap):
		if ap[i] in bp and ap[j] in cp:
			diff = ap[i] - ap[j]
			if abs(diff) < ctz:
				ctz = abs(diff)
				t = apI[i]
				maxleft = (mid-1) - t[0]
				t = apI[j]
				cv = t[0] - len(bp)
				maxright = mid + cv
		elif ap[i] in cp and ap[j] in bp:
			diff = ap[i] - ap[j]
			if abs(diff) < ctz:
				ctz = abs(diff)
				t = apI[j]
				maxleft = (mid-1) - t[0]
				t = apI[i]
				cv = t[0] - len(bp)
				maxright = mid + cv
		i += 1
		j += 1
	return maxleft, maxright, ctz

def findCtZ4(A, low, high):
	if high == low:
		return low, high, abs(A[low])		#base case with one element
	else:
		mid = int(math.floor(((low + high) / 2)))

		llow, lhigh, lctz = findCtZ4(A, low, mid)

		rlow, rhigh, rctz = findCtZ4(A, mid+1, high)

		clow, chigh, cctz = alg4(A, low, mid, high)

		if lctz <= rctz and lctz <= cctz:
			return llow, lhigh, abs(lctz)
			
		elif rctz <= lctz and rctz <= cctz:
			return rlow, rhigh, abs(rctz)
			
		else:
			return clow, chigh, abs(cctz)			

#get array from file
def fromFile():
	filename = sys.argv[1]
	#basic error checking for valid .txt file
	if not os.path.isfile(filename):
		print "Sorry, the filename '" + filename + "' does not exist or cannot be opened."
		sys.exit()
	elif filename[-4:] != ".txt":
		print "The input file '" + filename + "' must be a .txt file."
		sys.exit()
	#open and format file, then run functions
	fd = open(filename, 'r+')
	notxtname = filename[:-4]				#remove the .txt
	listoflists = [] 
	
	for line in fd:
		openBrack = line.replace("[", "")
		closeBrack = openBrack.replace("]", "")
		newline = closeBrack.replace("\n", "")
		arr = newline.split(',')
		arr = map(int, arr)
		listoflists.append(arr)
	fd.close()

	return notxtname, listoflists


minInt = -999
maxInt = 999
arrSize = 100
repeat = 5

if len(sys.argv) < 2:					#no filename given, use random arrays
	fd3 = open('results3.txt', 'w')
	fd4 = open('results4.txt', 'w')
	for y in range(repeat):
		A = genArray(arrSize)
		start = time.clock()
		ctz3 = findCtZ3(A, 0, len(A)-1)
		stop = time.clock()
		print stop - start
		fd3.write(str(A) + ", " + str(A[ctz3[0]:ctz3[1]+1]) + ", " + str(ctz3[2]) + '\n')
		start = time.clock()
		ctz4 = findCtZ4(A, 0, len(A)-1)
		stop = time.clock()
		print stop - start
		fd4.write(str(A) + ", " + str(A[ctz4[0]:ctz4[1]+1]) + ", " + str(ctz4[2]) + '\n')
	fd3.close()
	fd4.close()
else:									#filename given, use this
	fileInfo = fromFile()
	fname = fileInfo[0]
	lol = fileInfo[1]
	f3name = fname + '_results3.txt'
	f4name = fname + '_results4.txt'
	fd3 = open(f3name, 'w')
	fd4 = open(f4name, 'w')
	z = 0
	while z < len(lol):
		A = lol[z]
		ctz3 = findCtZ3(A, 0, len(A)-1)
		fd3.write(str(A) + ", " + str(A[ctz3[0]:ctz3[1]+1]) + ", " + str(ctz3[2]) + '\n')
		ctz4 = findCtZ4(A, 0, len(A)-1)
		fd4.write(str(A) + ", " + str(A[ctz4[0]:ctz4[1]+1]) + ", " + str(ctz4[2]) + '\n')
		z += 1
	fd3.close()
	fd4.close()
sys.exit()
	

