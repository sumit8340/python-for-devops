import sys

type = sys.argv[1]

if type == "t2.micro":
    print("Ok, we will create the instance for you")
elif type == "t2.large":
    print ("This is very costly")
else:
    print("Your input is not t2.micro we not able to create instance for you")