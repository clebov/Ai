import math
import RatioMap


class bayes(object):
    def __init__(self):
        # declare dictionaries to be used throughout out the program
        self.trainingSet = dict()  # used to store the label and the corresponding images
        self.testSet = dict()  # used to store the label and the corresponding Image
        self.pixProbmap = dict()  # 3d used to store the probability of an image being a label
        self.labelProb = dict()
        self.precision = dict()
        self.size = 28
        self.Scount = 0

        # a 2d array that keeps a counter for every time trainingSample() function makes
        # a guess for that label and guess
        self.confusionMatrix = []
        # a 2 d array that lays a common number that was mistaken to see where how the mistake occurred
        self.graphics = []
        self.graphics2 = []
        self.graphics3 = []
        self.graphics4 = []
        self.graphics5 = []
        self.graphics6 = []
        self.graphics7 = []
        self.graphics8 = []
        # variable used to print the accuracy of the bayes net
        self.match = 0
        self.Tcount = 0

    def createMatrix(self):
        for i in range(10):
            self.confusionMatrix.append([])
            for j in range(10):
                self.confusionMatrix[i].append(0)

    # print the confusion matrix which keeps track of how the program classifies an image
    def printMatrix(self):
        print()
        print("\t\t\t\t\t\t\t\t\tConfusion Matrix")
        print()
        print(' \t0 \t\t1 \t\t2 \t\t3 \t\t4 \t\t5 \t\t6 \t\t7 \t\t8 \t\t9')
        print("    --------------------------------------------------------------------------------  ")
        for i in range(10):
            print(i, end='\t')
            print("|", end='')
            for j in range(10):
                print(str(self.confusionMatrix[i][j]) + '\t\t', end='')
            print("|")

    def printAccuracy(self):
        print("The Accuracy of Naive Bayes Classifier = ", str(self.match * 100 / float(self.Tcount)) + "%")

        print("Digit\t\tPrecision")
        for digit in sorted(self.precision):
            lvpair = self.precision[digit]
            if lvpair != 0:
                print(" " + digit + "\t\t\t" + str("%.2f" % (lvpair[1] * 100 / float(lvpair[0]))) + "%")

            else:
                print(" " + digit + "\t\t\t" + "---")

    # create arrays that are used to store the log of the probabilities for each image with the highest confusion matrix
    def createGraphics(self):

        for i in range(28):
            self.graphics.append([])
            for j in range(28):
                self.graphics[i].append(0)

        for i in range(28):
            self.graphics2.append([])
            for j in range(28):
                self.graphics2[i].append(0)

        for i in range(28):
            self.graphics3.append([])
            for j in range(28):
                self.graphics3[i].append(0)

        for i in range(28):
            self.graphics4.append([])
            for j in range(28):
                self.graphics4[i].append(0)

        for i in range(28):
            self.graphics5.append([])
            for j in range(28):
                self.graphics5[i].append(0)

        for i in range(28):
            self.graphics6.append([])
            for j in range(28):
                self.graphics6[i].append(0)

        for i in range(28):
            self.graphics7.append([])
            for j in range(28):
                self.graphics7[i].append(0)

        for i in range(28):
            self.graphics8.append([])
            for j in range(28):
                self.graphics8[i].append(0)

    def trainSamples(self):
        self.calPrior()
        for label in self.trainingSet:
            self.calPixelProb(label)

    def calPrior(self):
        # calculate the prior label probabilities
        for label in self.trainingSet:
            # Compute Prior probability of each label
            self.labelProb[label] = (len(self.trainingSet[label]) + 1) / (float(self.Scount) + 3)

    def calPixelProb(self, label):
        gridProb = [[x for x in range(self.size)] for y in range(self.size)]
        # for each pixel in the trainingSet count how many times it a white , black, and grey pixel show up to be used
        # to calculate the probability of that pixel being white, black, or grey.
        for row in range(self.size):
            for col in range(self.size):
                whitePixel = 0
                greyPixel = 0
                blackPixel = 0
                for abc in self.trainingSet[label]:
                    if abc[row][col] == 1:
                        whitePixel += 1
                    if abc[row][col] == 2:
                        blackPixel += 1
                    if abc[row][col] == 3:
                        greyPixel += 1

                pixelProb = list()
                """Laplace smoothing is applied while evaluating pixel probability for each type of pixel"""
                # for laplace smoothing i choose .1 because i found that it had the greatest impact on the accuracy
                pixelProb.append((whitePixel + 1 * .1) / (float(len(self.trainingSet[label])) + 3 * .1))  # ' '


                pixelProb.append((blackPixel + 1 * .1) / (float(len(self.trainingSet[label])) + 3 * .1))  # '#'
                pixelProb.append((greyPixel + 1 * .1) / (float(len(self.trainingSet[label])) + 3 * .1))  # '+'

                gridProb[row][col] = pixelProb

                # Add 3d matrix to dictionary with label as key
            self.pixProbmap[label] = gridProb

    # take in the traininglabel and trainingimages files and convert the ASCII character in training images to values
    # to be used to calculate the prior probability(trainSample) as well as the pixel probability (calPixelProb)
    def Train(self):
        labels = open("traininglabels", 'r')
        images = open("trainingImages", 'r')
        count = 0
        # for every label in traininglabels
        for label in labels:

            label = label.rstrip('\n')
            sample = []
            for row in range(self.size):
                line = images.readline()
                line.rstrip('\n')
                row = list()
                for pixel in list(line):
                    count = count + 1
                    if pixel == ' ':
                        v = 1
                    elif pixel == '#':
                        v = 2
                    elif pixel == '+':
                        v = 3
                    row.append(v)
                if row: row.pop()
                # Append each row to sample
                sample.append(row)

            # Add sample to training set dictionary for corresponding label as key
            if label in self.trainingSet:
                self.trainingSet[label].append(sample)
            else:
                self.trainingSet[label] = [sample]
        self.Scount = count
        self.trainSamples()


    # take in the testlabel and testimages files and convert the ASCII character in training images to values
    #
    def Test(self):
        testlabel = open("testlabels", 'r')
        testimg = open("testimages", 'r')
        match = 0
        self.createMatrix()
        self.Tcount = 0
        for label in testlabel:
            self.Tcount = self.Tcount + 1
            label = label.rstrip('\n')
            sample = []
            for row in range(self.size):
                line = testimg.readline()
                line.rstrip('\n')
                row = list()
                for pixel in list(line):
                    if pixel == ' ':
                        v = 1
                    elif pixel == '#':
                        v = 2
                    elif pixel == '+':
                        v = 3
                    row.append(v)
                if row: row.pop()
                sample.append(row)

                if label in self.testSet:
                    self.testSet[label].append(sample)
                else:
                    self.testSet[label] = [sample]

                # applying  naive bayes here
                labelValPair = []
            if label in self.precision:
                labelValPair = self.precision[label]
                labelValPair[0] += 1

            else:
                self.precision[label] = [0, 0]
                labelValPair = self.precision[label]
                labelValPair[0] += 1
            # If label match given test label, increment count
            bestGuess = self.testingSample(label, sample)

            if label == bestGuess:
                self.match += 1
                labelValPair[1] += 1

    def testingSample(self, Test_label, sample):
        ValeMap = -float('inf')
        Guess = '0'

        # for the given label that is passed to the function find the pixProbmap that has the same key as the label
        # save the array with probability int
        for train_label in self.pixProbmap:
            trainedPixelGrid = self.pixProbmap[train_label]
            v_j = 0.0
            for row in range(self.size):
                for col in range(self.size):
                    val = sample[row][col]
                    prob = trainedPixelGrid[row][col][val - 1]
                    v_j += math.log(prob)
            v_j += math.log(self.labelProb[train_label])

            if v_j > ValeMap:
                ValeMap = v_j
                Guess = train_label

        # this section of the function increments a array for every time there is a guess made as a number
        testLabelToInt = int(Test_label)
        guessToInt = int(Guess)
        self.confusionMatrix[testLabelToInt][guessToInt] += 1

        return Guess


# create the object of the class bayes and call each function to train, test, print matrix, and then print the log
# likelihood of the number with the highest confusion matrix and the odd ratio.

classifier = bayes()
classifier.Train()
classifier.Test()
classifier.printAccuracy()
classifier.printMatrix()
RatioMap
