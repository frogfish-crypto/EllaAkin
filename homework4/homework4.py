# list operations

fav_foods=["wood ear mushrooms", "lasagna", "pizza", "hot pot", "potato"]
print(fav_foods)

# second food in list
print(fav_foods[1])

# last food with negative indexing
print(fav_foods[-1])

#append new food 
fav_foods.append("acai bowl")
print(fav_foods)

#insert apple
fav_foods.insert(0, "apple")
print(fav_foods)

#remove third item 
fav_foods.remove(fav_foods[2])
print(fav_foods)

print(len(fav_foods))

for food in fav_foods:
    food.upper()
print(fav_foods)

fav_foods_2 = fav_foods[::len(fav_foods)-1]
print(fav_foods_2)

if "potato" in fav_foods:
    print("A potato!")
else:
    print("No potato!")


# 3.2
numbers = list(range(0, 21))
print(numbers)
# 1
def get_first_fifteen (numbers):
    for i in numbers:
        return numbers[:15:1]

print(get_first_fifteen (numbers))
# 2
lst=get_first_fifteen (numbers)
def get_every_fifth (lst):
    for i in lst:
        return lst[::5]
    
print(get_every_fifth(lst))

# 3
lst = get_every_fifth(numbers)
def reverse_and_stride(lst):
    return lst[::-3]

print(reverse_and_stride(lst))
    

# 3.3 Nested lists
# 1
numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(numbers[2][::])

# 2
print(numbers[1][1])

numbers.append([10, 11, 12])
print(numbers)

def sum_nested(numbers):
    tot_sum=0
    for sublist in numbers:
        for num in sublist:
            tot_sum+=num
    return tot_sum

print(sum_nested(numbers))


# 3.4


def nest_list():
    final_list = []
    current_num = 1
    for i in range(5):
        sublist=[]
        for j in range(5):
            sublist.append(current_num)
            current_num+=1
        final_list.append(sublist)
    return(final_list)

final_list = nest_list()
print(final_list)


def replace_3s(final_list):
    for sublist in range(len(final_list)):
        for num in range(len(final_list[sublist])):
            if final_list[sublist][num]%3 == 0:
                final_list[sublist][num]='?'
    return final_list

print(replace_3s(final_list))

list = final_list
def sum_non(list):
    sum=0
    for sublist in range(len(final_list)):
        for num in range(len(final_list[sublist])):
            if final_list[sublist][num]!= '?':
                sum+=final_list[sublist][num]
    return sum

print (sum_non(final_list))


# Dictionaries 

ages = {
    "Katie" : 30,
    "Mariam" : 42,
    "Safia" : 25,
    "Mira" : 48
}

print(ages["Katie"])

ages["Mira"] = 100
print(ages)

ages.pop("Mariam")
print(ages)


# import matplotlib.pyplot as plt

# import numpy as np

##sin function 
#x = np.linspace(0, 2 * np.pi, 100) 
#y = np.sin(x)
#plt.figure(figsize = (6,4))
#plt.plot(x,y) 
#plt.show() 
#(to change period:
##just change y=np.sin(2*x)
##I think)
##several functions to same plot
#y1 = np.sin(x)
#y2 = np.cos(x)
#new cell
#plt.figure()
#plt.scatter(x, y1,label = "sin(x)")
#plt.scatter(x, y2, label = "cos(x)", color = "purple")
#plt.title("Sine and cosine wave")
#plt.xlabel("x values (radians)")
#plt.ylabel("f(x)")
#plt.legend()
#plt.show()
#new cell
#plt.figure()
#plt.plot(x, y1, color = "xkcd:ickygreen", linesyle = "-.", linewidth=10, alpha = 0.5, marker = "*")
#plt.show
##normally you wanna label all the axes 
#but this is just to show customization so she didn't bother
#marker draws a shape at every data point, asterisk gives you a star
#alpha is transparency 
#
##subplots - depends on having done the data series stuff (up above)
#fig, axes = plt.subplots(1, 2, figsize = (10, 4))
#axes[0].plot(x, y1, color ="teal", ls= ":")
##specify the subplot you're talking about ^ x and y1 indicates our sin graph
#axes[0].set_title("Sine Wave")
#axes[1].plot(x, y2, color = "cornflowerblue", ls = "--")
#axes[1].set_title("Cosine Wave", color = "indigo")
##should create two graphs side by side, one sine one cosine 
##subplots use  
##How would you plot two subplots vertically?
##      What woud you set the figsize to?
#fig, axes = plt.subplots(2,1, figsize=(4, 8)) ##instead of (1,2) lol
##How would you change the colors of the titles
##axes[0].settitle("Sine Wave", color = "pink") and change it for each of the axes things
##How would you change the lines to scatter plots
##axes[1].scatter(x, y^2, color ="cornflower blue")
##What do you need to call when when you finish a figure
# idk is it plt.show()?
#can do semicolons at theend of each thing too as a shortcut
# axes[0].scatter(x, y1, color ="teal", s=3)
# #Let's make two side by side subplots and plot on both?
#fig, axes = plt.subplot(1,2,figsize=(8,8))
#
# axes[0].
# #
#plt.figure
#
# 
# 
# 
# 
# 
# 
# j

