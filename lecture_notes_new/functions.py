#Function notes from class

# def say_hello(name):
#     print("Hello",name)

# say_hello(name="Ella")

# def add(a,b):
#     return a+b

# print (add(7,8))

# if, elif, else

#if main condition 
#   do something
# elif secondary condition 
#   do something
# else
#   do something

# x=5
# if x%2==0:
#     print("x is even")
# else:
#     print("x is odd")



# def check_num(num):
#     if num>0:
#         return ("num is positive")
#     elif num<0:
#         return("num is negative")
#     else:
#         return("num is zero")

# print (check_num(8))

# print(41>0)

# def can_vote(age, is_citizen):
#     if (age>18 and is_citizen==True):
#         return ("Can vote")
#     elif (age<18):
#         return ("Don't even touch the voting booth you child")
#     else:
#         return ("You can have a sticker")

# print(can_vote(19, False))

# def is_weekend(day):
#     if (day == "Saturday" or day == "Sunday"):
#         return "It is the weekend!"
#     else:
#         return "GO BACK TO WORK"

# print(is_weekend("Monday"))

# for i in range(10):
#     print ("aaaaaa", end="")
#     print("")

# fruit_basket = ("Lychee", "Mango")

# for fruit in fruit_basket:
#     print(fruit)

# def countdown(start):
#     while start>0:
#         print("T-", start)
#         start -= 1
#     print ("Liftoff!")

# countdown(10)

# def temperature(temp):
#     if (temp<65):
#         return ("It's cold today")
#     elif (temp>80):
#         return("It's hot today")
#     else:
#         return("it's warm today")

# print(temperature(70))


x= [40, 80, 10, 30, 50, 20]

list2 = [60, 87, 9, 50, 11]

# print(min(list))
# print(max(list))

#But we actually need it to be a return funtion in case we need the value later on 
#Define an argument if you want it to apply to anny list using the print function 

# def minimum():
#     return min(list)

# print (minimum())

# #This is if you want the guy to always reference a certain list 

# def minimum(x):
#     return min(x)

# print (minimum(list2))



# def maximum(x):
#     return max(x)

# print (maximum(list2))

# Create a function to determine if a positive integer is a prime number 

def primetime(num):
    if num<=0 or type(num)!=int:
        return "not positive integer"
    else:
        if num==1:
            return "neither prime nor composite"
        elif num==2:
            return "uhhhhhh hmmmmm"
        else:
            if num%2==0:
                return "not a prime"
            else:
                for i in range (2,num):
                    if num%i==0:
                        return "not a prime"
                    else:
                        return "prime!"

num=7
print(primetime(num))


# lists and dicts
numbers = [1, 2, 3, 4]

print(numbers)

fruits = ["apples", "cherries", "bananas"]

#can have diff elements and data types

mixed=["hello", 5, True, None]

print(mixed)

print(numbers[0])

fruits[0]="grape"

print(fruits)

numbers.append(5)

print(numbers)

#can insert into list instead of appending 

print(mixed.insert(1, False))
#list.insert(where you want to put it in index, value you're inserting)

#removing a word: 
print(fruits.remove("bananas"))

#pop function can remove based on index rather than value
print(fruits.pop(0))
#removes last element if parentheses empty 

#Slicing
list=[12,14,16,18,20]
sub_list = list[1:4]

nums = [1, 2, 3, 4, 5]
sub_nums = nums[1:4]

print(sub_nums)

#striding
list = [12, 14, 16, 18, 20, 22]

print(list[::1])

print(list[1:8:2])
#want it to start at 1, end at 8, and then go in steps of two

#range object should start from zero 

# print(nums[1:4])
# #gives 1 index to 4 index 
# #exclusive - not inclusive
# print(nums[3:])
# # same thing 
# print[:]
# #prints whole guy

# dict.values()
# dict.keys()
# dict.items()

# list.copy()
# list.clear()
# #Slicing lists - start is inclusive and stop is exclusive 

# dict["key"] = "value"
# del dict["key"]
# dict.clear()

#need to know common list functions 
#To access keys, values, items 
#secret code is lock#########

# list1=[0, 1, 2, 3, 4, 5 ,6 ,7, 8 ,9, 10]

# def range(start,end):
#     list_range=list1[start:end]
#     return list_range

# print(range(0,4))


# #to access an items in a nested line, use list[row][column]
# nested_list=[[2,4,6],
#              [8,10,12],
#              [14,16,18]]

# print(nested_list[2][1])


# stars_data = {
#     "name":["Sirius","Vega", "Altair"],
#     "Magnitude":[]
# }

# #use a for loop to print the nanes


# # for name in stars_data.values():

# list=[0,1,2,3,4,5]
# index=0
# while index<len(list):
#     print(list[index])
#     index+=1


# #nested lists and arrays 

# nested_list = [ [2, 4, 6],
# 				[8, 10, 12] 
# ]

# print(nested_list)

# arr = np.zeros((2,5))
# arr

# array([[0., 0., 0., 0., 0.],
#         [0., 0., 0., 0., 0.]])

# np.argmin 
# np.argmax
#arg is used for a lot of things to give position of a value 


# scores[argmin] 
# scores[argmax]
# pulls values at those indexes

# we want to find out highest exam scores 
# axis - way it moves across rows and columns is counterituitive

#what does np.linspace(10,100,10) produce?
#how do you make four horizontal subplots?
#How do you four vertical subplots?
# How do you make a legend
#Create a plot of tan(x) from 0 to 4pi
#answers will come later in matplotlib

#pandas series 

import pandas as pd

##Pandas series
#grade = pd.Series([88, 90, 80, 70, 60]) 
#print(grade.mean())
#print(grade.min)
#print(grade.max)
# Pandas series is kind of a weird list and array combo
# we're gonna use data frames though - each row and column is a pandas series and data frame holds them all in one data fram
# pandas outputs data more nicely and can hold more data 
# pandas can store multiple data types 
# Dictionary - way 1 to create a data frame
#data= {
# "Name" : ["Alice", "Bob", "Charlie"]
# "Age" : [25, 30, 67]
# "City" : ["LA", "SF", "NY"]
# }
# 
#print (data["age"]) 
#def = pd.DataFrame(data)
#df 
##this will produce a data frame (cute little table)
# print(df["Name"])
# #this is a pandas series inside the data fram (each row and column is its own pandas series)
##can also print multiple columns 
#df[["Name", "Age"]]
#df
# df[df["Age"]>25]
#df
# # this adds a conditional where it'll filter the data to only people older than 25
# df[df["City"]=="SF"]
#df
## will give us only the person who lives in sf
## now we want to age everyone up a year:
# df["Age"]= df["Age"]+1
# df 
# #every time you run the cell in jupyter it will rmeber, to resturn to original age you gotta run the above cell that initially defined the data frame (df)
##remember to dio df to run the data fram every time 
# df["Senior"] = df["Age"]>30
#df
# #will return a data frame that has a boolean true or false
# #will be true if over 30 
# #loc and iloc
# #loc is label indexing and works with column and row names 
# #while iloc works with the indicies themselves
# #one is inclusive or something
# df.loc[0,:]
##first input is row, second is column
# df.loc[row,column] - to have all columns, use a colon 
# print(def.loc[:, "Name"])
## integer indexing  
# print(df.iloc[0,:])
## does all the columns
# print(df.iloc[:,0])
# # does all the damn rows
# download students.csv file
## 3rd way to create a data frame 
#df = pd.read_csv("students.csv")
#df.head()
# to do bigass title in juptyer: hastag twice to get big title vrsus hastag once to get a normal sized totle for the cell lolllllll
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# k

# from astro.io import fits
# from astropy import units as u 
# with fits.open("spitzer_image.fits") as hdul:
#     header = 
#     data = hdul[0]

#     data

# print(header["NAXIS"])
# print(header["DATE"])
# print(header["EXPTIME"])
# #naxis1 defines pixels tht lie across detectors and naxis2 defines pixels that lie down it 
# plt.fig(figsize=(10,5))
# plt.imshow(data, cmap = "inferno", origin = "lower")
# plt.hist(data.ravel(), bins = 100)
# plt.colorbar()
# plt.show()

# # you can take a file with your phone then totally reconstruct and process it as a fits file in python 
# #add a vmin and vmax argument to see 


