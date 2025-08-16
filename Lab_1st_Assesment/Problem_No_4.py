'''
  Check Uppercase or Lowercase
 Take a character input and check if it is uppercase or lowercase.
'''



ch = input("Enter a character: ")
if ch.isupper():
    print("Uppercase letter")
elif ch.islower():
    print("Lowercase letter")
else:
    print("Not a letter")
