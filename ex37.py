#1. String Formats

d = 10 # signed integer decimal
e = 1.2e2 # 120.0
f = 0.12345
g = 1.2e-5
i = 0
o = 011 # octal 9, (8^1 x 1) + (8^0 x 1)
s = 'A little string.'

print """
%d is a signed integer decimal
%i is a signed integer decimal
%o is a signed octal value of decimal value %d
%X is a signed Hexadecimal of decimal value %d
%c is a single char
%r is a string using repr()
%E is in floating point exp. format
%F is in floating point decimal format
%G is a floating point representation of %E
%s is a string
%% is a %% sign
""" % (d, i, o, o, d, d, 'a', '%^"%', e, f, g, g, s)

#2. Escape Sequences

print """
\\ Backslash
\' Single Quotation
\" Double Quotation
\\a - AscII Bell, not included due to noise
Backspace, will delete space in a b c : a \bb \bc
\f Not sure about what formfeed does
\n New line
123Carriage Return should put 'CR:' at start \rCR:
\t Tab - standard
\v vertical tab... ?
"""

#3. Data Types
True and 'a'
True or 'a'
False and 'a'
False or 'a'

del d, e, f, g, i, o , s
list = []
s = 'A String'
n = 0
float = 0.0

#4. Keywords
print "Lets get n over 100!"

while n < 100:
    try:
        s = raw_input('Enter an integer:')
        s = int(s)
    except ValueError, e:
        print '\n#Error:', e
    else:
        if n == 0:            
            print '0 + %d' %s
        elif n != 0:
            print '%d + %d' % (n, s)
    finally:
        try:
            n += s
        except TypeError as e:
            print '\n#That\'s not a number\n#', e, '\n'
        
        if n > 100:   
            print 'Success! n is over 100, with a value of %d!' % n

list = [n**2 for n in range(10)] # list is an iterable, list comprehension

print 'Squares of numbers under 10:'

for i in list:
    print i

print 'list:', list

def gen(x):
    """Print Squares of numbers under x"""
    print 'Squares of numbers under %d:' % x
    generator = (x**2 for x in range(x))
    
    for i in generator:
        print i
    
    print 'Generator:', generator

gen(3)
gen(7)

def gen2():
    """Yields generator, range(10) printing x + 100"""
    global gen_range
    gen_list = range(gen_range)
    for x in gen_list:
        yield x**2
# yield does not run code in function, returns generator object
# generator object is iterable

z = gen2() # () are a must
# z is now generator object
try:
    temp = raw_input('Range:')
    gen_range = int(temp)
except ValueError as e:
    print '\n#Enter a number please...\n'
print 'Yield Function:', gen2
print 'Yield Generated Generator:', z

try:
    for i in z:
        print i
except NameError as e:
    print '\n#Quit messing with the program'
    print '#You just pressed Enter or something didn\'t you?\n'

with open('a.txt') as file:
    for x in file:
        print x,

class horse:
    """It's a horse"""
    attribs = ['name', 'height', 'weight', 'cute', 'colour']
    name = 'Mr Horse'
    height = 120
    weight = 300
    cute = True
    colour = 'Brown'   
    def neigh(self):
        return 'NEIGH!!!!'

pooch = horse()
print pooch.neigh()
