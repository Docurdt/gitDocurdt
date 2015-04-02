f = open("one-locus_EDM-1_001.txt")
o = open("one.txt",'w')             
line0 = f.readline()            
print line0, 

line = f.readline()
line2 = []
line2 = line.replace('	', ',')
print line2
line2 = line2.replace('0,','')
line2 = line2.replace(',0','')
print line2,
a = line2.count('1')
print a
for j in range(0, a):
	line2 = line2.replace(' 1','a'+str(line2.find('1')),1)
	print line2.find('1')
print line2
f.close()
