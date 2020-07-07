# Assignment 3.1
# Task

hrs = input("Enter Hours:")
rate = input("Enter Rate:")

# Does the input work? Try / Except Statement
try :
    h = float(hrs)
    r = float(rate)
except :
    print("Error, please enter numeric input")
    quit() # Ends program

# If / Else Statement for any hours over 40
if h - float(40) <= 0 :
    pay = h*r
else :
    overtime = ((h-40)*1.5*r)
    pay = overtime + (40*r)

print(pay)
