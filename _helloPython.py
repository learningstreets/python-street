# Hello Python
print("Hello Python")


# Comment
print("Use '#' before line starts to make that line commented")

""" 
This is 
Multi line Comments
"""
print("Use 'three double quotes' to make multi line comment.")


'''
 Whenever we declare a multi line commend just after a method or class definition or on top of the module
 then, that multi line comment gets convert into docStrings. We can access that by using objectName.__doc__
'''


def docStringFunction():
    """
    This is a docString function.
    """


print(docStringFunction.__doc__)




print("Know about Python")

print("Python is a Object Oriented Programming Language.")
print("Python uses Python Interpreter to compile the code.")
print("It is High Level, Case Sensitive language.")
print("The standard implementation of lPython is called cpyhon")
print("Python file Execution: Python Code ==(Bytecode)==> Python Virtual Machine =====> Machine Level Code  ")
print("First compilation happens in a interpreted manner into a ByteCode then an interpreter called Python Virtual Machine, executes the bytecode.")
print("Indentation is very very important in Python.")
print("")
print("")
print("")
