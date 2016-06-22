from sys import argv

script, filename = argv

txt = open(filename) #open(x.txt) call function on x.txt

print "Here's your file %r:" % filename #argv
print txt.read() 
#reads + prints the file, 
#txt var IS the file

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again) #same again

print txt_again.read() #also same

#raw_input for users, argv for programmers.

txt.close()
txt_again.close()
	

	
