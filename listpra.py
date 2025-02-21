
list1 = [i for i in range(50)]
print(list1)
list1.append(50)
print(list1)
# list1.clear()
# print(">>",len(list1),list1)
list1.remove(50)
print(list1)
print(list1.count(4))

list2 = [i for i in range(50) if i%4 ==0]
print(list2)