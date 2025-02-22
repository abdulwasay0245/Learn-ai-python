# hello = "Kusah Amdid"
# print(f'{hello:_>20}')

user1 = {
    "name": "Fahad",
    "age": 18,
    "address": {
        "city": "Karachi",
        "state": "Sindh",
        "street": "Gilanabad Housing Society",
        "country": "Pakistan"
    },
    "skills" : ["Python", "Django", "Flask", "Javascript", "React"]

}
for user in user1:
    print(user["skills"])

# print(user1["address"]["city"])

#1
# clear_data = user1.clear()
# print(clear_data)

#2
# print(user1.keys())

# #3
# print(user1.values())

# #4
# popdata = user1.pop("age")
# print(popdata)

# #5
# popitems = user1.popitem()
# print(popitems)
# print(user1)

# #6
# update_data = {"Planet": "Earth"}
# user1.update(update_data)
# print(user1)


# user1["city"] = "Moscow"
# user1["address"]["city"] = "Edinburgh"

# print(user1["city"])
# user1["address"]["city"]
# print(user1["address"])

# del user1 del Keyword is use to delete the dictionary or var or key or value

