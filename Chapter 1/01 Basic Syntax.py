


##########################################
#### Chapter 01 - Python ###### [01] #####
##########################################
### What is & History

## Python is a high-level, interpreted, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation. Python is dynamically-typed and garbage-collected.

## [History] Python was invented in the late 1980s by "Guido van Rossum"

    # [01] Python is a popular programming language.
    # [02] Python can be used on a server to "create web applications". or Software



##########################################
#### Chapter 01 - Python ###### [02] #####
##########################################
### Python Install

## Many PCs and Macs will have python already installed.

## [01] To check if you have python installed on a Windows PC, search in the start bar for Python or run the following on the Command Line (cmd.exe):
# >>> C:\Users\Your Name>python --version

## [02] To check if you have python installed on a Linux or Mac, then on linux open the command line or on Mac open the Terminal and type:
# >>> python --version


# If you find that you do not have Python installed on your computer, then you can download it for free from the following website: https://www.python.org/



##########################################
#### Chapter 01 - Python ###### [03] #####
##########################################
### [First] Python Program

# Let us execute a Python program to print "Hello, World!" in two different modes of Python Programming. 
    # (a) Interactive Mode Programming.
    # (b) Script Mode Programming.

print ("Hello, World!")

## [Output] >>> Hello, World!



##########################################
#### Chapter 01 - Python ###### [04] #####
##########################################
### File Run Command
# >>> C:\Users\Your Name> python3 test.py

# The output should read:
# [Output] >>> Hello, World!


### The Python Command Line
## To test a short amount of code in python sometimes it is quickest and easiest not to write the code in a file. This is made possible because Python can be run as a command line itself.

## Type the following on the Windows, Mac or Linux command line:
## >>> C:\Users\Your Name>python

## Or, if the "python" command did not work, you can try "py":
## >>> C:\Users\Your Name>py



##########################################
#### Chapter 01 - Python ###### [05] #####
##########################################
### Exit CMD Interface 

## Whenever you are done in the python command line, you can simply type the following to quit the python command line interface:

## >>> exit()



##########################################
#### Chapter 01 - Python ###### [06] #####
##########################################
### Most Important [Python Indentation]

## Indentation refers to the spaces at the beginning of a code line.

## Where in other programming languages the indentation in code is for readability only, the indentation in Python is very important.


## Python uses indentation to indicate a block of code.

# if 5 > 2:
#   print("Five is greater than two!")


## Python will give you an error if you skip the indentation:

# if 5 > 2:
#  print("Five is greater than two!") 
# if 5 > 2:
#         print("Five is greater than two!") 


## The number of spaces is up to you as a programmer, the most common use is four, but it has to be at least one.

# if 5 > 2:
#     print("Five is greater than two!")

## You have to use the same number of spaces in the same block of code, otherwise Python will give you an error:

# if 5 > 2:
#  print("Five is greater than two!")
#         print("Five is greater than two!")