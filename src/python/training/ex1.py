import datetime
responseName = input("Enter your name:")
responseAge = input("Enter your age:")
print("you will turn 100 in %s" %(100-int(responseAge) + int(datetime.datetime.now().year)))
