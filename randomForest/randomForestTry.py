#!/usr/bin/python
from sklearn.ensemble import RandomForestClassifier
import numpy
import sys

def main():
	if len(sys.argv) != 4:
		print "Usage: [program] [train] [test] [output]"
		return
	trainData = dataProcessor(sys.argv[1])
	testData = dataProcessor(sys.argv[2])

	print "Data load over, start to generate trees"

	target = [data.type for data in trainData]
	train = [data.matrix for data in trainData]
	test = [data.matrix for data in testData]
	numpy.savetxt("target.csv",target,delimiter=",")
	numpy.savetxt("train.csv",train,delimiter=",")
	numpy.savetxt("test.csv",test,delimiter=",")

	rf = RandomForestClassifier(n_estimators = 100,oob_score=True)

	rf.fit(train,target)
	print "fit done, # of class:",rf.n_classes_,", oob score:",rf.oob_score_

	result = rf.predict(test)
	fout = open(sys.argv[3],"w")
	for i in result:
		fout.write(`i`+"\n")
	
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
		tmp = [0 for k in range(20000)]
		for point in points:
			place, value = point.split(":")
			place = int(place)
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
