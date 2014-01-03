#!/usr/bin/python
from sklearn.ensemble import RandomForestClassifier
import numpy
import sys

def main():
	if len(sys.argv) < 5:
		print "Usage: [program] train test tree_num output [thread_num]"
		return
	elif len(sys.argv) == 5:
		threadNum = 1
	elif len(sys.argv) == 6:
		threadNum = int(sys.argv[5])

	print "try",int(sys.argv[3]),"trees with",threadNum,"threads"

	trainData = dataProcessor(sys.argv[1])
	testData = dataProcessor(sys.argv[2])
	target = [data.type for data in trainData]
	train = [data.matrix for data in trainData]
	test = [data.matrix for data in testData]

#	target = numpy.genfromtxt("./data/target.csv",delimiter=",")
#	train = numpy.genfromtxt("./data/train.csv",delimiter=",")
#	test = numpy.genfromtxt("./data/test.csv",delimiter=",")
	print "Data load over, start to generate trees"

	rf = RandomForestClassifier(n_estimators = int(sys.argv[3]),n_jobs=threadNum,oob_score=True)

	rf.fit(train,target)
	print "fit done, # of class:",rf.n_classes_,", oob score:",rf.oob_score_

	result = rf.predict(test)
	fout = open(sys.argv[4],"w")
	for i in result:
		tmp = int(i)
		fout.write(`tmp`+"\n")
	
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
		self.matrix = self.sparseToDense(points[1:])
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
		"""
		tmp = numpy.zeros((self.DATA_ROWS,self.DATA_COLUMNS))
		for point in points:
			place, value = point.split(":")
			place = float(place)
			value = float(value)
			tmp[place / self.DATA_COLUMNS][place % self.DATA_COLUMNS] = value
		return tmp
		"""
if __name__ == "__main__":
	main()
