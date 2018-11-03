def loop():
    for counter in range(10):
        print ("GCI is great")


def questions():
    userName=input("What is your name? ")
    print("Hello " + userName + " , please to meet you!")
    reverseName=userName[::-1]
    print("Did you know that your name backwards is {}?".format(reverseName))
