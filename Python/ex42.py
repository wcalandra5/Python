# Animal is-a object (yes, sort of confusing) look at the extra credit - making a class named Animal that is-a object
class Animal(object):
    
    def __init__(self, age):

        # Add an age
        self.age = age

# Dog is-a Animal
class Dog(Animal):
    
    def __init__(self, name, age):

        # Inherit age from Animal
        super(Dog, self).__init__(age)

        # Dog has-a init that passes through self and name parameters
        self.name = name

        # Add a trick
        self.trick = ""


# Cat is-a Animal
class Cat(Animal):

    def __init__(self, name, age):

        # Inherit age from Animal
        super(Cat, self).__init__(age)

        # Cat has-a init passing through self and name parameters
        self.name = name

# Person is-a object
class Person(object):
    
    def __init__(self, name):

        #Person has-a init that passes through self and name parameters
        self.name = name

        # Person has-a pet of some kind
        self.pet = None

        # Add age
        self.age = 0

# Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        
        ## hmm what is this strange magic? - super() gives access to methods and props of a parent (or Base) class - so from Person get the name
        super(Employee, self).__init__(name)

        # Employee has-a salary set to parameter from self
        self.salary = salary

        # Adding title
        self.title = None

# Fish is-a object
class Fish(object):

    def __init__(self, name):

        # Add a name
        self.name = name
    
    def name_length(self): # notice it takes in an object and uses its props
        print len(self.name)


# Salmon is-a Fish
class Salmon(Fish):

    def __init__(self, name, prey):

        # Inherit name
        super(Salmon, self).__init__(name)

        # Add a prey
        self.prey = prey


# Halibut is-a Fish
class Halibut(Fish):
    
    def __init__(self, name, color):

        # Inherit Fish
        super(Halibut, self).__init__(name)

        # Add a color
        self.color = color

# rover is a Dog
rover = Dog("Rover", 15)

# satan is-a Cat
satan = Cat("Satan", 10)

# mary is-a Person
mary = Person("Mary")

# mary has-a pet named Satan - get pet attribute from Mary and set it to Satan
mary.pet = satan

# mary is 40
mary.age = 40

# Frank is-a employee
frank = Employee("Frank", 120000)

# frank has-a pet named Rover - get that pet attribute and set it to Rover
frank.pet = rover

# flipper is-a Fish
flipper = Fish('Flipper')

# crouse is-a salmon
crouse = Salmon('crouse', 10)

# harry is-a halibut
harry = Halibut('harry', 'red')

# Try function
harry.name_length() # works, prints 5