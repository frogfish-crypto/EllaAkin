# File: homework2.py

# Your file path should look like:
# python_decal_fa25/yourname/homework2/homework2.py

# Questions (Answer these in the homework2.py file as comments):
# 1) What’s the difference between Git, GitHub, and Git Bash?
    # Git is the local version of the version control tool that lets you track code history on just your computer
    # GitHub is an online system that tracks version history for your code and allows you to share it with others
    #Git Bash is the terminal app that lets you use git commands for Windows
# 2) What’s the difference between the terminal and the command line?
    #Terminal is the window itself, and the command line is the environment you enter the commands in
# 3) How does Windows PowerShell differ from Git Bash?
    #PowerShell is the built in terminal for Windows, while Git Bash is an emulator 
# 4) What’s the difference between Anaconda, conda, and Python?
    #Anaconda is the overall library of many packages like numpy, conda, etc
    #conda is a package manager/installer built into anaconda
    #python itself is the programming language than can use packages for calculations and other purposes
# 5) What is VS Code? 
    # VS code is a code editing application that works with many languages, not just python. 
# 6) What is a Jupyter Notebook? How is it different from Jupyter Lab?
    #a Jupyter notebook is an individual document in the larger Jupyterlab workspace.
# 7) What does ~/ mean?
    #It represents the home directory like /Users/Ella
# 8) What’s the difference between an absolute path and a relative path?
    #absolute path specifies a file or directory based on the overall path starting from the root directory. 
    #Meanwhile, a relative path specifices a location based on your current directory
    #For example the path would be shorter if you were already in one of the directories along the path
# 9) Imagine you're in your "yourname" repo. Write the absolute and relative paths to "course_assignments/homework2".
    #Absolute: /Users/Ella/Desktop/python_decal_fa26_2/EllaAkin/course_assignments/homework2
    #Relative: course_assignments/homework2
# 10) What command lets you move from "course_assignments/homework2/" to "course_assignments/"?
    #cd ..
# 11) What would rm ./ do in your current directory? (Don’t try it!)
    #I think it would delete everything in the current directory 
# 12) What do the following commands do?
# git add
    #moves your new files to staging area
# git commit
    #saves the files at that moment in time 
# git push
    #pushes the commits to a remote repository 
# 13) What's the difference between "git add ." and "git add <file>"?
    #git add . adds everything in the directory, while git add <file> just adds that specific file 
# 14) What do "git status" and "git log -1" do?
    #git status shows you what your repo is currently doing: what's in the staging area, what untracked files there are, etc.
    #git log -1 displays the  previous commit and associated information
# 15) What’s the difference between cloning a repository and pulling from it?
    #cloning a repo makes a copy of it in your directory, while pulling from it lets you take changes from the remote repositiory 
    #and put them into your clone of it
# 16) What has been your most frustrating bug or error in this class so far? How did you troubleshoot or fix it?
    #I accidentally put a git repo inside another git repo... enough said... took an hour to fix
# 17) What’s a question you still have? What’s something you’re confused about?
    #Why do you sometimes need to run git push origin main? I used to just do git push and it also worked. 
# 18) Tell me a fun fact!
    # Lions have nicitating membranes (transluscent second eyelid)
# 19) Print your favorite math expression you've learned in Python so far. 
# (Hint: Use print() and add a comment explaining what it does.)

print(5//2)
#Floor division! It rounds the value produced by the division down to the nearest whole integer