#Reverse a string using a loop.

text = input("Enter a string: ")
result = ""
for i in text:
    result = i + result
print("Reversed string is:", result)
