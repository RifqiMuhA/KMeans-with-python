import numpy

# input : data : list of int
def makeNewCenterPoint(data):
    banyak = int(0)
    sum = int(0)
    for i in data:
        sum = sum + i
        banyak = banyak + 1
    return (sum/banyak)


# this is a demonstration of the K-Means Algorithm. 
# for simplicity, the data set is only an int, making it one dimensional and easy to compute.

dataset = [9, 19, 29, 81, 61, 0, 91, 36, 18, 98, 54, 73, 64, 84, 25, 58, 25, 96, 47, 74, 14]

# the cluster will bwe done on a list. there will be 3 clusters
# the number 3 is chosen by random. there is a method to determine the optimal
# number of cluster, but for simplicity sake, we will stick to choosing it randomly. 
K1 = []
K2 = []
K3 = []

# Now we will make the center point for each clusters. the value of these center point is random.
# the same case with the number of clusters, there is a method to determine the center point so the result
# will be optimal. but for simplicity sake, we will choose it randomly.
p1 = int(97)
p2 = int(62)
p3 = int(6)

print("Inisiasi : ")
print("K1 = " + str(K1) + " p1 = " + str(p1))
print("K2 = " + str(K2) + " p2 = " + str(p2))
print("K3 = " + str(K3) + " p3 = " + str(p3))
print()

# we will now begin clustering the data
# var diff is th distance between the data and the center point
# This is the first iteration. 
# it is done separately because you cannot stop at one iteration, so you cant apply the end condition to the first iteration

print("Iterasi 1")
for i in dataset:
    diff1 = numpy.absolute(i - p1)
    diff2 = numpy.absolute(i - p2)
    diff3 = numpy.absolute(i - p3)

    if (diff1 < diff2 and diff1 < diff3):
        K1.append(i)
    elif(diff2 < diff1 and diff2 < diff3):
        K2.append(i)
    else:
        K3.append(i)
p1 = makeNewCenterPoint(K1)
p2 = makeNewCenterPoint(K2)
p3 = makeNewCenterPoint(K3)
print("K1 = " + str(K1) + " p1 = " + str(p1))
print("K2 = " + str(K2) + " p2 = " + str(p2))
print("K3 = " + str(K3) + " p3 = " + str(p3))

iterasi = 2
while True:
    print("\nIterasi " + str(iterasi))
    K1temp = []
    K2temp = []
    K3temp = []

    for i in dataset:
        diff1 = numpy.absolute(i - p1)
        diff2 = numpy.absolute(i - p2)
        diff3 = numpy.absolute(i - p3)

        if (diff1 < diff2 and diff1 < diff3):
            K1temp.append(i)
        elif(diff2 < diff1 and diff2 < diff3):
            K2temp.append(i)
        else:
            K3temp.append(i)
    p1 = makeNewCenterPoint(K1)
    p2 = makeNewCenterPoint(K2)
    p3 = makeNewCenterPoint(K3)

    print("K1 = " + str(K1) + " p1 = " + str(p1))
    print("K2 = " + str(K2) + " p2 = " + str(p2))
    print("K3 = " + str(K3) + " p3 = " + str(p3))

    if (K1temp == K1 and K2temp == K2 and K3temp == K3):
        print("Hasil iterasi " + str(iterasi) + " sama dengan hasil iterasi " + str(iterasi-1))
        print("Program diselesaikan")
        break
    else:
        K1 = K1temp
        K2 = K2temp
        K3 = K3temp
    iterasi = iterasi + 1



