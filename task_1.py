# methods for a list
# List with numbers from 1 to 10
_list = list(range(134, 234))
# 1. count
print(_list.count(1))  # 0
# 2. remove
_list.remove(1)  # in this case we don't have a element removed -ValueError
print(_list)
# 3. index
print(_list.index(1))  # in this case doesn't exist the element 1 -ValueError
# 4. copy
_list2 = _list.copy()  # create a new instance with the values of the list
print(_list2)
# 5. reverse
_list.reverse()  # change the order of the elements in the list from the last item to the first item
print(_list)
# 6. sort
_list.sort()  # in this case return none because the list is in order
print(_list)
# 7. max
print(max(_list))  # return 234
# 8. min
print(min(_list))  # return 134
