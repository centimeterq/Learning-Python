# example tuples

tuples = ("eren", "mikasa", "historia")

# access item on tuples you can use index eg variabel[index]

print(tuples[1]) # output "mikasa"

# convert tuples to list you can use list function example list(tuples)

# !! warning if you want change a item, you must convert to list first
convert_to_list = list(tuples)

# add item on tuples you can use method extend, but you must convert first

convert_to_list.append("pieck") # output ["eren", "mikasa", "historia", "pieck"]

# remove

convert_to_list.remove("eren") # output ["mikasa", "historia", "pieck"]

# if you want convert to tuples again you can use tuple function

convert_to_tuple = tuple(convert_to_list) # output ("eren", "mikasa", "historia", "pieck")
