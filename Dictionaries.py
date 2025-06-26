customer = {   # {} defines a dictionary / dictionaries are case-sensitive
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}


customer["name"] = "Jack Smith"
print(customer["name"])    # use [] to use a 'key'

customer["email"] = "abc@gmail.com" # you can add a new key and value in the dictionary

print(customer.get("birthdate"))       # you can use .get() method, which gives 'none' when there is no key in the dictionary

print(customer.get("birthdate", "Jan 1 1980")) # Default 'birthdate', which doesn't exist in dictionary, to Jan 1 1980