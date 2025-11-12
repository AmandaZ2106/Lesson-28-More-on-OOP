class Employee:
    def __init__(self):
        print("Employee created!")
    def __del__(self):
        print("Calling Destructor!")
def Create_obj():
    print("Creating Object!")
    obj=Employee()
    print("Function End..")
    return obj
print("Calling Create_obj function...")
obj=Create_obj()
print("Program ended...:")

