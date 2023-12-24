#Exeption Handling :
#x = [5]
#
#try:
#   x.append("3")#AttributeError
#   print(x)
#    
#except Exception:
#     print("X is a integer")   
a = int(input("Enter a number"))
try:
    if (3+4-a)>0:
        print(a/0)#ZeroDivisionError
    else:
        print("Hello"+4)#TypeError
except ZeroDivisionError:
    print(a/5)
except TypeError:
   print("Hello"+str(4))
except Exception:
    print("Error occured")
finally:
    print("Bye")
#except (TypeError,AttributeError,ZeroDivisionError) as e:
#    print("Error Occured",e)
#x =int(input("enter a number:"))
#if x < 0:
#    raise Exception("No negative number allowed")
#else:
#    print(x)
#finally: