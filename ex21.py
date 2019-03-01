def add(a, b):
    print(f"Adding {a} and {b}")
    return a + b

def subtract(a, b):
    print(f"Subtracting {b} from {a}")
    return a - b

def multiply(a, b):
    print(f"Multiplying {a} and {b}")
    return a * b

def divide(a, b):
    print(f"Dividing {a} by {b}")
    return a / b

age = add(18, 7)
height = subtract(200, 19)
weight = multiply(30, 3)
iq = divide(1000, 5)

# print(f"Age: {age}\nHeight: {height}\nWeight: {weight}\nIQ: {iq}")

what = add(age, subtract(height,multiply(weight,divide(iq,2))))

# print (what)

a = 120 * 123 - 233 + 231 / 23

function_a = add(subtract(multiply(120,123), 233), divide(231, 23))

print(a)
print(function_a)
