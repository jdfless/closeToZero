The p2.py function solves the close to zero problem (where you find the sub-array where the sum is closest to zero of
a given array) using the sum of suffices technique with the divide and conquer technique with either enumeration
or sort and compare. Algorithms 1 and 2 demonstrate the enumeration and sort and compare techniques with only the
sum of suffices.

Below is the usage of the program p2.py.

Jonathan Flessner
26-October-2014

p2.py accepts one or zero command line arguments.

---Random Array (no command line arg given)---
If you do not give a command line arg, the program will randomly generate an array of
numbers and find the subarray closest to zero.  The results for algorithm 3 will be 
output in a txt file called results3.txt.  The results of algorithm 4 will be output
in a txt file called results4.txt. If you would like to change the size of the array, 
alter the variable 'arrSize' on line 250. This is currently set to 50.  If you would 
like to change how many arrays are generated, change the variable 'repeat' on line 251.
This is currently set to 5.
-------------------------------------------------------------------------------------

---Arrays from a file (file given on command line)---
If you would like to use arrays from a txt file, give the input file name as a cmd
line arg. Ex. "python p2.py input.txt".  The program will use both the alg3 and alg4 
formulas to find the subarray(s) closest to zero and output them in a file named
[filename]_results3.txt and [filename]_results4.txt. If you have more than one cmd
line arg they will be ignored.  Errors will be thrown for files that do not exist or 
that are not .txt files.
-------------------------------------------------------------------------------------

WARNING: The program overwrites without prompt or warning any file with the same name
it is writing to. Any files named 'results3.txt' or 'results4.txt' will be overwritten
if you run the program w/o cmd line args.  Any file named '[filename]_results3.txt' or 
'[filename]_results4.txt' will be overwritten if you give that filename as the cmd line
argument.

Note: If the txt file you give as a cmd line arg is not formatted with one array per line
with the array in square brackets "[]" and the values seperated by commas the program
will not be able to properly map the array and will likely fail. If there are characters 
other than brackets, commas, newlines or ints (ie. any alpha character) the program will 
fail.

The output will always be [inputArray], [subArrayCtZ], ctzValue.
