'''
Created on Feb 12, 2019

@author: Dylan
'''

x_list = ["Apple", 27, 5637, "Toucan", "okay?"]
x_list.append(2232)
list.append(x_list, "Avocado")
print(x_list)

print(x_list[1])

'''Python lists'''
a = ["Retention", 3, None]
b = ["Retention", 3, None]


'''comparing lists with is results in a boolean value, but should not be used for comparing ints, strs,and most other data types'''
print(a is b)


'''comparing lists with = results in a boolean value'''
b=a
print(a is b)

'''Comparing values with null 'None' values'''
c = "Something"
d = None
print(c is not None, d is None)


e = 2
f = 6
print(e==f)
print(e>f)

