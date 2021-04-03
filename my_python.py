from random import randint  # import random
import datetime
import math
import json
import re
import my_file as file

# Hello Python!
x, y = 1, 2
go = y > x
z1 = z2 = 'Number '
if go:
    x -= 1
    y -= 1
z2 = str(x + y)
print(z1 + z2 + "st:")


def my_fun():
    global x  # Not needed now; needed when wanna edit it.
    print(x)
    global z1, z2  # Now needed
    z2 = float(z2)
    print(true_type(x) + true_type(y) + true_type(z2) + true_type(go)[:-3])
    z1 = "Salary: "
    z2 *= 1000 * 10
    print(z1 + str(z2) + "$ P/M")


def true_type(typ, space=True):
    do_space = " - "
    if not space:
        do_space = ""
    return str(type(typ))[8:-2] + do_space


x = '''I AM \"MAHDI PARASTESH\", A SOFTWARE ENGINEER!'''
my_fun()
print()

algebra, scientific = 1j, 12e5
if true_type(algebra, False) == 'complex' and not (not (isinstance(scientific, float))):
    print(algebra * scientific)  # 1200000j


def to_12_hours(h24): return h24 % 12


print(str(to_12_hours(14) ** 2) + "(**) - " + str(12.2 // 4.1) + "(//)")
# ** => Math.pow() (Exponentiation)
# // => Floor Division
# Learn Bitwise Operators

obj1, obj2 = ["a", "b"], ["a", "b"]
print(str(obj1 is obj2) + " while " + str(obj1 == obj2) + " but " + str("c" in obj1))
# is -> is not
# in -> not in


# Collections
myList, myTuple = ["Iran", "Netherlands", "Germany", "France"], ("Turkey", "South Korea", "Japan", "Malaysia")
rand, randTuple = randint(0, 1), randint(0, 2)
if rand == 1:
    myList[0] = "Singapore"
elif randTuple == 2:
    myList[2] = "Deutschland"
else:
    myList[1] = "Nederland"
# myTuple[1] = "North Korea" -> IMPOSSIBLE
if randTuple == 0:
    myTuple = list(myTuple)
    myTuple[1] = "North Korea"
    myTuple = tuple(myTuple)
myList.sort()
myList.reverse()
myList.reverse()
print(myList[0] + " is in love with " + myTuple[-rand] + ", but " + str(myTuple[rand:-1])[1:-1] +
      " hate each other.")
oneItemTuple = ("South Korea",)  # A comma(,) is needed, otherwise it'll be recognised as a 'str'!
joined = myTuple + oneItemTuple
print(str(joined) + " [" + str(joined.count(oneItemTuple[0])) + " times, first in " +
      str(joined.index(oneItemTuple[0])) + " index]")
del myTuple  # Deleted completely, but deleting one of its items is impossible again!
myList.append("Russia")
myList.pop(len(myList) - 1)  # Added Russia but removed immediately.
myList.append("Russia")
myList.remove("Russia")  # The same
echo = str(myList)
print("DONE!") if rand == 1 else print(echo + " with Third changed!") if randTuple == 2 \
    else print(echo + " with Second changed!")
if 2 > 1: pass  # Empty IF statement

mySet, theirSet = set(), {"United States", "United Kingdom"}
# print(type({})) # <class 'dict'>
mySet.clear()
for i in myList: mySet.add(i)
if "Deutschland" not in mySet and "Nederland" not in mySet:
    mySet = mySet.union(theirSet)
else:
    if "Deutschland" in mySet: mySet.update(["Deutschland", ])
    if "Nederland" in mySet: mySet.update(["Nederland", ])
while len(mySet) > 5:
    if "Iran" in mySet:
        mySet.remove("Iran")  # Will raise error if does not exist
        continue
    # mySet.discard("Iran")  # WON'T raise error if does not exist
    mySet.pop()
else:
    mySet.update({1, 2, 3})
print(str(mySet) + " : " + str(mySet.difference(set(myList)).issubset(mySet)))
del mySet
print()

turkicCapitals = {
    "Turkey": "Ankara",
    "Azerbaijan": "Baku",
    "Turkmenistan": "Ashgabat",
    "Uzbekistan": "Tashkent",
    "Kazakhstan": "Astana",
    "Iran": "Tehran"
}
if "Kyrgyzstan" not in turkicCapitals:
    turkicCapitals["Kyrgyzstan"] = "Bishkek"
now = lambda: datetime.datetime.now()
if now().year > 2019:
    turkicCapitals["Kazakhstan"] = "Nur-Sultan"
if "Iran" in turkicCapitals:
    dictToList = list(turkicCapitals.values())
    if dictToList[len(dictToList) - 1] == "Tehran":
        turkicCapitals.popitem()
    else:
        del turkicCapitals["Iran"]  # turkicCapitals.pop("Iran")
if "Turkey" in turkicCapitals:
    for c in turkicCapitals:
        print(c + " : " + turkicCapitals.get(c))
print("{ " + str(len(turkicCapitals)) + " }")
turkicCapitals = dict(
    Turkey="Ankara",
    Azerbaijan="Baku",
    Turkmenistan="Ashgabat",
    Uzbekistan="Tashkent",
    Kazakhstan="Nur-Sultan",
    Kyrgyzstan="Bishkek"
)
eastTurks, westTurks = turkicCapitals.copy(), turkicCapitals.copy()
eastTurks.pop("Azerbaijan")
eastTurks.pop("Turkey")
westTurks.pop("Turkmenistan")
westTurks.pop("Uzbekistan")
westTurks.pop("Kazakhstan")
westTurks.pop("Kyrgyzstan")
turkicCapitals.clear()
del turkicCapitals
eTurk = wTurk = ""
for e in eastTurks.values(): eTurk += e + ", "
print("Eastern Capitals: " + eTurk)
for x, y in westTurks.items():
    wTurk += x + " : " + y + ", "
print("Western Capitals: " + wTurk)
turk, pTurk = "Turk".upper(), ""
for t in turk: pTurk += t
print(pTurk + "!!!")
print()

# Loops
for x in range(6): pass  # values from 0 to 5
# range(2, 5) => from 2 to 5
theRange = ""  # range(0, 11, 2) => from 0 to 10, increment step is 2
for x in range(0, 11, 2):
    theRange += str(x) + ", "
else:
    print(theRange)


# Functions and Lambda Expressions
def arbitrary_args(*people):
    if people[0] != "Amin": return
    print(people)  # Tuple


arbitrary_args("Amin", "Queeny", "Jun")


# noinspection PyUnusedLocal
def kwargs(first, second, third): pass  # Keyword Arguments


kwargs(first="Amin", second="Queeny", third="Jun")


def arbitrary_kwargs(**people): print(people)  # Dict


arbitrary_kwargs(first="Amin", second="Queeny", third="Jun")


def sum_nums(nums):
    s = 0
    for n in nums: s += n
    return s


def mean():
    return lambda *nums: (sum_nums(nums)) / len(nums)


print("Mean: " + str(int(mean()(4, 5, 6))))
print()


# Classes
class Living:
    def __init__(self, birth, height, max_lifespan):
        self.birth = birth
        self.height = height
        self.max_lifespan = max_lifespan

    def age(self):  # Can use anything instead of "self", but have to be the first parameter.
        return now().year - self.birth


class Animal(Living):  # pass
    def __init__(self, birth, height, max_lifespan, is_vertebrate, hands, feet, eyes):
        Living.__init__(self, birth, height, max_lifespan)  # WITH "self"
        self.is_vertebrate = is_vertebrate
        self.hands = hands
        self.feet = feet
        self.eyes = eyes


class Human(Animal):
    def __init__(self, name, birth, height, loves, friends):
        super().__init__(birth, height, 122, True, 2, 2, 2)  # WITHOUT "self"
        self.name = name
        self.loves = loves
        self.friends = friends

    def __iter__(self):
        self.itLoves = 0
        return self

    def __next__(self):
        if self.itLoves < len(self.loves):
            ret = self.itLoves
            self.itLoves += 1
            return self.loves[ret]
        else:
            raise StopIteration


mahdi = Human("Mahdi", 2000, 173, ("Amin", "Jun", "Queeny"), ["Maryam", "Adnan", "Bagher", "Surush"])
if now().year > 2016: mahdi.height = 178.5
if mahdi.age() > mahdi.max_lifespan:
    del mahdi.height
    del mahdi
else:
    print("Hello, my name is " + mahdi.name + ". I'm a " + mahdi.__class__.__name__.lower() + " being.")
    print("I'm " + str(mahdi.age()) + " years old and " + str(mahdi.height) + " centimetres tall.")
    print("I have " + str(mahdi.hands) + " hands, " + str(mahdi.feet) + " feet and " + str(mahdi.eyes) + " eyes.")

    itMahdi = iter(mahdi)
    printable = "My loves are "
    printable += next(itMahdi) + ", "
    printable += next(itMahdi) + " and "
    printable += next(itMahdi) + "."
    print(printable)

    myIt = iter(mahdi.friends)
    printable = "My close friends are "
    printable += next(myIt) + ", "
    printable += next(myIt) + ", "
    printable += next(myIt) + " and "
    printable += next(myIt) + "."
    print(printable)
    for x in mahdi.friends:
        # The for loop actually creates an iterator object
        # and executes the next() method for each loop.
        pass
    print()

# Date & Time plus Math
print(now().strftime("Right Now: %A, %Y.%m.%d %H:%M:%S"))
birthAmir = datetime.datetime(2000, 4, 9)
print("AMIR's Birth Date: " + str(birthAmir))
print("Built-In Math: " + str(min(1, 100, 2) + max(3, 15, 4)) + " - " + str(abs(-16)) + " - " + str(pow(2, 4)))
print("Modular Math: " + str(math.floor(math.sqrt(64) + math.pi)) + " - " + str(math.ceil(10.4)))
print()

# JSON
skills = '''{
    "Photoshop":85, "HTML & CSS":95, "JavaScript":90, "jQuery":30,
    "PHP":78, "Flash":5, "Android Dev":88, "Java":95,
    "Kotlin":95, "Flutter":80, "Dart":95, "After Effects":20,
    "Python":20, "Bootstrap":19
}'''
myJson = json.loads(skills)
print("Python: " + str(myJson["Python"]) + "%")
languages = {
    "Persian": 100,
    "Azerbaijani": 30,
    "English": 100,
    "Formal Arabic": 50,
    "Hebrew": 15
}
jsonText = json.dumps(languages, indent=2)
# None of "dumps"'s keyword arguments are required. More arguments:
# sort_keys=True
# separators=(". ", " = ")
print("My Languages: " + jsonText)
print()

# RegEx
reText = "AMIN is barbie!"
mySearch = re.search("^AMIN", reText)  # Match object
if mySearch is not None:
    print("Found: " + reText[mySearch.span()[0]:mySearch.span()[1]])
myFindall = re.findall("a", reText.lower())
print(myFindall)
mySplit = re.split(" ", reText)
print(str(mySplit) + " - " + str(re.split("", reText, 9)))
myReplace = re.sub("\s", " - ", reText)
print(myReplace)
print()

# Errors
try:
    print("Trying" + "...")
except TypeError:
    print("An error occurred!")
else:
    print("No error occurred!")

try:
    # noinspection PyTypeChecker
    print("String" + 1)
except:
    print("An error occurred!")
finally:
    print()

# User Input
# how = input("How are you today?")
print("Be tokhme chapam!")
# Python 3.6 uses the input() method.
# Python 2.7 uses the raw_input() method.

# String Formatting
aminsAge = now().year - 1999
txt = "AMIN is {} years old!"
print(txt.format(aminsAge))
australiaMinimumWage, costOfLiving, ausBrakhah = 2520, 55.58, "{}. Australia's Economic Brakhah: {:.2f}"
print(ausBrakhah.format(9, australiaMinimumWage / costOfLiving))
print("New Zealand: {1}, USA: {2:.1f}, Japan: {0:.2f}".format(68, 100, 74))
print("Oman: {om}, Arabia: {sa}, UAE: {ua}, Qatar: {qt}, Kuwait: {kw}".format(om=56, sa=55, ua=53, qt=48, kw=40))
print()

# List all the function names (or variable names) in a module:
print(dir(file))
