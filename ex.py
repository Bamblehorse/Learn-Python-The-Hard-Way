# Learn Python The Hard Way
# Using code from all exercises

def t(ascii_decimal, exercise_number):
    """Prints 'Exercise' and Number, with ascii symbols either side."""
    ascii_char = chr(ascii_decimal)
    print '\n', ascii_char, 'EXERCISE', exercise_number, ascii_char,'\n'

def w():
        """Initiates empty raw input to pause output and wait for input"""
        prompt = '\n' + chr(178) + ' Press Enter/Return to continue...'
        raw_input(prompt)

a = 254 # Default ascii symbol, cube.
s = '  ' + chr(26)  # Arrow, >
d = '\t' + chr(175) # Double arrow, >>

print chr(219) + ' LEARN PYTHON THE HARD WAY ' + chr(219)
print '-----------------------------\n'

t(a,1)
print s, 'The print statement, using: " " and \' \'.'
print s, 'The \'Octothorpe\' character #, for comments.'

t(a,2)
print s, 'Use # to edit out code and leave useful info for yourself.'

t(a,3)
print s, 'Math symbols: + - / * % < > <= >='
print d, '100 + 30 = ', 100 + 30
print d, '100 - 30 = ', 100 - 30
print d, '100 / 30 = ', 100 / 30
print d, '100 * 30 = ', 100 * 30
print d, '100 % 30 = ', 100 % 30
print d, '100 < 30 = ', 100 < 30
print d, '100 > 30 = ', 100 > 30
print d, '100 <= 30 = ', 100 <= 30
print d, '100 >= 30 = ', 100 >= 30
print d, '100 <= 100 = ', 100 <= 100
print d, '100.0 / 30.0 = ', 100.0 / 30.0
print d, '100.0 % 30.0 = ', 100.0 % 30.0, '\n'
temp = (5 + 3) / (4 * 2) - (2 + 3)
print s, 'PEMDAS: (5 + 3) / (4 * 2) - (2 + 3) = ', temp
print d, 'Because: (8) / (8) - (5) = ', (8) / (8) - (5)
print d, 'Because: 1 - 5 = ', 1 - 5

t(a,4)
print s, 'Variables,'
print d, 'such as: x = \'String\' y = 1.234, and r = \'$tr4nge\''
x = 'String'
y = 1.234
r = '$tr4nge'
print d, 'Print x, y, r'
print d, x, y, r

t(a,5)
print s, 'Formatters,'
print d, 'Such as: %s, %d and %r % (x, y, r)'
print d, 'With variables x, y and r:'
print d, 'Such as: %s, %d and %r' % (x, y, r)
print s, 'Extra: round(y), round(y, 2)'
print d, round(y), ',', round(y, 2)

w()

t(a,6)
print s, 'Add: + between strings to join them, print x + r.'
print d, x + r

t(a,7)
print s, 'Multipy Strings and Commas to print onto the same line.'
print d, 'print x * 5: ', x * 5
print d, 'print x,'
print d, 'print r'
print d, x,
print r

t(a,8)
f = '%r %r'
print s, 'Add %\'s into variables.'
print d, 'f = "%r %r"'
print d, 'print f % (x, y)'
print d, f % (x, y)

t(a,9)
print s, 'Newline Escape and Triple Quotes:'
print d, 'print\'\\n\'\n'
print d, 'print """'
print d, 'multi-'
print d, 'line-'
print d, 'print'
print d, '"""'

t(a,10)
print s, 'All Escape Sequences:'
print d, '\\\\ Backslash \\'
print d, '\'Single-quote\''
print d, '\"Double-quote\"'
print d, '\\a - ASCII bell (BEL)'
print d, '\\b - ASCII backspace (BS) \b'
print d, '\\f - ASCII formfeed (FF) \f'
print d, '\\n - ASCII linefeed (LF) \n'
print d, 'u\'\\N{FULL BLOCK}\''
print d, u'- Char named in the unicode database(Unicode only)\N{FULL BLOCK}'
print '%s\\r - ASCII \rcarriage return (CR)' %d
print d, '\\t - \tASCII horizontal tab(TAB)'
print d, u'\\u00a9 - Character with 16-bit hex value 00a9 (Unicode), \u00a9'
print d, u'\\U000000a9 - Character with 32-bit hex value 000000a9 (Unicode), \U000000a9'
print d, '\\v\v - ASCII Vertical tab VT' 
print d, '\\020 - Character with octal value 20, \020'
print d, '\\x10 - Character with hex value 10, \x10'

w()

t(a,11)
print s, 'User Input:'
print d, 'temp = raw_input(\'Prompt:\')'
temp = raw_input(d + 'Prompt:')
print d, 'print temp'
print d, temp
print s, 'Note: Lines should be < 80 characters and input() is for python code'

t(a,12)
print s, 'Note:'
print d, 'You can use a prompt for raw input(\'here\')'
print d, 'In terminal: python -m pydoc "module"'

t(a,13)
print s, 'from sys import argv'
print d, 'x, y, z = argv'
print d, 'x = script name: module.py'

t(a,14)
print s, 'Use a variable as a raw_input(prompt)'

t(a,15)
print s, 'temp = open(\'a.txt\')'
temp = open('a.txt')
print d, 'print temp.read()\n'
print temp.read(), '\n'
print d, 'temp.close()'
temp.close()
temp = 0

w()

t(a,16)
print s, 'File commands:'
print d, '.close() - .read() - . readline() - .truncate() - .write(stuff)'
print s, 'temp = open(\'a.txt\', \'w\')'; temp = open('a.txt', 'w')
print d, 'temp.truncate()'; temp.truncate()
print d, 'temp.write(\'This is the data of a.txt\\n\')'
temp.write('This is the data of a.txt\n')
print d, 'temp.write(\'A text file.\\n\')'
temp.write('A text file.\n')
print d, 'temp.write(\'End of message.\')'
temp.write('End of message.')
print d, 'print temp.read()'
print d, 'temp.close()'; temp.close()
print s, 'temp = open(\'a.txt\', \'r\')'
temp = open('a.txt', 'r')
print d, 'print temp.read()\n'
print temp.read(), '\n'
print d, 'temp.close()'; temp.close()
print s, 'Note: w,r,a - w+,r+,a+ - w truncates and r is default'

t(a,17)
print s, 'from os.path import exists'; from os.path import exists
print d, 'exists(\'a.txt\')' ; exists('a.txt')
print d, 'len(\'string\') = ', len('string')

# ex 18 function
def one(*args):
    a1, a2 = args
    print '%r, %r' % (a1, a2)

t(a,18)
print s, 'def one(*args):'
print d, 'a1, a2 = args'
print d, 'print \'%r, %r\' % (a1, a2)'
print d, 'one(\'Fun-\', \'ction\')' ; one('fun-', 'ction')
print s, 'Functions can take many, or no ,arguments'



t(a,19)
print s, 'Functions can take math, numbers, strings, anything as arguments'

w()

t(a,20)
print s, '\'Rewind\' files - file.seek(0) /(0,1,2)'
print s, 'x += y notation, x = x + y, also extra:'
print d, '-=, *=, /=, %=, **=, //='
print d, 'is, is not, in, not in'

t(a,21)
print s, '\'return\' the result of a function, maybe to a variable.'

t(a,22)
print s, 'What do you know so far?'
print d, 'Everything in this file.'

t(a,23)
print s, 'Read some code'
print d, 'OK.'

t(a,24)
print s, 'Practice... Such as this file...'

t(a,25)
print s, 'temp = \'A pack of cards\''; temp = 'A pack of cards'
print d, 'print temp'; print d, temp
print s, 'words = temp.split(\' \')'; words = temp.split(' ')
print d, 'print words'; print d, words
print s, 'temp = sorted(words)'; temp = sorted(words)
print d, 'print temp'; print d, temp
print s, 'word = words.pop(0)'; word = words.pop(0)
print d, 'print word'; print d, word
print s, 'word = words.pop(-1)'; word = words.pop(-1)
print d, 'print word'; print d, word

print '\n', s, 'Extras:'
print d, 'import x (as y)'
print d, '"""Documentation comment"""'
print d, 'module.function(args)'
print d, 'from module import function'
print d, 'from module import *'

w()

t(a,26)
print s, 'Took a test.'

t(a,27)
print s, 'Memorizing Logic:'
print d, 'and, or, not'
print d, '!=, ==, >=, <='
print d, 'True, False'
print s, 'NOT:'
print d, 'not False:', not False
print d, 'not True:', not True
print s, 'OR:'
print d, 'True or False:', True or False
print d, 'True or True:', True or True
print d, 'False or True:', False or True
print d, 'False or False:', False or False
print s, 'AND:'
print d, 'True and False:', True and False
print d, 'True and True:', True and True
print d, 'False and True:', False and True
print d, 'False and False:', False and False

t(a,28)
print s, 'Took a test.'

w()

t(a,29)
print s, 'if True == True:'
print d, 'print \'That\'s True.'

if True == True:
    print '\n', s, 'That\'s True.'
    
t(a,30)
print s, 'if 2 > 5:'
print d, 'print \'Weird.\''
print s, 'elif 2 == 5:'
print d, 'print \'Hmm.\''
print s, 'else:'
print d, 'print \'Sounds right.\''

if 2 > 5:
    print 'Weird.'
elif 2 == 5:
    print 'Hmm.'
else:
    print '\n', s, 'Sounds right.'

t(a,31)
print s, '0 < x < 10, 0 <= x < 10, x in range(start, stop, increment)'

t(a,32)
print s, "list = [1, 2, 3, 4, 'a', 'b', 'c', 'd']"
list = [1, 2, 3, 4, 'a', 'b', 'c', 'd']
print s, 'for i in list:'
print d, 'print i\n'

for i in list:
    print d, i

print s, 'list = []'
print s, 'for i in range(0,20,2):'
print d, 'list.append(i)'
list = []

for i in range(0,20,2):
    list.append(i)

print '\n', s, 'print list'    
print d, list

print s, 'Note: x = [[a,b,c],[1,2,3]] - 2d list'
w()

t(a,33)
print s, 'temp = 0'
print s, 'while temp < 10:'
print d, 'print temp'
print d, 'temp += 1\n'

temp = 0

while temp < 10:
    print d, temp
    temp += 1
    
t(a,34)
print s, 'Ordinal = 1st, 2nd etc.'
print s, 'Cardinal = List element at location 0'

t(a,35)
print s, 'from sys import exit'
print s, 'while True - infinite loop'
print s, 'exit(0) - clean exit'

t(a,36)
print s, 'Design/Debug - Write program'

w()

t(a,37)
print s, 'Symbol Review:'
import ex37

