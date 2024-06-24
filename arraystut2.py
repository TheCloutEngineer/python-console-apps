# import array as arr
# #
# # # Time Complexity O(1)
# # # Auxiliary Space O(n)
# #
# # a = arr.array('i', [1, 2, 3, 4, 5])
# # print("The newly created array is : ", end=" ")
# # for i in range(0, 5):
# #     print(a[i], end=" ")
# # print()
# #
# # b = arr.array('d', [1.1, 2.2, 3.3, 4.4, 5.5, 6.6])
# # print("\nThe new created array is : ", end=" ")
# # for i in range(0, 6):
# #     print(b[i], end=" ")
# # print()
# # c = arr.array('i', [1, 2, 3])
# #
# # # Time Complexity: O(1): for inserting elements at the end;
# # # O(n): for inserting elements at the beginning and to full arr
# # # Auxiliary Space: O(1)
# #
# # print("\nArray before insertion : ", end=" ")
# # for i in range(0, 3):
# #     print(a[i], end=" ")
# # print()
# # c.insert(1, 4)
# # print("Array after insertion : ", end=" ")
# # for i in c:
# #     print(i, end=" ")
# # print()
# # d = arr.array('d', [1.1, 2.2, 3.3, 4.4, 5.5])
# # print("Array after insertion : ", end=" ")
# # for i in range(0, 5):
# #     print(d[i], end=" ")
# # print()
# # d.append(4.4)
# # print("Array after insertion : ", end=" ")
# # for i in d:
# #     print(i, end=" ")
# # print()
# #
# #
# # AP = arr.array('i', [1, 2, 3, 4, 5, 6, 7])
# #
# # for i in AP:
# #     print("\n", i, end=" ")
# # print()
# #
# # print(AP[0])
# # print(AP[1])
# # print(AP[4])
# #
# from array import array
#
# arr = array('i', [1, 2, 3, 4, 5, 6])
#
# print(arr)
#
# print(arr.buffer_info())
#
# print(arr[2])
#
# for i in arr:
#     print(i)
#
# for i in range(5):
#     print(i)
#
# for pnt in range(1, 4):
#     print(pnt, arr[pnt])
#
# arr.reverse()
# print(arr)
#
# arr.append(2)
# print(arr)
#
# arr.remove(2)
#
# print(arr)
#
# arr = array('i', [-1, 2, 2, 3, 4, 5])
# print(arr[3])
# print(arr.index(2))
#
# arr = array('i', [])
# x = int(input("Enter size of array"))
# print("enter %d element" % x)
# for i in range(x):
#     n = int(input())
#     arr.append(n)
# print(arr)
#
# i = 0
# while i < x - 1:
#     j = i + 1
#     while j < x:
#         if arr[i] == arr[j]:
#             del arr[j]
#             x = x - 1
#         j += 1
#     i += 1
# print(
# type(765),
# type(2.718),
# type('2 pi'),
# type(abs(7)),
# type(abs(-7.0)),
# type(abs(1)),
# type(int),
# type(type)
# )


import datetime

minute_timedelta = datetime.timedelta(minutes=42)

seconds_in_a_minute = minute_timedelta.total_seconds()

print(seconds_in_a_minute + datetime.timedelta(seconds=42).total_seconds())


def kilometers_to_miles(kilometers):
    km_to_miles_factor = 0.621371

    miles = kilometers * km_to_miles_factor
    return miles


print(kilometers_to_miles(10))

