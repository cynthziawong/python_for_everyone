hrsscore = input("Enter Score: ")

try:
    hrsscore = float(hrsscore)
except:
    print("Please input Numeric Value")
    exit()

if hrsscore > 1.0 :
    print("Value out of range")
elif hrsscore >= 0.9 :
    print("A")
elif hrsscore >= 0.8 :
    print("B")
elif hrsscore >= 0.7 :
    print("C")
elif hrsscore >= 0.6 :
    print("D")
elif hrsscore < 0.0 :
    print("Value out of range")
else :
    print("F")
