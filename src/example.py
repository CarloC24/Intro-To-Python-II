boolean = True
while boolean:
    x = input("parse command:")
    if x == "q" or "Q":
        print("exiting")
        break
    elif x == "n":
        print("north")