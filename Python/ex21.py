def add(a, b):
    print "ADDING %d + %d" %(a, b)
    return a + b # Use of return statements

def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d\n" % (age, height, weight, iq)

# A puzzle for extra credit, type it in anyway. Work this "inside out"
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes:", what, "a big negative - start with divide and work your way out."

try_this = add(weight, subtract(iq, weight)) # add 45 + 5 = 50

print "Let's try:", try_this