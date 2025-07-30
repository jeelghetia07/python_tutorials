def fun():
    print("this is the fun function ")

def disp():
    print("this is the disp function ")

def msg():
    print("this is the msg function ")

functions = [fun,disp,msg]

for func in functions:
    func()

# Output:
# this is the fun function
# this is the disp function
# this is the msg function