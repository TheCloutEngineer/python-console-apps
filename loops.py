#
#
# list1 = ["red", "green", "blue", "orange", "purple"]
#
# for i in range(len(list1)):
#     print(list1[i])
#
# # for i in range(3, 10):
# #     print(i)
#
# numbers = [1, 2, 3, 4, 5, 6, 7]
#

dict1 = {
            'value': 11
        }

dict2 = dict1

print("Before value is updated")
print("dict = ", dict1)
print("dict2 = ", dict2)

print("\ndict points to:", id(dict1))
print("\ndict2 points to:", id(dict2))

dict2['value'] = 22

print("\nAfter value is updated")
print("dict = ", dict1)
print("dict2 = ", dict2)

print("\ndict points to:", id(dict1))
print("\ndict2 points to:", id(dict2))