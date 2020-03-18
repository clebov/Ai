from Net import classifier
import math

# this part of the program creats the Odd Ratio images

GraphicList = []
GraphicList2 = []

graphicImage = []
graphicImage2 = []
graphicImage3 = []
convertToASCII = []
oddRatioSeries = []

oddToImage = []
classifier.createGraphics()

label = ['4', '7', '8', '5']
label2 = ['9', '9', '3', '3']

for i in range(28):
    graphicImage.append([])
    graphicImage2.append([])
    graphicImage3.append([])
    oddToImage.append([])
    for j in range(28):
        oddToImage[i].append('')
        graphicImage[i].append('')
        graphicImage2[i].append('')
        graphicImage3[i].append('')

for row in range(28):
    for col in range(28):
        classifier.graphics[row][col] += (math.log(classifier.pixProbmap['4'][row][col][1]))
        classifier.graphics2[row][col] += (math.log(classifier.pixProbmap['9'][row][col][1]))

        classifier.graphics3[row][col] += (math.log(classifier.pixProbmap['7'][row][col][1]))
        classifier.graphics4[row][col] += (math.log(classifier.pixProbmap['9'][row][col][1]))

        classifier.graphics5[row][col] += (math.log(classifier.pixProbmap['8'][row][col][1]))
        classifier.graphics6[row][col] += (math.log(classifier.pixProbmap['3'][row][col][1]))

        classifier.graphics7[row][col] += (math.log(classifier.pixProbmap['5'][row][col][1]))
        classifier.graphics8[row][col] += (math.log(classifier.pixProbmap['3'][row][col][1]))

GraphicList.append(classifier.graphics)
GraphicList2.append(classifier.graphics2)

GraphicList.append(classifier.graphics3)
GraphicList2.append(classifier.graphics4)

GraphicList.append(classifier.graphics5)
GraphicList2.append(classifier.graphics6)

GraphicList.append(classifier.graphics7)
GraphicList2.append(classifier.graphics8)

for index in range(len(label)):

    graphicImage = []
    graphicImage2 = []
    graphicImage3 = []
    oddToImage = []

    for k in range(28):
        graphicImage.append([])
        graphicImage2.append([])
        graphicImage3.append([])
        oddToImage.append([])
        for j in range(28):
            oddToImage[k].append('')
            graphicImage[k].append('')
            graphicImage2[k].append('')
            graphicImage3[k].append('')

    a = ''
    for row in range(28):
        for col in range(28):
            b = GraphicList[index][row][col]
            if -8.99 <= b <= -4.00:
                a = ' '
            if -3.99 <= b <= -3.00:
                a = '.'
            if -2.99 <= b <= -2.00:
                a = '-'
            if -1.99 <= b <= -1.00:
                a = '+'
            if -0.99 <= b <= -0.00:
                a = '$'
            graphicImage[row][col] = a

    for k in graphicImage:
        for l in k:
            print(l, end='')
        print()

    for row in range(28):
        for col in range(28):
            b = GraphicList2[index][row][col]
            if -8.99 <= b <= -4.00:
                a = ' '
            if -3.99 <= b <= -3.00:
                a = '.'
            if -2.99 <= b <= -2.00:
                a = '-'
            if -1.99 <= b <= -1.00:
                a = '+'
            if -0.99 <= b <= -0.00:
                a = '$'
            graphicImage2[row][col] = a

    for k in graphicImage2:
        for l in k:
            print(l, end='')
        print()

    # Create an ASCII image for the odd ratio image and print to screen
    for row in range(28):
        for col in range(28):
            oddToImage[row][col] = math.log(
                classifier.pixProbmap[label[index]][row][col][1] / classifier.pixProbmap[label2[index]][row][col][1])

    for row in range(28):
        for col in range(28):
            b = oddToImage[row][col]
            if b > 1:
                a = '+'
            if .00 <= b <= 1.99:
                a = ' '
            if -.99 <= b <= -.00:
                a = "-"
            if -1.99 <= b <= -1.00:
                a = '*'
            if -2.99 < b <= -2.00:
                a = '#'
            graphicImage3[row][col] = a

    for k in graphicImage3:
        for l in k:
            print(l, end='')
        print()

    #
    # for index in range(len(oddRatioSeries)):
    #     for k in range(classifer.size):
    #         for l in range(classifer.size):
    #             print(oddRatioSeries[index][k][l], end='')
    #         print()
    i += 1

# END
