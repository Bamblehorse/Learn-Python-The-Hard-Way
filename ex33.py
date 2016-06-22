def loop(x, count, j):  
    #while i < count:
    for i in range(x, count, j):
        print "At the top i is %d" % i
        numbers.append(i)
    
        #i = i + j
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i


numbers = []
loop(0, 6, 1)

print "The numbers: "

for num in numbers:
    print num