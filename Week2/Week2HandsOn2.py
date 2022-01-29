dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50, 6:60}
dic4 = {}

# write a python script to concatenate the following dictionaries into a new one
for x in (dic1, dic2, dic3): 
    dic4.update(x)
print(dic4)
print()

# Write a python script to check if a given key already exists
print(dic4.get(10, None))
print()


# Write a python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x * x)
n = 6
dic = {x:x * x for x in range (1, n + 1)}
print(dic)
print()
