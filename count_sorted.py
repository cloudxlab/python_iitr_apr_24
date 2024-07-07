import sys
prev = None
count = 0
for line in sys.stdin:
	if line == prev:
		count += 1
	else:
		if prev != None:
			print(prev, count)
		count = 1
		prev = line
print(prev, count) 
