f = open("interesting_drink.txt", "a")
f.write('100000\n')
for i in range(100000):
    f.write(str(i+1)+" ")
f.write('\n')
f.write('100000\n')
for i in range(100000):
    f.write(str(i+1)+"\n")
f.close()
