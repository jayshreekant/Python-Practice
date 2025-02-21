print("Hello")
jlist = [12,23,34,546,78,64,"Ram", True, False ]
# print(type(jlist))
# print(jlist[-8])
# print("hfskhfjk ",len(jlist)-8)
# print(jlist[len(jlist)-8])


jlist2 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]

# for num in jlist2:
#     print(num)
"""Second Item will be - 1 always 
    Index will be starting from Zero
    Jump Index will have regular counting"""
print(len(jlist2))
print(jlist2[1:])
print(jlist2[1:4])
print(jlist2[1:-1])
print(jlist2[1:len(jlist2)-1])  


"""Jump Index"""
print(jlist2[0:26:4])


def add(a=4,b=5):
    print(a+b)

add(4,4)
add()
add(-4,-4)
add(-4)
add(4/4)