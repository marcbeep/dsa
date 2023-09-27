# Cheatsheet - Python

## Operators

```
+, -, /, *, %, <, >, <=, >=, !=, ==
```

## Variables & Names

```
number = 100
type = audi
print "There are", number, "cars available."
print "There are %d cars available" % number
print "Type of car: %s." % type
```

## Prompts

```
age = raw_input("How old are you? ")
```

## Reading files

```
from sys import argv
script, filename = argv
txt = open(filename)
print "Here's your file %r:" % filename
print txt.read()
```

## Writing files

```
print "Opening the file..."
target = open(filename, 'w')
print "Truncating file..."
target.truncate()
```

## Functions

```
def print_two(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)
```

## For Loops

```
count = [1, 2, 3, 4, 5]
for number in count:
    print "Number: %d" % number
```

```
elements = []
for i in range (0, 6):
    print "Adding %d to the list." % i
    elements.append(i)
```

## While Loops

```
i = 0
numbers = []

while i < 6:
    print "At the top i is %d" % i
    numbers.append(i)
    i = i + 1
    print "Numbers now: ", numbers
```

## Accessing Lists

```
animals = ['bear', 'tiger']
bear = animals[0]
```

## Bigger program

```
from sys import exit

def room():
    print "How much gold do you take?"

    next = raw_input("> ")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("No number")

    if how_much < 50:
        print "You're not greedy, you win!"
        exit(0)

def dead(why):
    print why, "Good job!"
    exit(0)
```

## List operations

```
list = ["apple", "banana", "orange"]

Negative Indexing (Start from End) - print(list[-1])

Range - print(list[2:5])
print(list[:4])
print(list[2:])

Insert - list.insert(2, "watermelon")

Add - list.append("kiwi")

Extend - adds to end of list
list2 = ["tropical", "juice"]
list.extend(list2)

Remove - list.remove("banana")

Pop (specified Index) - list.pop(1)

Loop through Indexes -
for i in range(len(list)):
    print(list[i])

List comprehension -
fruits = ["apple", "banana", "kiwi"]
newlist = [x for x in list if "a" in x]
# prints apple, banana

Sort - list.sort()

Sort Descending - list.sort(reverse=True)

Custom sort (this sorts based on how close the number is to 50) -
def func(n):
    return abs(n-50)

list = [100, 50, 65]
list.sort(key = func)

Copy lists - list1 = list2.copy()
```

## Dictionaries

```
thisdic = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}

print(thisdict["brand"])
```

## Getting things from things

```
# Dict Style
mystuff['apples']

# Module Style
mystuff.apples()
print mystuff.tangerine

# Class Style
thing = MyStuff()
thing.apples()
print thing.tangerine
```

## Object oriented example

```
class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)


happy_bday = Song(["Happy bday", "Line 2", "Line 3"])
bulls_on_parade = Song(["Bulls Line 1", "Bulls Line 2"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()
```
