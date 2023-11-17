# example list

lists = ["eren", "armin", "mikasa", "historia"]

# access item on list, you can use index eg : variable[index]

print("access item on list : " + lists[2]) # output mikasa

# you can acccess mutiple item with variabel[index:index]

print("access mutiple item :" , lists[1:3]) # output ["armin", "mikasa"]

# change item on list, you can use variabel[index want you change] = new value

lists[1] = "petra"

print("change value armin to petra : " , lists)

# add item you can use append method eg : variabel.append(new value)

# it will add item on back list
lists.append("pieck")

print("add item on back list " ,lists) # output ["eren", "armin", "mikasa", "historia", "pieck"]

# if use want add item on index spesific you can use insert method
# example i want insert item on thirdty position you can

lists.insert(2, "jean") # output ["eren", "armin", "jean", "mikasa", "historia", "pieck"]

print("insert item on spesific position : ", lists)

# combine 2 list, you can combine 2 list using extend method eg :

lists2 = ["reiner", "annie", "zeke", "gabi"]
lists.extend(lists2)

print("result combine 2 list : ", lists) # output ['eren', 'petra', 'jean', 'mikasa', 'historia', 'pieck', 'reiner', 'annie', 'zeke', 'gabi']

# remove item on list, you can use methos remove on list eg : variabel.remove(index)

lists.remove("eren") # output ["mikasa", "historia"]

print("item after remove : ", lists)

# check item on list
if "mikasa" in lists:
    print("mikasa i love you")
