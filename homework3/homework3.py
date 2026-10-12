
#1. Print functions
    # Say Goodbye
def say_goodbye(name):
    print("Goodbye", name)

name = "Meryl Streep"
say_goodbye(name)

    # Area of a circle 
def area_circle(radius):
    print(radius*(3.14))

radius = 3
area_circle(radius) 

#2. Return Functions
    #Subtract, multiply, and divide
def subtract(a, b):
    return(a-b)

a=10
b=3
print(subtract(a,b))

def multiply(a, b):
    return(a*b)

a=10
b=3
print(multiply(a,b))

def divide(a, b):
    return(a/b)

a=6
b=3
print(divide(a,b))

#3. Conditionals
    #What should I wear?
temperature = [100, 90, 78, 101, 66]

def what_to_wear(temprature):
    minimum = min(temperature)
    maximum = max(temperature)
    return(minimum,maximum)

print(what_to_wear(temperature))

    # Check if it's the weekend
Monday = 1
Tuesday = 2
Wednesday = 3 
Thursday = 4
Friday = 5
Saturday = 6 
Sunday = 7

def is_weekend(day):
    if day==6 or day==7:
        return "It is the weekend!"
    else: 
        return "It is not the weekend."

print(is_weekend(Monday))


    #Fuel efficiency calculator 
def fuel_needed(miles, gallons):
    efficiency = miles/gallons 
    print("Miles per gallon:")
    return efficiency

print("Miles per gallon:", fuel_needed(10, 2))

    #secret code
def encrypt(num):
    if num%1==0:
        final_digit = num%10
        num_chunk = num//10
        multiplier = 1
        while multiplier <=(num_chunk):
            multiplier*=10
        new_num = final_digit*multiplier + num_chunk
    return new_num

num = 12345

print(encrypt(num))

# Loops

    # Oski stole your power
def power_function (x, y):
    magnitude = 1
    for i in range (y-1):
        magnitude*=10
        raised_x = x*magnitude
    return raised_x
print(power_function (10, 5))

    # Min and max with loops 

        # For loops
list = [4, 3, 6, 10, 0.5, 2]

def minimum(list):
    minimum=list[0]
    for i in range(len(list)):
        if list[i]<=minimum:
            minimum=list[i]
    return minimum

print(minimum(list))

def maximum(list):
    maximum=list[0]
    for i in range(len(list)):
        if list[i]>=maximum:
            maximum=list[i]
    return maximum

print(maximum(list))


        # While loops
def minimum_while(list):
    num=list[0]
    minimum=list[0]
    count=0
    while count<len(list):
        if list[count]<=minimum:
            minimum = list[count]
        count+=1
    return minimum

print(minimum_while(list))

def maximum_while(list):
    num=list[0]
    maximum=list[0]
    count=0
    while count<len(list):
        if list[count]>=maximum:
            maximum = list[count]
        count+=1
    return maximum

print(maximum_while(list))

    # Calculate the sum

num=2468

def summation(num):
    sum_num=0
    num_as_str=str(abs(num))
    for digit in (num_as_str):
        sum_num+=int(digit)
    return sum_num

print(summation(num))


num=1111
result = (summation(num)) #should equal 4
print(f"The result of calculating all the digits in this equation (6.3) with num={num} is {result}" )




# File: average_vowels.py

# You’re curious about the average number of vowels compared to consonants in a paragraph.

# --- 1. Counting Vowels ---
# Write a return function that takes a string as input.
# The function should return a tuple containing:
#     (number of vowels, number of consonants)
# Name this function: counting_vowels_and_consonants()

# Hint: You can use .isalpha() to check if a character is a letter.


# --- 2. Average Vowels ---
# Write a return function that takes in a paragraph (string) as input.
# The function should:
#   - Split the paragraph into individual sentences.
#   - Use counting_vowels_and_consonants() to count values for each sentence.
#   - Return a tuple: (number of sentences, average vowels per sentence, average consonants per sentence)
# Name this function: average_vowels_and_consonants()

# Here is your paragraph to analyze. It is a quote from Richard Feynman. 
paragraph = (
    "Fall in love with some activity, and do it! "
    "Nobody ever figures out what life is all about, and it doesn't matter. "
    "Explore the world. "
    "Nearly everything is really interesting if you go into it deeply enough. "
    "Work as hard and as much as you want to on the things you like to do the best. "
    "Don't think about what you want to be, but what you want to do. "
    "Keep up some kind of a minimum with other things so that society doesn't stop you from doing anything at all."
)

# Write descriptive print statements, with f-strings, that output the average vowels and consonants per sentence of the paragraph. 


string = paragraph
vowels_list = set("aeiouAEIOU")

def counting_vowels_and_consonants(string):
    vowels = 0
    consonants = 0
    for char in string:
        if char.isalpha():
            if char in vowels_list:
                vowels+=1
            else: 
                consonants+=1
    return vowels, consonants

print (counting_vowels_and_consonants(string))



def average_vowels_and_consonants(paragraph):
    total_sentences=0
    total_vowels = 0
    total_consonants = 0
    sentence_count = 0
    avg_consonants = 0
    avg_vowels = 0
    sentences = []
    current_sentence = ""
#ok so here I'm trying to split the text up into sentences
    for char in string:
        current_sentence += char
        if char in [".","?","!"]:
            sentences.append(current_sentence)
            total_sentences += 1
            current_sentence = "" 
            #resets it
    for sentence in sentences:
        vowels,consonants = counting_vowels_and_consonants(sentence)
        total_vowels += vowels 
        total_consonants += consonants
    sentence_count = total_sentences
    # floor division to return whole numbers
    avg_vowels=total_vowels//total_sentences
    avg_consonants=total_consonants//total_sentences
    return sentence_count, avg_vowels, avg_consonants

sentence_count, avg_vowels, avg_consonants = average_vowels_and_consonants(paragraph)

print(f"Total Sentences Analyzed: {sentence_count}")
print(f"Average Vowels per Sentence: {avg_vowels}")
print(f"Average Consonants per Sentence: {avg_consonants}")