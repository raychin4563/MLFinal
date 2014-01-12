data1 = importdata('92output');
data2 = importdata('output_s0t2g0.005c5');
data3 = importdata('output_random10000Int');

w = [0.9215 0.791 0.7441];
output = zeros(length(data1),1);

for i = 1:length(data1)
	count = zeros(1,12);
	count(data1(i)) = count(data1(i)) + w(1);
	count(data2(i)) = count(data2(i)) + w(2);
	count(data3(i)) = count(data3(i)) + w(3);
	
	maxRecord = count(1);
	maxIndex = 1;
	for j = 1:12
		if count(j) > maxRecord
			maxRecord = count(j);
			maxIndex = j;
		end
	end

	output(i) = maxIndex;
end
dlmwrite('blendingOutput',output);
