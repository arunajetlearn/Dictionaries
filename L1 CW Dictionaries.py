#Create a dictionary
D = {
  "name": "Pulkit",
  "age": 23,
  "city": "Agra",
}

# Accessing values in a dictionary
print(D["name"])
print(D)

# Create a list with the same information to show the difference between list and a dictionary
L = ["Pulkit", 23, "Agra"]
print(L[0])

# Get the list of keys
print(D.keys())

# Get the list of values
print(D.values())

# Get the list of keys and values
for i in D.keys():
	print(i, D[i])
	
# Check if the key exists in the dictionary or not
a=input("Enter the key to be checked: ")
if a in D:
	print("key exist")
else:
	print("key does not exist")
	
# Add a key-value pair to the dictionary
D["Profession"] = "Software Engineer"
print(D)

# Delete a key-value pair
del(D["Profession"])
print(D)

# Change a value in the dictionary
D["city"] = "Bangalore"
print(D)

# Store a list as a value in the dictionary
D["marks"] = [99,87, 85, 92, 90]
print(D)

# Access a value in the list stored in the dictionary
print(D["marks"][1])

# Create a nested dictionary
classroom = {
  "PulkitChawla" : {"age": 23,"marks": [89, 85, 90, 86, 90]},
  "Kanishk": {"age": 13,"marks": [90, 95, 85, 87, 80] }
}


# Go through basic dictionary operations for nested dictionary
print(classroom.keys())
print(classroom.values())

for i in classroom.keys():
	print(classroom[i])

classroom["PulkitChawla"]["age"] = 30
print(classroom.values())