trainTmp = dlmread("./../train.dat"," ");
trainX = [];
trainy = trainTmp(:,1);
for i = 1:rows(trainTmp)
	for j = 2:columns(trainTmp)
		if trainTmp(i,j) ~= 0
			trainX(i,trainTmp(i,j)) = 1;
		end
	end
end
trainy
