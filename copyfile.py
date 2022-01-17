
exist_name = input("\nEnter the name of the file you want to copy: ")
new_name = input("\nEnter the name of the file you want to create: ")

exist_file= open(exist_name, 'r')       # open the existing file for reading
content = exist_file.read()             # read contents of existing file 
new_file = open(new_name, 'w')          # create and open the new file for writting 
new_file.write(content)                 # write the conent to the new file 

# close both files 
new_file.close() 
exist_file.close()