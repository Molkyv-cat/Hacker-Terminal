from datetime import datetime

print("=== Login Terminal ===")

name = input("Username: ")
age = input("Age: ")

print("=== Access Granted ===")

timenow = datetime.now()

print("Hello!")

print("Your name:" , name)
print("Your age:" , age)
print("Time now:" , timenow.time())

print("=== Have a nice day! ===")
