class Parent(object): # Parent class of object.

    def override(self): # parent has-a function/method override with
        print "PARENT override()"
        
    def implicit(self):
        print "PARENT implicit()"
        
    def altered(self):
        print "PARENT altered()"
        
class Child(Parent): # Child class of parent

    def override(self): # same as parent, overrides
        print "CHILD override()"
        
    def altered(self): # same as parent, overrides
        print "CHILD, BEFORE PARENT altered()"
        super(Child, self).altered()
        print "CHILD, AFTER PARENT altered()"

dad = Parent() # dad is instance of parent class
son = Child() # son instance of Child, Child class of parent

dad.implicit() #P imp
son.implicit() #P imp

dad.override() # P over
son.override() # C over

dad.altered() # P alt
son.altered() # C before, p alt, c aft p alt