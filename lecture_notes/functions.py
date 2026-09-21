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

def can_vote(age, is_citizen):
    if (age>18 and is_citizen==True):
        return ("Can vote")
    elif (age<18):
        return ("Don't even touch the voting booth you child")
    else:
        return ("You can have a sticker")

print(can_vote(19, False))

def is_weekend(day):
    if (day == "Saturday" or day == "Sunday"):
        return "It is the weekend!"
    else:
        return "GO BACK TO WORK"

print(is_weekend("Monday"))

for i in range(10):
    print ("aaaaaa", end="")
    print("")

fruit_basket = ("Lychee", "Mango")

for fruit in fruit_basket:
    print(fruit)

def countdown(start):
    while start>0:
        print("T-", start)
        start -= 1
    print ("Liftoff!")

countdown(10)

def temperature(temp):
    if (temp<65):
        return ("It's cold today")
    elif (temp>80):
        return("It's hot today")
    else:
        return("it's warm today")

print(temperature(70))