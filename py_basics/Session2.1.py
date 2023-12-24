#variable scope
#local
#global
#builtin
#a = 45
#b = 65.43
#c ="stryhb"
#
#print(a,b,c)
#s = "welcome"#global variable
#
#
#def hello():
#    global s
#    print(s)
#    s = "Good Morning" #local variable
#    print(s)
#
#
#
#hello()
#print(s)
def outer():
    global x
    x = 5 #local variable
    def inner(x):
#        nonlocal x
#        x = 10
        print(x)
    inner(6)
    print(x)
x = 2
outer(111)
print(x)