def print_two(*args):
    arg1, arg2, arg3 = args
    print (f"arg1 {arg1} arg2 {arg2} arg3 {arg3}")

def print_none():
    print ("No args")
print_two (123,123, "third")
print_none()
