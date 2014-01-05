#!/usr/bin/python
import sys

def main():
	if len(sys.argv) < 3:
		print "Usage: program output ans"
	foutput = open(sys.argv[1])
	fans = open(sys.argv[2])
	outputRaw = foutput.read()
	ansRaw = fans.read()
	output = outputRaw.split("\n")
	ans = ansRaw.split("\n")

	count = 0
	for i in range(len(ans)):
		if ans[i] == "":
			continue
		if int(ans[i]) == int(output[i]):
			count += 1
	accuracy = float(count) / len(ans)
	print "Accuracy:",accuracy

if __name__ == "__main__":
	main()
