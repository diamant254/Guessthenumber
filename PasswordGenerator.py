import random
import string

def new_password(length):
    string_digits = string.ascii_letters + string.digits
    result = ''.join(random.choice(string_digits) for i in range(length))
    print("You're new password is:")
    print(result)

    
def testinputlength():
    x = 0
    while True:
        if x == 0:
            lengthinput = input("How long is you're password gonna be?: ")
        if int(lengthinput) > 100:
            print("It's to long")
            continue
        elif lengthinput.isdecimal() == True:
            new_password(int(lengthinput))
            againpassword()
            break
        else:
            lengthinput = input("Just numbers: ")
            x = 1
            continue



def againpassword():
    again = input("One more password? y|n\n")
    if again == "y":
        testinputlength()

testinputlength()
