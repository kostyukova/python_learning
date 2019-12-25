file = open("yob1995.txt", "r")
maxname = None
maxcount = 0
max2name = None
max2count = 0
for line in file:
    (name, sex, count) = line.rsplit(",")
    count = int(count)
    if sex == 'F':
        print (name, count)
        if count > maxcount:
            max2name = maxname
            max2count = maxcount
            maxname = name
            maxcount = count
        elif count > max2count:
            max2name = maxname
            max2count = count
print ("Most popular", maxname, maxcount)
print ("Second popular", max2name, max2count)