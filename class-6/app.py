<<<<<<< HEAD
# name = ["wasay", "fahad"]
# nested_list = [["a", "b", "c"], [1,2,3]]
# # name.remove("wasay")
# # name.insert(1,"fahad")
# # name.pop()
# # name.append("fahad")
# print(name)
# print(nested_list[0][0]) #output a
# print(nested_list[1][0]) #output 1

# number_list = [3, 5, 1]

# print(number_list[-1]) #output 1
# number_list.reverse()
# print(number_list)

# integer = [4, 5, 6, "wasay", "wasay"]

# integer.extend([1, 2, 8]) #add at the end of the list
# print(integer)
# print(integer.count("wasay")) #wasay is repeat 2 times in list

# new_interger = integer.copy() #copy merthod copy all the item in the lsit
# print(new_interger)

# print(new_interger.clear()) #Removes all elements from the list.
# print(new_interger)

# number_new_list = [4, 5, 7, 10, 15]
# print(max(number_new_list)) #Returns the largest item in the list.
# print(min(number_new_list)) #Returns the smallest item in the list.
# print(sum(number_new_list)) #Returns the sum of all elements in the list.

# let = [1,1, 1]
# print(any(let)) #Returns True if any element in the list is True.
# print(all(let)) #Returns True if all elements in the list are True.

# lst = [1, 2, 3, 4]
# del lst[1]
# print(lst)  # Output: [1, 3, 4]

# del lst[:2]  # Deletes first two items
# print(lst)  # Output: [4]

# string = "hello"
# lst = list(string)
# print(lst)  # Output: ['h', 'e', 'l', 'l', 'o']

# lists = ["orange", "banana", "grape", "apple"]
# print(len(lists))
# print(len(lists[2]))
# print(lists[0:1]) #start from orange and end at banana but does not print banana
# print(lists[1:3].pop())
# print(lists[:1])
# print(lists[1:])
# print(lists[1],[31])



# new = ["orange", "banana", "grape", "apple","cherry", "pineapple","papaya","lime"]
# # half_list = len(new) // 2
# # print(new[0: half_list])

# print(new[1:4:2])


# to add nested list do this
# appen1 = [1,2,3,4,5,6]

# append2 = [7,8,9]


# appen1.append(append2)
# print(appen1)

vegatable = ["ladyfinger", "Capsicam", "carraot", "Potatao", "Ginger", "Tomato"]

lenght = len(vegatable) // 2
vegatable.insert(lenght, "wasay")
print(vegatable)

save = vegatable.pop()
print(save)

new_save = ["1","2","3", save]
new_save.insert(1,save)
new_save.remove("Tomato")
print(new_save)
# print(dir(list))

quiz = ["aloo", "bhendi", "marchi", "non"]

new_quiz = quiz.remove("aloo")
print(new_quiz)

print(quiz)

fruits = ["apple", "bananan", "cherry"]
frruits_2 = fruits
frruits_2.append("mango")
print(fruits[-1], frruits_2)

varss = frruits_2.copy()
=======
# name = ["wasay", "fahad"]
# nested_list = [["a", "b", "c"], [1,2,3]]
# # name.remove("wasay")
# # name.insert(1,"fahad")
# # name.pop()
# # name.append("fahad")
# print(name)
# print(nested_list[0][0]) #output a
# print(nested_list[1][0]) #output 1

# number_list = [3, 5, 1]

# print(number_list[-1]) #output 1
# number_list.reverse()
# print(number_list)

# integer = [4, 5, 6, "wasay", "wasay"]

# integer.extend([1, 2, 8]) #add at the end of the list
# print(integer)
# print(integer.count("wasay")) #wasay is repeat 2 times in list

# new_interger = integer.copy() #copy merthod copy all the item in the lsit
# print(new_interger)

# print(new_interger.clear()) #Removes all elements from the list.
# print(new_interger)

# number_new_list = [4, 5, 7, 10, 15]
# print(max(number_new_list)) #Returns the largest item in the list.
# print(min(number_new_list)) #Returns the smallest item in the list.
# print(sum(number_new_list)) #Returns the sum of all elements in the list.

# let = [1,1, 1]
# print(any(let)) #Returns True if any element in the list is True.
# print(all(let)) #Returns True if all elements in the list are True.

# lst = [1, 2, 3, 4]
# del lst[1]
# print(lst)  # Output: [1, 3, 4]

# del lst[:2]  # Deletes first two items
# print(lst)  # Output: [4]

# string = "hello"
# lst = list(string)
# print(lst)  # Output: ['h', 'e', 'l', 'l', 'o']

# lists = ["orange", "banana", "grape", "apple"]
# print(len(lists))
# print(len(lists[2]))
# print(lists[0:1]) #start from orange and end at banana but does not print banana
# print(lists[1:3].pop())
# print(lists[:1])
# print(lists[1:])
# print(lists[1],[31])



# new = ["orange", "banana", "grape", "apple","cherry", "pineapple","papaya","lime"]
# # half_list = len(new) // 2
# # print(new[0: half_list])

# print(new[1:4:2])


# to add nested list do this
# appen1 = [1,2,3,4,5,6]

# append2 = [7,8,9]


# appen1.append(append2)
# print(appen1)

vegatable = ["ladyfinger", "Capsicam", "carraot", "Potatao", "Ginger", "Tomato"]

lenght = len(vegatable) // 2
vegatable.insert(lenght, "wasay")
print(vegatable)

save = vegatable.pop()
print(save)

new_save = ["1","2","3", save]
new_save.insert(1,save)
new_save.remove("Tomato")
print(new_save)
# print(dir(list))

quiz = ["aloo", "bhendi", "marchi", "non"]

new_quiz = quiz.remove("aloo")
print(new_quiz)

print(quiz)

fruits = ["apple", "bananan", "cherry"]
frruits_2 = fruits
frruits_2.append("mango")
print(fruits[-1], frruits_2)

varss = frruits_2.copy()
>>>>>>> 6c7156682b4a50692bac421b13d9626c1a0c0b8e
print(varss)