f = open("2-locus-control.txt")
f1 = open("2-locus-control1.txt", 'w+')


line0 = f.readline()
#print line0,
#f1.writelines(line0)

for j in range(1,401):
    for i in range(1,201):
        xstr = f.read(1)
        if xstr == '0':
            pass
        elif xstr == '1':
            f1.write( 'a'+str(i/2+i%2)+',' )
        elif xstr == '2':
            f1.write('b'+str(i/2+i%2)+',')
    xstr = f.read(1)
    if xstr == '1':
        f1.write('case'+'\n')
    elif xstr == '0':
        f1.write('control'+'\n')
    xstr = f.readline()


f.close()
f1.close()


