class UserID:
    def __init__(self, fname, age):
        self.fname = fname
        self.age = age

fname = input("Enter your first name: ")
age = int(input("Enter your age: ")) 

status = UserID(fname, age)

print(f"User Details: Name = {status.fname}, Age = {status.age}")
