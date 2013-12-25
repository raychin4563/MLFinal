function nearest = calNearest(graph)
%initialize nearest and bfs buffer
	buf = [];
	nearest = zeros(rows(graph),columns(graph));
	pointRecord = zeros(rows(graph),columns(graph),2);
	for r = 1:rows(graph)
		for c = 1:columns(graph)
			nearest(r,c) = 1000;
			if graph(r,c) ~= 0
				buf = cat(1,buf,[r c]);
				nearest(r,c) = 0;
				pointRecord(r,c,1) = r;
				pointRecord(r,c,2) = c;
			end
		end
	end
%BFS
	while rows(buf) ~= 0
		r = buf(1,1);
		c = buf(1,2);
		buf = buf(2:end,:);
		rd = 0;
		cd = 0;
		for rd = [-1 1]
			tmpR = r+rd;
			tmpC = c+cd;
			if tmpR <= 0 || tmpC <= 0 || tmpR > rows(nearest) || tmpC > columns(nearest)
				continue;
			end
			distance = sqrt((tmpR - pointRecord(r,c,1))^2 + (tmpC - pointRecord(r,c,2))^2);
			if distance < nearest(tmpR,tmpC)
				nearest(tmpR,tmpC) = distance;
				pointRecord(tmpR,tmpC,1) = pointRecord(r,c,1);
				pointRecord(tmpR,tmpC,2) = pointRecord(r,c,2);
				buf = cat(1,buf,[tmpR tmpC]);
			end
		end
		
		rd = 0;
		cd = 0;
		for cd = [-1 1]
			tmpR = r+rd;
			tmpC = c+cd;
			if tmpR <= 0 || tmpC <= 0 || tmpR > rows(nearest) || tmpC > columns(nearest)
				continue;
			end
			distance = sqrt((tmpR - pointRecord(r,c,1))^2 + (tmpC - pointRecord(r,c,2))^2);
			if distance < nearest(tmpR,tmpC)
				nearest(tmpR,tmpC) = distance;
				pointRecord(tmpR,tmpC,1) = pointRecord(r,c,1);
				pointRecord(tmpR,tmpC,2) = pointRecord(r,c,2);
				buf = cat(1,buf,[tmpR tmpC]);
			end
		end
	end
