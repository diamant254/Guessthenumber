def opencontact():
    
    viewcontact = input("Open contacts? y | n \n")
    
    if viewcontact == "y":
        print("Yes")
    elif viewcontact == "n":
        print("No")
    else:
        print("Try again")
        opencontact()

opencontact()


def readfile():
    file = open("contacts.txt", "r")
    print(file.read())

readfile()

def writefile():
    file = open("contacts.txt", "a")
