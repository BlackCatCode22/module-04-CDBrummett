han = open('mbox.txt')

for line in han:
    line = line.rstrip()
    wds = line.split()
    # guardian in a compound statement 
    if len(wds) < 3 or wds[0] != 'from' :
        continue
    print(wds[2])
