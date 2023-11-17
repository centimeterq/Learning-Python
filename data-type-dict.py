# example dict

dicts = {
    "name" : "Miko Meysa Bima",
    "age" : 18
}

# access item dict, you can use variabel[name of key]

name = dicts["name"] # output Miko Meysa Bima
print("access name of dict : ", name)

# add item you can use variabel[new key] = value

dicts["language"] = "indonesia" # output {'name': 'Miko Meysa Bima', 'age': 18, 'language': 'indonesia'}

print("after add item :", dicts)

# change item you can use variabel[keyname want change] = new value

dicts["name"] = "Levi Ackerman"

print("new value on name : ", dicts["name"])

# if you want remove a item in dict you can use del variabel["name keys"]

del dicts["age"]

print("after delete : ", dicts)

# nested dict example

sirkel_ngawi = {
    "fuad" : {
        "name" : "Mas Fuad",
        "age" : 24,
        "born_place" : "Ngawi"
    },
    "rusdi" : {
        "name" : "Mas Rusdi",
        "age" : 23,
        "born_place" : "Ngawi"
    }
}

# if you want access item, you can use variabel[key][key]

print(sirkel_ngawi["fuad"]["name"]) # output Mas Fuad
