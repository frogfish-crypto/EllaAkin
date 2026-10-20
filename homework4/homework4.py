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
