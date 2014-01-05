#!/usr/bin/python
import numpy
import sys
import time
from math import exp
from sklearn import cluster
from copy import deepcopy

class RBF:

	def __init__(self,gamma,k):
		self.hasTrained = False
		self.gamma = gamma
		self.k = k

	def test(self,data):
		if not self.hasTrained:
			return
		ans = [d[0] for d in data]
		predict = [0]*len(data)
		X = [d[1:] for d in data]
		for tmp in range(len(X)):
			print "("+`tmp`+")",
			sys.stdout.flush()
			x = X[tmp]
			# one versus one multiclassification
			count = [0 for l in range(self.classNum)]
			for i in range(self.classNum):
				for j in range(self.classNum):
					if i >= j:
						continue
					module = self.modules[(i,j)]
					centerSet = self.centerSets[(i,j)]
					sum = 0
					for k in range(len(module)):
						sum += module[k] * exp(- self.gamma * self.distance(x,centerSet[k]))
					count[i] += sum
					count[j] -= sum
			max = count[0]
			indexRecord = 0
			for i in range(self.classNum):
				if max < count[i]:
					max = count[i]
					indexRecord = i
			predict[tmp] = self.inverseMap[indexRecord]
		
		error = 0
		for i in range(len(ans)):
			if ans[i] != predict[i]:
				error += 1
		error /= len(ans)
		return predict, error

	def train(self,data):
		self.hasTrained = True
		#distinguish between classes
		classifiedData, self.classNum, self.inverseMap = self.classifyData(data)
		self.modules = {}
		self.centerSets = {}
		#do one versus one train
		for i in range(self.classNum):
			for j in range(self.classNum):
				print "("+`i`+","+`j`+")" ,
				sys.stdout.flush()
				if i >= j:
					continue
				module, centerSet = self.twoClassTrain(classifiedData[i],classifiedData[j])
				self.modules[(i,j)] = module
				self.centerSets[(i,j)] = centerSet
			print ""
	def classifyData(self,data):
		classified = []
		classes = set()
		map = {}
		inverseMap = {}
		count = 0
		
		for d in data:
			if d[0] not in classes:
				classes.add(d[0])
				map[d[0]] = count
				inverseMap[count] = d[0]
				count += 1
				classified.append([])
			classified[map[d[0]]].append(d)
		return classified, count, inverseMap

	def twoClassTrain(self,data1,data2):
		#y is a N * 1 matrix
		data = data1 + data2
		y = [[1 if d[0] == data1[0][0] else -1] for d in data]
		X = [d[1:] for d in data]
		centroid, label, inertia = cluster.k_means(X,self.k)
		phi = self.genTransferMatrix(X,centroid)
		w = numpy.dot(numpy.linalg.pinv(phi),y)
		return w, centroid
		
	#TODO: rewrite this function
	def genTransferMatrix(self,data,centers):
		phi = [[0 for l in range(len(centers))] for k in range(len(data))]
		for r in range(0,len(data)):
			for c in range(0,len(centers)):
				phi[r][c] = exp(- self.gamma * self.distance(data[r],centers[c]))
		return phi

	def distance(self,data1,data2):
		# 2 norm for intdata
		count = numpy.linalg.norm(numpy.subtract(data1,data2))
		count = count * count
		return count

def main():
	#testy = [[2,4],[3,5]]
	#testx = [[1], [1]]
	#print numpy.dot(testy,testx)
	if len(sys.argv) < 6:
		print "Usage: program train test gamma k output"
		return

	trainData = processData(sys.argv[1])
	testData = processData(sys.argv[2])
	gamma = float(sys.argv[3])
	k = int(sys.argv[4])
	RBFclassifier = RBF(gamma,k)
	print "Data load over, "+`len(trainData)`+" data is read."
	print "Start to train RBF network with gamma:" + `gamma` + " k: " + `k`

	timeRecord = time.clock()
	RBFclassifier.train(trainData)
	print "training is done, cost: " + `time.clock() - timeRecord` + " secs"
	print "start to test"

	timeRecord = time.clock()
	output, error = RBFclassifier.test(testData)
	print "test is done, error rate: " + `error*100` + "%, cost:",(time.clock() - timeRecord)

	fout = open(sys.argv[5],"w")
	for o in output:
		fout.write(`o`+"\n")
	fout.close()

	print "done"

def processData(filePath):
	fin = open(filePath)
	raw = fin.read()
	fin.close()
	raws = raw.split("\n")
	data = []
	for r in raws:
		if r == "":
			continue
		rawFeature = r.split(" ")
		feature = [0]*2501
		feature[0] = int(rawFeature[0])
		for f in rawFeature[1:]:
			if f == "":
				continue
			else:
				place, value = f.split(":")
				feature[int(place)] = float(value)
		data.append(feature)
	return data

if __name__ == "__main__":
	main()
