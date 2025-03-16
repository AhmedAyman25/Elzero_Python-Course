# height = [1.80, 1.75, 1.70, 1.65, 1.60]
# weight = [80, 70, 65, 55, 50]


# x = [1, 2, 3, 4, 5]
# print(all(x))
# print(any(x))
# print(dir())
# print(divmod(10,3))
# first = [11.25, 18.0, 20.0]
# second = [10.75, 9.50]
# first.append(100)
# first.remove(18.0)
# print(first)
# first.reverse()
# print(first)
myString = 'hello i am ahmed'
print(myString.title())
print(myString.capitalize())

x,y,z = '1','11','111'
print(x.zfill(4))
print(y.zfill(4))
print(z.zfill(4))

print(myString.upper())
print(myString.count('e'))

str = "ILovePython25"
print(str.isalnum())

money = 500165968123
print("Money in the bank: {:,.2f}".format(money))
myList = [1,2,8,9,5,6,3]
print(myList)
a =myList
a.append(150)
print(myList)
a.pop()
print(myList)
a.pop()
print(myList)
print('*'*30)
ls = [50,60,70]
m,n,o  = ls
print(m)
print(n)
print(o)
print('*'*30)
mySet = {2,4,2,8,6,5,4,8,9,10}
print(len(mySet)) #7
mySet.add(7)
print(mySet)
#mySet.remove(80) #error because 80 not in the set
print(mySet)
mySet.discard(80) #looks like remove but no error
print(mySet)

mySet2 = {'A','B','C','D'}
mySet.update(mySet2) # update = union -> looks like add but add multiple values
print(mySet)
mySet.union(mySet2)
print(mySet)
##############################################################
set1 = {1,2,3,4,5,"Ahmed",'X',True}
set2 = {'X',1,2,False,'Omar'}
# difference() (set1 - set2) -> return a set that contains the difference between two sets
print(set1.difference(set2)) # {3, 4, 5, 'Ahmed'}

#difference_update() (set1 - set2) -> remove the items that exist in both sets (update the original set)
# set1.difference_update(set2)
# print(set1) # {3, 4, 5, 'Ahmed'}

#intersection() (set1 & set2) -> return a set that contains the intersection between two sets
print(set1.intersection(set2)) # {1, 2, 'X'}
#intersection_update() (set1 & set2) -> update the original set with the intersection between two sets
# set1.intersection_update(set2)
# print(set1) # {1, 2, 'X'}

#semmetric_difference() (set1 ^ set2) -> return a set that contains the symmetric difference between two sets (items that exist in one set but not in both)
print(set1.symmetric_difference(set2)) # {3, 4, 5, 'Ahmed', False, 'Omar'}
#symmetric_difference_update() (set1 ^ set2) -> update the original set with the symmetric difference between two sets
# set1.symmetric_difference_update(set2)
# print(set1) # {3, 4, 5, 'Ahmed', False, 'Omar'}

#union() (set1 | set2) -> return a set that contains the union between two sets
print(set1.union(set2)) # {1, 2, 3, 4, 5, 'Ahmed', 'Omar', 'X', False}

print('=' * 30)
print('yes') if 10 > 5 else print('no')
print("Hi" if 10 < 5 else "Bye")
print('=' * 30)
mySkills = {
    "Html":"90%",
    "PHP":"80%",
    "JS":"70%",
    "Css":"60%",
    "Python":"75%",
}

for skill in mySkills:
    print(f"my progress in Lang {skill} is: {mySkills[skill]}")
print('='*30)

for key,value in mySkills.items():
    print(f"{key} => {value}")

print('='*30)
peoples  = {
    "Ahmed" :{
        "html":"80%",
        "css":"90%",
        "js":"70%",
        "php":"60%",
    },

    "Omar" :{
        "html":"60%",
        "css":"70%",
        "js":"90%",
        "php":"80%",
    },
    "Ali" :{
        "html":"70%",
        "css":"60%",
        "js":"80%",
        "php":"90%",
    }
}   

for name in peoples:
    print(name)
    for skill in peoples[name]:
        print(skill, " -> ",peoples[name][skill])

print('='*30)
for pepoles_Key, peoples_value in peoples.items():
    print(f"{pepoles_Key} progress is: ")
    for lang_key, lang_value in peoples_value.items():
        print(f"{lang_key} => {lang_value}")
print('='*30)

def show_datails(* skills):
    print("Your Skills are : ")
    for skill in skills:
        print(skill)

show_datails("Html","js","algorithms")

print('*'*30)
# Recursion
def cleanWord(word): #AAhmmmeeeddd
    if len(word) == 1:
        return word
    
    if word[0] == word[1]:
        return cleanWord(word[1:])
    return word[0] + cleanWord(word[1:])
    

print(cleanWord("AAhmmmeeeddd"))

####################################################
### lambda Function = Anonymous function
### lambda type is function
### Syntax -> [Keyword lambda] [variables_names] [:] [block of code]

hi = lambda name : f"Hi {name}"
print(hi("Ahmed"))
print(type(hi)) 

print('*'*30)

#-----------------------------
#----- Iterable vs Iterator
#-----------------------------
# Iterable -> is an object that contains a collection of items (list, tuple, set, dictionary, String)
# Iterator -> is an object that represent a stream of data
# iterator -> object used to iterate over iterable objects like lists, tuples, sets, and dictionaries using the iter() and next() functions
# iter() -> return an iterator object
# next() -> return the next item in the iterable object
# StopIteration -> raised when the next() function reaches the end of the iterable object
# you can generate an iterator from an iterable object using the iter() function

myList = [1,2,3,4,5]
myIter = iter(myList)
print(next(myIter)) #1
print(next(myIter)) #2

print('*'*30)

#------------------- For loop generate an iterator automatically -------------------
for letter in "Ahmed":
    print(letter)

print('*'*30)

for letter in iter("Ahmed"):
    print(letter)
#------------------------------------------------------------------------------------
print('*'*30)
frozenSet = frozenset('aabbss')
print(type(frozenSet))

def Fun():
    ''' this is the describtion of the function'''
    pass

print(Fun.__doc__)
help(Fun)
print('*'*30)



