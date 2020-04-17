# The list class provides mutable sequence of elements
empty_list = list()
print('empty_list ->', empty_list)
list_str = list('hello')
print('list_str-->', list_str)
list_tup = list((1, 2, (3, 5, 7)))
print('list_tup->', list_tup)
list_syn = [3, 4, 'a', 'b']
print('list_syn->', list_syn)
print("'a' in list syn->", 'a' in list_syn)
print("1 not in list_syn", 1 not in list_syn)
empty_list = []
print('empty_list->', empty_list)
empty_list.append(5)
print('empty_list->', empty_list)
empty_list.append([6, 7])
print('empty_list->', empty_list)
last_elem = empty_list.pop()
print('last_elem ->', last_elem)
print('empty_list ->', empty_list)
empty_list.extend([6, 7])
print('empty_list ->', empty_list)
first_elem = empty_list.pop(0)
print('first_element = ', first_elem)
print('empty_list = ', empty_list)
empty_list.insert(0, 10)
print('empty_list = ', empty_list)
empty_list.remove(7)
print('empty_list = ', empty_list)
empty_list.clear()
print('empty_list = ', empty_list)
avg = 68.3
if avg >= 90:
    print('Distinct')
elif avg in range(60, 90):
    print('Above Average')
else:
    print('Fail')
# checking the build iin jenkins
