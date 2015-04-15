f = open("2-locus_EDM-1_001.txt")
f1 = open("2-locus-case.txt", 'w+')
f2 = open("2-locus-control.txt",'w+')
line0 = f.readline()
print line0,
f1.writelines(line0)
f2.writelines(line0)

for i in range(1,801):
    line = f.readline()
    if i < 401:
        f1.writelines(line)
    else:
        f2.writelines(line)




f.close()
f1.close()
f2.close()
