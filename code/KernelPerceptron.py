import math
import numpy as np
from itertools import izip

#0. Variables
# The size of our alphabet
# The size of the feature map for p = 3
# The size of the feature map for p = 4


#1. As we read from the file:
'''
    create a linear classifier 
    record the vectors for which we had mistakes
    Return the array of vectors for which we had mistakes
'''
def perceptron(trainfile, p):
    if p == 3:
	    w = [0] * 20 * 20 * 20
    else : #p = 4
        w = [0] * 20 * 20 * 20 * 20

	with open(trainfile, 'r') as file:
		for line in file:
			templine = map(int, line.split())
			label = templine[-1]
			featurevec = listOfSubstrings(templine[0], p)

			if (label * np.dot(w, featurevec)) <= 0:
				temparray = [label * x for x in featurevec]
				w = map(sum, izip(w, temparray))

	#get the error for the algorithm (Open testfile, and run)
'''	error = 0
	linecount = 0
	with open(testfile, 'r') as test:
		for line in test:
			linecount += 1
			templine = map(int, line.split())
			label = templine[len(templine) - 1]
			featurevec = templine[:-1]
			if label == 0:
				label = -1
			else:
				label = 1
			if (label * np.dot(w, featurevec)) <= 0:
				error += 1

	#print out the error
	print "Error on perceptron:", error, "/", linecount
'''
#2. Find how many substrings are in common between the two
def kernelSub(str1, str2, p)
    alreadyFound = []
    for i in range(0, len(str1) - p) :
        v = str1[i:(i+p-1)]
        if v in str2 and not (v in alreadyFound) :
            alreadyFound.append(v)

    return len(alreadyFound)

def runTest (perceptronArray, p, testFile)
    error = 0
    lineCount = 0
    with open(testFile, 'r') as file:
        for line in file:
            lineCount += 1
			templine = map(int, line.split())
            distance = 0
            for mistake in perceptronArray:
                label = mistake[-1]
                numSubstrings = kernelSub(tempLine[0], mistake[0], p)
                d = kernelSub(tempLine[0], tempLine[0], p) + kernelSub(mistake[0], mistake[0], p)
                distance += math.sqrt(d + 2 * numSubstrings) * label
            if (distance / abs(distance) != templine[-1]) :
                error += 1
    return float (error) / float (lineCount)

if __name__  == "__main__" :
    #1. generate the perceptron for size 3 (the list)
    p3 = perceptron(".\\hw5train.txt", 3)
    #2. generate the perceptron for size 4 (the list)
    p4 = perceptron(".\\hw5train.txt", 4)

    #3. Training Errors
    trainingError3 = runTest(p3, 3, ".\\hw5train.txt")
    print "Training error with p = 3: ", trainingError3
    trainingError4 = runTest(p4, 4, ".\\hw5train.txt")
    print "Training error with p = 4: ", trainingError4

    #4. Training Errors
    testError3 = runTest(p3, 3, ".\\hw5test.txt")
    print "Test error with p = 3: ", testError3
    testError4 = runTest(p4, 4, ".\\hw5test.txt")
    print "Test error with p = 4: ", testError4

