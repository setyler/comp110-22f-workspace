"""Demonstrating capabilities of dictionaries."""

# type declaration 
schools: dict[str, int]

# initialize to an empty dictionary
schools = dict()

# set a key-value pairing in the dictionary 
schools["UNC"] = 19_400
schools["duke"] = 6_717
schools["NCSU"] = 26_150

# print dictionary literal representation 
print(schools)

# access a value by its key 
print(f"UNC has {schools['UNC']} students.")

# remove a key-value pair from a dictionary by its key 
schools.pop("duke")

# test for existence of key 
if "Duke" in schools:
    print("Found key 'duke' in schools.")
else:
    print("No key 'duke' found in schools")

# update/reassign key-value pair
schools["UNC"] = 20_000
schools["NCSU"] += 200 

for key in schools:
    print(f"Key: {key} -> Value: {schools[key]}")

