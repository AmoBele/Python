def greet(input):
    if "Hello" in input:
        return "Eyy, there"
    else:
        return "i am not sure if i understand what your saying"

x = input("Greet: ").capitalize()
results= greet(x)
print(results)
