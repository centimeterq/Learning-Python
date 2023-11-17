# example sets

sets = {"banana", "apple", 1922, 1903, True, False}

# access item on sets, you can use for loop

for item in sets :
    print(item) # output item on sets

# if you wanna check item you can use

print("banana" in sets) # output True

# if you want add a item on sets you can use add method

sets.add("cherry") # its will add item on sets

print("sets after add item : ", sets)

# if you want add list / another set to set you can use update methos

list = ["durian", "pineapple"]

sets.update(list) # output {"banana", "apple", 1922, 1903, True, False, "durian", "pineapple"}

print("after add list : ", sets)

# if you want remove item on set you cant use a remove or discard method

sets.remove(1903) # its will remove 1903 item

sets.discard("banana")

print("after remove : ", sets)

# if you want remove all item on sets you cant use clear method

# comment
# sets.clear()

print("remove all method : ", sets)

# if you want search item same on 2 tuples you can use method intersection_update

sets2 = {"blueberry", "alcohol", 1922}

sets.intersection_update(sets2)

print(sets) # output 1922

# if you want item not same on 2 sets you can use difference_update

sets.difference_update(sets2) # output {False, True, 'durian', 'cherry', 'pineapple', 'apple'}

print(sets) # output {False, True, 'durian', 'cherry', 'pineapple', 'apple'}
