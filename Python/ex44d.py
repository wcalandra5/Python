class Parent(object):

    def override(self):
        print "PARENT override()"

    def implicit(self):
        print "PARENT implicit()"

    def altered(self):
        print "PARENT altered()"

class Child(Parent):

    def override(self):
        print "CHILD override()"
    
    def altered(self):
        print "CHILD, BEFORE PARENT altered()"
        super(Child, self).altered() # remember, this will fetch the parent version
        print "CHILD, AFTER PARENT altered()"
    
dad = Parent()
son = Child()

dad.implicit()
son.implicit() # inherited from parent so no change

dad.override()
son.override() # this is overriden, so child version prints

dad.altered()
son.altered() # will print the parent version as well as the before and after
