string = raw_input("Name your text file:")
txt = open(string, "w+")
print "File name is %r." % txt.name

print "Add text to file:"
a ="\n"
b = raw_input("line 1:")
txt.write(b)
txt.write(a)
b = raw_input("line 2:")
txt.write(b)
txt.write(a)
b = raw_input("line 3:")
txt.write(b)

print "File now reads:"
txt.read()

print "By line:"
print txt.readline()
print txt.readline()
print txt.readline()


print "Saving file."
txt.close()
print "File closed."