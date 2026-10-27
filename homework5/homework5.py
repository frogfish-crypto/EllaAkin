# Git is the local version control just for your own computer, github is the google-docs-like online website that holds repositiories you can share with people
# Terminal is the pop up window, while the command line is the actual interface you use to communicate with your computer 
# Local repository is the version history and branches of your code on your own computer, which you can push to a remote repsitory like Github to share with people
# Version control is the ability to save and later look at or restore past versions or snapshots of your code. It tracks modifications essentiallly
# Staging area is that inbetween point where things going to git stay before they get saved to your version history. It's where files go when you say git add.
# git add adds stuff to the staging area 
# git commit adds the changes you've made to the file(s) to your local repository 
# git push sends it from your local repo to a remote repo like github
# git status shows what's currently in your staging area and what is being tracked 
# git pull can take chnges from a remote repo and apply them to your local repo
# pwd prints the working directory, as in whch part of which file path you currently are in 
# ls lists all the files in your current folder
# cd changes your current directory to whatever you specify, like cd Desktop
# nano lets you edit files in the terminal
# touch creates a new file in your current folder
# mv moves files from one location to another (you need to type out or otherwise indicate both folder paths)
# rm removes a file that is specified. You can also delete every file on your computer if you type a specific phrase that I'm not going to type because I'm scared
# cat reads and prints out the contents of your file(s) (stands for concatenate)
# 2.2 
# pwd
# ls
# (cd ..) then (cd brianna_repo) then (git pull)
# mv homework.py ~/python_decal/judy_decal/homework/
# cd ~/python_decal/judy_decal/homework/
# cat homework.py
# git add, git commit -m "new changes to homework", git push
# git pull origin main, git push origin main
# ~/Recent/
# 2.3 photo added to the folder

# 3:
 
def checkDataType(var):
    dataType = type(var).__name__
    return dataType

print(checkDataType(3.14))
print(checkDataType(True))

# 3.2: 
def evenOrOdd(num):
    if num%2==0:
        return "Even"
    else: 
        return "Odd"

print(evenOrOdd(7))
print(evenOrOdd(10))

# 4:  
def sumWithLoop(numbers):
    sum=0
    for i in numbers:
        sum+=i
    return sum

numbers = [1, 2, 3, 4, 5]
print(sumWithLoop(numbers))


# 5:
def duplicateList(list):
    newList = []
    for i in list:
        newList.append(i)
        newList.append(i)
    return newList
list = ['a','b','c']
print(duplicateList(list))

# 5.2 
# It was missing a colon
def square(num):
    return num*num

num=2
print(square(num))

