my_dict = {'C1': [1, 2, 3], 'C2': [5, 6, 7], 'C3': [9, 10, 11]}

# C1 C2 C3
# 1 5 9
# 2 6 10
# 3 7 11

for i in my_dict:
    print(i, end=" ")
for j in my_dict['C1']:
    print(j, "\r")
