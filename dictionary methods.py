myDict = {
    "fast": "In a Quick Manner",
    "harsh": "A pilot",
    "marks": [1, 2, 5],
    "anotherdict": {'harsh': 'pilot'},
    1: 2
}

# Dictionary Methods
print(list(myDict.keys())) # Prints the keys of the dictionary
print(myDict.values()) # Prints the keys of the dictionary 
print(myDict.items()) # Prints the (key, value) for all contents of the dictionary 
print(myDict)
updateDict = {
    "yash": "pilot Friend",
    "nabhan": "pilot Friend",
    "Shubham": "pilot Friend",
    "harsh": "A pilot"
}
myDict.update(updateDict) # Updates the dictionary by adding key-value pairs from updateDict
print(myDict)

print(myDict.get("harsh")) # Prints value associated with key "harsh"
print(myDict["harsh"]) # Prints value associated with key "harsh"

# The difference between .get and [] sytax in Dictionaries?
print(myDict.get("harsh2")) # Returns None as harsh2 is not present in the dictionary
print(myDict["harsh2"]) # throws an error as harsh2 is not present in the dictionary