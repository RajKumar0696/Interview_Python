# 44. Write a Python program to print the index of a character in a string.
# Sample string: w3resource
# Expected output:
# Current character w position at 0
# Current character 3 position at 1
# Current character r position at 2


string = "w3school"
for i in range(len(string)):
    print("Current character", string[i], "position at", i)
