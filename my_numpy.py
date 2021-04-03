import numpy as np

print("NumPy (Numerical Python): v" + str(np.__version__))
arr = [1, 2, 3, 4, 5]
arr1D = np.array(arr)  # a list, tuple or any array-like object
print(str(arr1D) + " is a " + str(type(arr1D)))
arr0D = np.array(6)
arr2D = np.array([[1, 2, 3], [4, 5, 6]])
# This is also a matrix, NumPy has np.mat() for them.
arr3D = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
# An array of matrices
print(str(arr0D.ndim) + ", " + str(arr1D.ndim) + ", " + str(arr2D.ndim) + ", " + str(arr3D.ndim) + " Dimensions")
# There can be even more dimensions
arr5D = np.array([1, 2, 3, 4], ndmin=5)
print(arr5D)
print('Number of Dimensions :', arr5D.ndim, "Forth First:", arr5D[0][0][0][0])
# Another method for indexing
print("Second element in first dimension of the 2D array:", arr2D[0, 1])
print("Third element of the second array of the first array of the 3D array:", arr3D[0, 1, 2])
print('Last element from 2nd dim of the 2D array:', arr2D[1, -1])
print()

# Fruits: Slicing, Data Types, Copy and View, Shape and Reshape, and Iteration
fruits1 = np.array([["apple", "pear", "lemon"], ["watermelonn", "melon", "cantaloupe"],
                    ["potato", "tomato", "onion"]], dtype="U10")
# Data types in a normal Python list are not required to be the same, but in NumPy it's required.
myFruits = np.concatenate((fruits1[::2, -2], fruits1[1, 0:3:2]))
print("My Fruits:", myFruits, "(", np.array(myFruits).dtype, ")")
print(myFruits.astype('S'))
print(np.array([-10, 0, 2]).astype(bool))
copiable = fruits1[2, :].copy()
viewable = copiable.view()
print(copiable.base, viewable.base)
# astype() => a copy; reshape() => a view.
print("Shapes:", fruits1.shape, "arr5D: ", arr5D.shape)
arr = list(fruits1)
arr.append(list(fruits1[0]))
fruits2 = np.array(arr).reshape(6, -1)  # Unknown Dimension: 2
print(fruits2)
fruits3 = fruits2.reshape(-1)  # Flatten
for f in fruits3:
    pass
for i in np.nditer(fruits3[::4]):
    print(i)
for i in np.nditer(np.array([1, 2, 3]), flags=['buffered'], op_dtypes=['S']):
    print(i)
for idx, x in np.ndenumerate(fruits3[::4]):  # The same thing, but with indices
    print(idx, x)
print()

# Fruits: Joining and Stacking, and Splitting
fruits4 = np.array((("orange", "tangerine"), ("orange", "tangerine")))
fruits5 = np.array((("grape", "pomegranate"), ("grape", "pomegranate")))
# Axis is a cross-like change between elements of dimensions
print(">> Concatenation (Axis=1):")
fruits6 = np.concatenate((fruits4, fruits5), axis=1)  # axis=0 by default; axis < n-D
print(fruits6)
print(">> Stacking (Axis=1):")
# Stacking is same as concatenation, the only difference is that stacking is done along a new axis.
fruits7 = np.stack((fruits4, fruits5), axis=1)  # axis=0 by default; axis < n-D - 1
print(fruits7)
print(">> Stacking Along Rows:")
fruits8 = np.hstack((fruits4, fruits5))  # no "axis" allowed
print(fruits8)
print(">> Stacking Along Columns:")
fruits9 = np.vstack((fruits4, fruits5))  # no "axis" allowed
print(fruits9)
print(">> Stacking Along Height (depth):")
fruits10 = np.dstack((fruits4, fruits5))  # no "axis" allowed
print(fruits10)
print(">> Splitting (!= Indexing):")
fruits8.reshape(-1)
splitted1 = np.array_split(fruits8, 3)
print(splitted1[0])
# We also have the method split() available but it will not adjust the
# elements when elements are less in source array for splitting.
splitted2 = np.split(fruits8, 2)  # "3" raises ValueError
print(splitted2[0])
splitted3 = np.array_split(fruits8, 3, axis=1)
print(splitted3)
print(">> Splitting Along Rows, Columns and Height:")
splitted4 = np.hsplit(fruits8, 2)  # no "axis" allowed; "3" raises ValueError
print(splitted4)
splitted5 = np.vsplit(fruits8, 1)
print(splitted5)
splitted6 = np.dsplit(fruits7, 2)  # Watch, it's "fruits7"; only 3D arrays allowed here
print(splitted6)
print()

# Searching, Sorting and Filtering
arr = np.array([1, 2, 3, 4, 5, 4, 4])
print("Find \"4\":", np.where(arr == 4))
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print("Find Even Numbers:", np.where(arr % 2 == 0))
print("Find Odd Numbers:", np.where(arr % 2 != 0))
# searchsorted(): where the specified value would be inserted to maintain the search order.
print("Search Sorted:", np.searchsorted(arr, 2.5), " - ", np.searchsorted(arr, 2))
print("Search Sorted From Right Side:", np.searchsorted(arr, 2, side='right'))
print("Search Sorted Multiple:", np.searchsorted(arr, [2, 4, 6]))
theSorted = np.sort(myFruits)  # sort() => a copy
print("Sort:", theSorted)
print("Sort Booleans:", np.sort(np.array([True, False, True])))
print("Sort 2D Array:", np.sort(np.array([[3, 2, 4], [5, 0, 1]])))
# Filtering: getting some elements out of an existing array and creating a new array out of them.
print("Filtered the bigger fruits:", theSorted[[True, False, False, True]])
print("Filtered using the array itself:", arr[arr > 4])
print("Filtered the even numbers:", arr[arr % 2 == 0])
print()

from numpy import random

# Random
print("Random Integer:", random.randint(100))  # 1arg -> max; 2arg -> min, max
randArr = random.randint(95, 100, size=5)
print("Random Array:", randArr, type(randArr))
print("Random 2D Array:", random.randint(100, size=(3, 5)))
print("Random Float:", random.rand())  # A single float number
print("Random Float Array:", random.rand(5))
print("Random Float 2D Array:", random.rand(2, 3))
choices = ["Elizabeth", "William", "Olivier", "Amir Ali", "Jun", "Braydan", "Florian", "Dominik"]
print("Random Choice:", random.choice(choices))
print("Random Choice:", random.choice(choices, size=(1, 4)))
print()

# ufuncs (Universal Functions)
x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
# z = []
# for i, j in zip(x, y): z.append(i + j)
# print(z)
# INSTEAD:
print("ufuncs Add:", np.add(x, y))
