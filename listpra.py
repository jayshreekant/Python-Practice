
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

list3 = [3,22,55,21,112,1,2,89,4,7,545,4,45,5]
print(list3)
list3.sort()
print(list3)
print(list3.sort())
list3.sort(reverse=True)
print(list3)
list3.sort()
print(list3)
# print(sorted(list3))