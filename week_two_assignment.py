my_list = []
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

print("append:", my_list)
my_list.insert(1, 15)
print("insert:", my_list)
my_list.extend([50, 60, 70])
print("extend:", my_list)
my_list.pop()
print("pop:", my_list)

my_list.sort()
print("sort:", my_list)

index_30 = my_list.index(30)
print("index of 30:", index_30)