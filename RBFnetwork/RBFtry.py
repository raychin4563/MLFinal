#!/usr/bin/python
import numpy
import sys
import time
from math import exp

DATA_ROWS = 50
DATA_COLS = 50

def main():
#	testy = [[2,4],[3,5]]
#	testx = [[1],[1]]
#	print numpy.dot(testy,testx)
	if len(sys.argv) < 5:
		print "Usage: program train test gamma output"
		return

	trainData = dataProcessor(sys.argv[1])
	testData = dataProcessor(sys.argv[2])
	gamma = float(sys.argv[3])
	
	print "Data load over, "+`len(trainData)`+" datas is read. Start to calculate phi"

	timeRecord = time.clock()
	phi = genTransferMatrix(trainData,gamma)
	print "calculating phi is done, cost: %d sec".format(time.clock() - timeRecord)

	numpy.savetxt("phi.record",phi)

	y = [[d.type] for d in trainData]

	timeRecord = time.clock()
	w = numpy.dot(numpy.linalg.inv(phi),y)
	print "calculating inverse matrix is done, cost: %d sec".format(time.clock() - timeRecord)

	test = [data.data for data in testData]
	train = [data.data for data in trainData]
	output = genOutput(test,train,w,gamma)

	fout = open(sys.argv[4],"w")
	for o in output:
		fout.write(`o`+"\n")

	print "done"

def genOutput(test,train,w,gamma):
	output = []
	for testData in test:
		count = 0
		for i in range(len(train)):
			count += w[i] * exp(-gamma * distance(testData,train[i]))
		output.append(count)
#		if count >= 0:
#			output.append(1)
#		else:
#			output.append(-1)

def genTransferMatrix(datas,gamma):
	phi = [[0 for l in range(len(datas))] for k in range(len(datas))]
	for r in range(0,len(datas)):
		print `r`+"/"+`len(datas)`+" is done"
		for c in range(0,len(datas)):
			if r > c:
				phi[r][c] = phi[c][r]
			elif r == c:
				phi[r][c] = 1
			else
				phi[r][c] = exp(-gamma * distance(datas[r].data,datas[c].data))
	return phi

def distance(data1,data2):
	# 2 norm for intdata
	count = numpy.linalg.norm(numpy.subtract(data1,data2))
	return count
	"""
	queue1 = sorted(data1.keys())
	queue2 = sorted(data2.keys())
	go1 = 0
	go2 = 0
	count = 0
	while go1 != len(queue1) or go2 != len(queue2):
		if go1 == len(queue1):
			count += len(queue2) - go2
			go2 = len(queue2)
		elif go2 == len(queue2):
			count += len(queue1) - go1
			go1 = len(queue1)
		else:
			if queue1[go1] > queue2[go2]:
				count += 1
				go2 += 1
			elif queue1[go1] < queue2[go2]:
				count += 1
				go1 += 1
			else:
				go1 += 1
				go2 += 1
	return count
	"""

def dataProcessor(filepath):
        fin = open(filepath)
        raw = fin.read()
        fin.close()
        raws = raw.split("\n")
        datas = []
        for rawData in raws:
                if rawData == "":
                        break;
                datas.append(Data(rawData))
        return datas

class Data:
        def __init__(self,rawData):
                points = rawData.split(" ")
                self.type = float(points[0])
                self.data = self.sparseToDense(points[1:])
        def sparseToDense(self, points):
                tmp = [0 for k in range(2500)]
                for point in points:
			if point == "":
				continue
                        place, value = point.split(":")
                        place = int(place) - 1
                        value = float(value)
                        tmp[place] = value
                return tmp

if __name__ == "__main__":
	main()
