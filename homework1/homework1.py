#File: homework1.py

# --- Variables and Data Types ---
a = 10 
print (a)
print (type(a))

b = 1.5
print (b)
print (type(b))

c = 3j
print (c)
print (type(c))

d = "hello"
print (d)
print (type(d))

e = [1, 2, 3]
print (e)
print (type(e))

f = {"name":"Ellen", "favorite fruit:": "strawberry"}
print (f)
print(type(f))

g = (1, 2)
print (g)
print (type(g))

h = ["apple", "banana", "strawberry"]
print (h)
print (type(h))

i = True
print (i)
print (type(i))

j = None
print (j)
print (type(j))

k = ["True", "blue", "12"]
print (k)
print (type(k))

l = str(14)
print (l)
print (type(l))

m = 1e4
print (m) 
print (type(m))


# 1: I found 9 
# 2: int, float, complex, str, list, dict, tuple, bool, Nonetype
# 3: m, c, b are all float, l and d are str, e, h and k are list
# The data type of l is str. It looks like str() converts whateveris enclosed in the parentheses into a string

n = b"hello"
print (n)
print(type(n))

# --- Booleans ---
print(10>9) # True, 10 greater than 9
print(10==9) #False, 10 does not equal 9
print(10<=9) #False, 10 is not less than or equal to 9
print(bool("abc")) #True 
print(bool(["apple", "cherry", "banana"])) #True
print(bool(True)) #True
print(bool(False)) #False
print(bool(0)) #False
print(bool("")) #False
print(bool(" ")) #True
print(bool(())) #False
print(bool([])) #False
print(bool({})) #False
print(bool(True and False)) #False
print(bool(True and True)) #True
print(bool(False and False)) #False
print(bool(True or False)) #True
print(bool(True or True)) #True
print(bool(False or False)) #False
print(bool(not(False))) #True
print(bool(not(True))) #False

# 1: I noticed that if False in included anywhere (in "and" operations) it switches to False, and the default appears to be false for empty bool() functions and empty lists and strings but true for non-empty lists and strings
# 2: I was surprised that empty lists, dicts, and tuples in bool default to False 
# 3:
print(4//3==1)
# This will return true because if you round 4/3 down to the nearest whole number it will be 1 
# 4: 
print(21!=21)
#This will return False because  21 != 21 is saying "21 does not equal 21"

# --- Operators ---
print(10+5) #returns 15, performs addition
print(10-5) #returns 5, performs substraction
print(2*4) #returns 8, performs multiplication
print(6/3) #returns 2, performs division
print(5%2) #returns 1, which is the remainder after diving 5/2
print(3**2) #returns 9, 3^2, raises first number to power of second number
print(15//2) #returns 7, floor division (rounds down to nearest whole number integer)

# Comparison Operators 
print(5==2) #False, it's asking if the two are equal
print(10!=10) # False, != means "does not equal" and they are equal
print(2<5) #True, 2 is less than 5
print(12>5) #True, 12 is more than 5
print (5<=6) #True, 5 is less than or equal to 6 (specifically less than)
print(1>=10) #False, 1 is not more than or equal to 10

#Assignments Operators
x = 5
x += 5
x -= 4
x *= 3
print (x) #returns 18; 5+5-4 equals 6, 6*3 equals 18

#Logical Operators
#1: The operator "and" returns true if everything included is true 
print(10>7 and 10>5) #This returns true 
print(10>7 and 10<5) #This returns false because 10<5 is not true

#2: The operator "or" returns true if anything included is true 
print(10>7 or 10<5) #Returns true because one statement is true
print(10<7 or 10<5) #Returns false because neither is true

#The operator "not" reverses the boolean so if something is false it's true and vice versa
print(not False) #Returns true
print(not True) #Returns false

#More questions: 
# 1: / returns a float while // returns a (rounded-down) int
# 2: % returns the remainder leftover after division and // returns 
# 3: Use modulus (%) to calculate the remainder when dividing two numbers
print(7%2) #returns 1
# 4: Assignment operators are used to store values in variables (like x = 6) and compound assignment operators perform simple math operations and thus assign a new value to a variable  

# --- Strings ---
my_string = "hello"
print(my_string) # prints hello
print(my_string[0]) #prints h 
print(my_string[1]) #prints e
print(my_string[2]) #prints l
print(my_string[3]) #prints l
print(my_string[4]) #prints o
print(my_string[-1]) #prints o (index starts from back)
print(my_string[1:3]) #prints from index 1 up to (stops before) index 3 ("el")
print(my_string[0:5:2]) #prints index 1 through 5 in steps of two (hlo) aka it skips every other letter
print(len(my_string)) #returns 5, the number of characters (index is length-1)
print(my_string+"goodbye") #prints hellogoodbye
print (7*my_string) #prints hello 7 times

# 1: slicing means extracting a new substring from an existing string. Every operation we did with my_string[] and at least one colon inside the brackets was slicing. (Without the colon it's just indexing)
# 2: 
name = "Oski"
print ("Hello, my name is", name)
#prints out Hello, my name is Oski
# 3: name = "Oski"
print (f"Hello, my name is", {name})
# The second version prints out Hello, my name is {'Oski'} instead of just Oski
# According to UToronto, f-strings convert variables of all types to strings for the puroses of printing the string but they do ot change the variable's actual data type as defined


# --- Terminal Commands ---
# cd 
# Changes directories. Use it to move from folder to folder
# cd Documents will take you to the folder Documents 

# ls
# lists everything in your current directory
# ls 

# ls -a
# Shows all the regular AND hidden files in your current directory
# ls -a EllaAkin will show all the files and hidden files in the directory

# mkdir
# Makes a new directory 
# mkdir homework2

# cat
# Displays everything in the file in terminal
# cat file.txt

# pwd
# prints what directory you are in
# pwd will say something like /Users/Ella/Documents

# cd ..
# Changes directory to parent directory 
# cd ..

# cd. 
# changes director to same directory 
# cd.

# cd~
# Takes you to home folder, same as cd by itself
# cd~

# cp
# Copies files and folders from one place to another
# cp file.txt file-new.txt (the duplicate file is named file-new.txt)

# mv 
# moves files 
# mv ~/Downloads/MyFile.txt ~/Documents/Work/MyFile.txt

# rm 
# removes a file permanently
# rm file.text

# clear
# erases everything previously run in the terminal
# clear 

# grep
# Searces for all instances of a given text with a file
# grep "error" file.txt

#1: 
# ls -S
# Lists everything in the directory by size 
# 

# du
# shows disk usage of each subdirectory 
# du

# ditto -V 
# Copies everything in one folder to another with status updates
# ditto -V /Documents /Newfolder

# 2: ls shows the files that aren't hidden, while ls -a shpws all the files including the hidden ones
# 3: A hidden file does not show up when you search with ls unless you specifiy that you want to search for hidden files 
#   An example is .git, where the dot indictates the file should be hidden by default
# 4: -i is ignore case, used in grep to ignore charcters' case (upper or lower) when searching for text 
#   grep -i "word" file.txt 
#   -l is long format, which makes the ls command display everything with more detailed descriptions
#   ls -l 
#   - n for number makes grep print line numbers alongside the instances of the gven text it finds
#   grep -n "word" file.txt


