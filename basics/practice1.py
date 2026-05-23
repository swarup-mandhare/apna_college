print ("Welcome to the Result Dashboard!!")
name = input("Please enter your name : ")
print("Welcome",name)
Grade = int(input("enter you grade from 4-10"))
mks1 = int(input("pleae enter you English marks : "))
mks2 = int(input("pleae enter you Hindi marks : "))
mks3 = int(input("pleae enter you Physics marks : "))
mks4 = int(input("pleae enter you Chemistry marks : "))
mks5 = int(input("pleae enter you Maths marks : "))
average = (mks1 + mks2 + mks3 + mks4 + mks5)/5
if (average <38):
    print("You are failed")
elif (average <50):
    print ("You have secured E grade with",average," percent")
elif (average <65):
    print ("You have secured D grade with",average," percent")
elif (average <80):
    print ("You have secured C grade with",average," percent")
elif (average <90):
    print ("You have secured B grade with",average," percent")
else:
    print("Your have secured A grade with",average," percent")